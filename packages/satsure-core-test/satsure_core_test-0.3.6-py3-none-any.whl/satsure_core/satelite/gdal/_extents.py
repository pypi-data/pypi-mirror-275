import subprocess
from typing import Tuple

from osgeo import gdal
from osgeo.gdalconst import GA_ReadOnly


def get_extents(raster_path: str) -> Tuple[float, float, float, float]:
    """
    Get the X and Y extents of a raster

    :param raster_path: Path of the raster
    :returns: A tuple containing the extents (min-x, min-y, max-x, max-y)
    """
    data = gdal.Open(raster_path, GA_ReadOnly)
    geoTransform = data.GetGeoTransform()
    min_x = geoTransform[0]
    max_y = geoTransform[3]
    max_x = min_x + (geoTransform[1] * data.RasterXSize)
    min_y = max_y + (geoTransform[5] * data.RasterYSize)

    return (min_x, min_y, max_x, max_y)


def set_extents(
    min_x: float,
    min_y: float,
    max_x: float,
    max_y: float,
    raster_path: str,
    output_path: str,
) -> None:
    """
    Set the X and Y extents of a raster

    :param min_x:
    :param min_y:
    :param max_x:
    :param max_y:
    :param raster_path: Path of the raster for which extents are to be set
    :param output_path: Path of output raster
    """
    command = f"gdalwarp -overwrite -te {min_x} {min_y} {max_x} {max_y} {raster_path} {output_path}"

    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode("utf-8"))
