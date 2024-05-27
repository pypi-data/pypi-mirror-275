import pytest

import satsure_core.satelite.gdal._extents
from satsure_core.satelite.gdal import set_extents


class TestSetExtents:
    """Test setting of extents to a raster"""

    def test_set_extents(self, mocker):
        mocker.patch("satsure_core.satelite.gdal._extents.subprocess")

        expected_command = f"gdalwarp -overwrite -te 0.0 0.0 1.0 1.0 mock_raster_path.tif mock_output_path.tif"

        set_extents(0.0, 0.0, 1.0, 1.0, "mock_raster_path.tif", "mock_output_path.tif")
        satsure_core.satelite.gdal._extents.subprocess.check_output.assert_called_with(
            expected_command,
            stderr=satsure_core.satelite.gdal._extents.subprocess.STDOUT,
            shell=True,
        )

    def test_exception(self):
        with pytest.raises(Exception) as exc_info:
            set_extents(
                0.0, 0.0, 1.0, 1.0, "mock_raster_path.tif", "mock_output_path.tif"
            )

        assert (
            str(exc_info.value)
            == "ERROR 4: mock_raster_path.tif: No such file or directory\nERROR 4: Failed to open source file mock_raster_path.tif\n\n"
        )
