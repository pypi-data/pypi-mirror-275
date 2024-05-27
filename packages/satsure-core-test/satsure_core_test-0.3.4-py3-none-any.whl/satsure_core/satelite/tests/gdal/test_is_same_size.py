import pytest

from satsure_core.satelite.gdal import is_same_size


class TestIsSameSize:
    """Test whether two rasters are of same size"""

    def test_rasters_with_same_sizes(self, datadir):
        raster_1 = datadir / "input1.tif"
        raster_2 = datadir / "input2.tif"

        assert is_same_size(str(raster_1), str(raster_2))

    def test_rasters_with_different_sizes(self, datadir):
        raster_1 = datadir / "input1.tif"
        raster_2 = datadir / "input4.tif"

        assert not is_same_size(str(raster_1), str(raster_2))

    def test_with_non_existing_file(self, datadir):
        raster_1 = datadir / "input1.tif"
        raster_2 = datadir / "non_existing_file.tif"

        with pytest.raises(AttributeError) as exc_info:
            is_same_size(str(raster_1), str(raster_2))

        assert str(exc_info.value) == "'NoneType' object has no attribute 'RasterXSize'"
