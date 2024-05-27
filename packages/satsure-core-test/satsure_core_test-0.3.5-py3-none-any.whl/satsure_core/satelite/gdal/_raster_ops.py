import subprocess
from pathlib import Path, PosixPath
from tempfile import NamedTemporaryFile
from typing import Dict, Optional, Tuple, Union

from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly

from satsure_core.satelite.core import Downloader


def create_jpeg_image(
    input_file: PosixPath,
    output_file: Optional[str] = None,
    bands_position: Tuple[int, int, int] = (3, 2, 1),
    quality: int = 10,
    target_resolution: int = 100,
):
    """Generates JPG image for a given tif

    Args:
        input_file (PosixPath): Path of the input file
        output_file (Optional[PosixPath], optional): Output path for the file. If not proivded, defaults to input file by changing extension. Defaults to None.
        quality (int): Compression ratio. (how much you want to compress)
        bands_position (Iterable[int, int, int], optional): List of rgb bands to use. Defaults to (3, 2, 1).
        target_resolution (int, optional): Target resolution. Defaults to 100.
    """
    if output_file is None:
        output_file = f"{str(input_file)[:-4]}.jpg"

    command = ("gdal_translate", "-of", "JPEG", "-scale", "-ot", "Byte")
    for band in bands_position:
        command += ("-b", f"{band}")
    command += (
        "-tr",
        f"{target_resolution}",
        f"{target_resolution}",
        "-co",
        f"QUALITY={int(quality)}",
        f"{input_file}",
        f"{output_file}",
    )
    subprocess.run(command, shell=False, capture_output=True)


def is_same_size(raster_path_1: str, raster_path_2: str) -> bool:
    """
    Compare size (width, height) of two rasters

    :param raster_path_1: Path of first raster
    :param raster_path_2: Path of second raster
    :returns: Boolean value
    """
    raster_1 = gdal.Open(raster_path_1, GA_ReadOnly)
    raster_2 = gdal.Open(raster_path_2, GA_ReadOnly)
    return (raster_1.RasterXSize, raster_1.RasterYSize) == (
        raster_2.RasterXSize,
        raster_2.RasterYSize,
    )


def mask(
    raster_path: str,
    mask_raster_path: str,
    output_path: str,
    no_data_value: int = 0,
) -> None:
    """
    Mask a specified raster using another raster

    :param raster_path: Path of raster that needs to be masked
    :param mask_raster_path: Path of mask raster
    :param output_path: Path of output raster
    :param no_data_value: Value to use for `No Data` pixels (Defaults to 0)
    """
    command = f'gdal_calc.py -A {raster_path} -B {mask_raster_path} --outfile={output_path} --calc="A*B" --NoDataValue={no_data_value}'

    subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)


def clip_with_shp(
    input_file: PosixPath,
    shp_path: PosixPath,
    output_folder: PosixPath,
    output_file: Union[str, None] = None,
) -> PosixPath:
    """
    Function to clip a raster file using a shapefile

    Parameters:
        input_file          - str, path to the raster file to be clipped
        shpFile             - str, path to the shapefile by which input_file should
                              be clipped
        destFolder          - str, path to folder which the clipped file will
                              be written
        out_fname           - str, optional, file name (only file name not path
                              ) for output, if not given, then fname filename
                              will be taken
        crop_to_intersection- bool, whether the croping should be done to the
                              intersection of raster and the vector
    """
    suffix = input_file.split(".")[-1]
    s3_temp_file = False
    if input_file[:5] == "s3://":
        s3_temp_file = True
        input_file_local = NamedTemporaryFile(delete=False, suffix=f".{suffix}")
        Downloader().download_object_from_s3(input_file, input_file_local.name)
        if suffix == "jpg":
            Downloader().download_object_from_s3(
                f"{input_file}.aux.xml", f"{input_file_local.name}.aux.xml"
            )
        input_file = Path(input_file_local.name)
    else:
        input_file = Path(input_file)
    shp_path = Path(shp_path)
    output_folder = Path(output_folder)
    output_folder.mkdir(exist_ok=True, parents=True)

    file_name = input_file.name

    if output_file is not None:
        out_fname_path = Path(output_file)
        file_name = out_fname_path.stem + input_file.suffix
    outFile = output_folder.joinpath(file_name)
    command = (
        "gdalwarp",
        "-q",
        "-srcnodata",
        "0",
        "-dstnodata",
        "0",
        "-overwrite",
        f"{input_file}",
        f"{outFile}",
        "-cutline",
        f"{shp_path}",
        f"-crop_to_cutline",
        "-co",
        "COMPRESS=LZW",
    )
    resp = subprocess.run(command, shell=False, capture_output=True)
    if s3_temp_file:
        input_file_local.close()
        input_file.unlink()
        if suffix == "jpg":
            Path(f"{input_file_local.name}.aux.xml").unlink()
    if resp.returncode != 0:
        raise ValueError()

    return outFile


def get_file_info(input_file: PosixPath, crs: bool = False, stats: bool = True) -> Dict:
    """
        Getting file info using rio
    :param input_file:
    :param crs:
    :param stats:
    :return:
    """

    result = {}
    if crs:
        command = ("rio", "info", f"--crs", f"{input_file}")
        resp = subprocess.run(command, shell=False, capture_output=True)
        if resp.returncode == 0:
            result.update({"crs": resp.stdout.decode("utf-8").replace("\n", "")})
    if stats:
        command = ("rio", "info", f"--stats", f"{input_file}")
        resp = subprocess.run(command, shell=False, capture_output=True)
        if resp.returncode == 0:
            stats = resp.stdout.decode("utf-8").replace("\n", "").split(" ")
            result.update(
                {"stats": {"min": stats[0], "max": stats[1], "mean": stats[2]}}
            )

    return result
