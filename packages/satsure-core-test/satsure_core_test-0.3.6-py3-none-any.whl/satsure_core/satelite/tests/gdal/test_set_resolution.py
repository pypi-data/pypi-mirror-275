import pytest

import satsure_core.satelite.gdal._resolution
from satsure_core.satelite.gdal import set_resolution


class TestSetResolution:
    """Test setting of resolution to a raster"""

    def test_set_resolution(self, mocker):
        mocker.patch("satsure_core.satelite.gdal._resolution.subprocess")

        expected_command = (
            "gdal_translate -tr 10.0 -10.0 mock_raster_path.tif mock_output_path.tif"
        )

        set_resolution(10.0, -10.0, "mock_raster_path.tif", "mock_output_path.tif")
        satsure_core.satelite.gdal._resolution.subprocess.check_output.assert_called_with(
            expected_command,
            stderr=satsure_core.satelite.gdal._resolution.subprocess.STDOUT,
            shell=True,
        )

    def test_exception(self):
        with pytest.raises(Exception) as exc_info:
            set_resolution(10.0, -10.0, "mock_raster_path.tif", "mock_output_path.tif")

        assert (
            str(exc_info.value)
            == "ERROR 4: mock_raster_path.tif: No such file or directory\n"
        )
