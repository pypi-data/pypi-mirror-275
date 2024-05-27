import subprocess
from typing import Tuple

from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly


def get_resolution(raster_path: str) -> Tuple[float, float]:
    """
    Get the X and Y resolution of a raster

    :param raster_path: Path of the raster
    :returns: A tuple containing the X and Y resolution (x-res, y-res)
    """
    data = gdal.Open(raster_path, GA_ReadOnly)
    geoTransform = data.GetGeoTransform()
    x_res = geoTransform[1]
    y_res = geoTransform[-1]

    return (x_res, y_res)


def set_resolution(
    x_res: float, y_res: float, raster_path: str, output_path: str
) -> None:
    """
    Set the X and Y resolution of a raster

    :param x_res:
    :param y_res:
    :param raster_path: Path of the raster for which resolution is to be set
    :param output_path: Path of output raster
    """

    command = f"gdal_translate -tr {x_res} {y_res} {raster_path} {output_path}"

    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode("utf-8"))
