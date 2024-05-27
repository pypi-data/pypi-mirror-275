import re
import subprocess
import tempfile
from pathlib import PosixPath

from satsure_core.satelite.gdal._extents import get_extents, set_extents
from satsure_core.satelite.gdal._resolution import get_resolution, set_resolution


def get_projection(file_path: str) -> str:
    """
    Function to get projection of file (Vector / Raster)
    Currently supports only EPSG based projections
    :param file_path:
    :return:
    """
    command = f"gdalsrsinfo {file_path} -e"
    projection_str = subprocess.check_output(
        command, stderr=subprocess.STDOUT, shell=True
    )

    if "error" in projection_str.decode("utf-8")[:20].lower():
        raise Exception(projection_str.decode("utf-8"))

    projection_code = re.findall(rb"\nEPSG:(.+?)\n", projection_str)
    if not projection_code:
        raise Exception(
            "Cannot find projection, currently supports only " "EPSG based projections"
        )

    return f"EPSG:{projection_code[0].decode('utf-8')}"


def reproject_raster(
    input_file: PosixPath, output_file: PosixPath, target_crs: str
) -> None:
    """
    Reproject a raster to a specified SRS

    :param input_file:
    :param output_file:
    :param target_crs:
    :return:
    """
    command = ("gdalwarp", "-t_srs", f"{target_crs}", f"{input_file}", f"{output_file}")
    subprocess.run(command, shell=False, capture_output=True)


def reproject_vector(vector_path: str, output_path: str, target_srs: str) -> None:
    """
    Reproject a vector to a specified SRS

    :param vector_path: Path of vector file
    :param output_path: Path of reprojected vector file
    :param target_srs: SRS to which the input vector needs to be reprojected to
    """
    command = f"ogr2ogr -t_srs {target_srs} {output_path} {vector_path}"
    result = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    if "error" in result.decode("utf-8")[:20].lower():
        raise Exception(result.decode("utf-8"))


def reproject_using_raster(
    raster_path: str, target_raster_path: str, output_path: str
) -> None:
    """
    Reproject a given raster to the SRS, extent and resolution of target raster

    :param raster_path: Path of the raster to reproject
    :param target_raster_path: Path of the target raster
    :param output_path: Path of output raster
    """

    with tempfile.NamedTemporaryFile() as temp_path_1:
        target_crs = get_projection(target_raster_path)
        reproject_raster(raster_path, temp_path_1.name, target_crs)

        with tempfile.NamedTemporaryFile() as temp_path_2:
            extents = get_extents(target_raster_path)
            set_extents(
                extents[0],
                extents[1],
                extents[2],
                extents[3],
                temp_path_1.name,
                temp_path_2.name,
            )

            resolution = get_resolution(target_raster_path)
            set_resolution(resolution[0], resolution[1], temp_path_2.name, output_path)
