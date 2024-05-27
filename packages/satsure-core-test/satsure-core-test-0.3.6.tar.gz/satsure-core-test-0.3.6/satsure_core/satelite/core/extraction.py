import subprocess


def extract(
    raster_path: str, polygon_path: str, field: str, stat_fn: str, output_path: str
) -> None:
    """
    Extract zonal stats using exactextract

    :param raster_path: Path of input raster
    :param polygon_path: Path of input vector
    :param field: Attribute which uniquely identifies each feature in vector file
    :param stat_fn: Stats function to use for zonal stats
    :output_path: Path of output file
    """

    command = f"exactextract -r RASTER:{raster_path} -p {polygon_path} -f '{field}' -s 'stat_value={stat_fn}(RASTER)' -o {output_path}"

    try:
        subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
    except subprocess.CalledProcessError as e:
        raise Exception(e.output.decode("utf-8"))
