from satsure_core.satelite.gdal import get_extents


class TestGetExtents:
    """Test getting the extents of a raster"""

    def test_get_extents(self, datadir):
        raster_path = str(datadir / "input1.tif")

        extents = get_extents(raster_path)

        assert extents == (353110.0, 1627160.0, 354110.0, 1628160.0)
