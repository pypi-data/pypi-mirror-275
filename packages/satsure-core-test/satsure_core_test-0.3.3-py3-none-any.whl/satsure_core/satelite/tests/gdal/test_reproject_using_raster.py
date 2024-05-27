from pathlib import Path

from satsure_core.satelite.gdal import (
    get_extents,
    get_projection,
    get_resolution,
    reproject_using_raster,
)


class TestReprojectUsingRaster:
    """Test reprojection of a raster to the
    projection, extents and resolution of another raster
    """

    def test_reproject_using_raster(self, datadir):
        raster_path = str(datadir / "raster_for_reprojection.tif")
        target_raster_path = str(datadir / "target_for_reprojection.tif")
        output_path = str(datadir / "reprojection_output.tif")

        raster_projection = get_projection(raster_path)
        raster_extent = get_extents(raster_path)
        raster_resolution = get_resolution(raster_path)

        target_projection = get_projection(target_raster_path)
        target_extent = get_extents(target_raster_path)
        target_resolution = get_resolution(target_raster_path)

        reproject_using_raster(raster_path, target_raster_path, output_path)

        output_projection = get_projection(output_path)
        output_extent = get_extents(output_path)
        output_resolution = get_resolution(output_path)

        assert raster_projection != target_projection
        assert raster_extent != target_extent
        assert raster_resolution != target_resolution

        assert output_projection == target_projection
        assert output_extent == target_extent
        assert output_resolution == target_resolution

        Path(output_path).unlink()
