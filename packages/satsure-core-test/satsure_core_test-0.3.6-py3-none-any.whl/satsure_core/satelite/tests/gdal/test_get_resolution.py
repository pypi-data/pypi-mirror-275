from satsure_core.satelite.gdal import get_resolution


class TestGetResolution:
    """Test getting resolution of a raster"""

    def test_get_resolution(self, datadir):
        raster_path = str(datadir / "input1.tif")

        resolution = get_resolution(raster_path)

        assert resolution == (10, -10)
