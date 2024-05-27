import satsure_core.satelite.gdal._raster_ops
from satsure_core.satelite.gdal import mask


class TestMask:
    """Test masking of a raster"""

    def test_mask_command(self, mocker):
        mocker.patch("satsure_core.satelite.gdal._raster_ops.subprocess")

        expected_command = 'gdal_calc.py -A mock_raster_path -B mock_mask_raster_path --outfile=mock_output_path --calc="A*B" --NoDataValue=0'

        mask("mock_raster_path", "mock_mask_raster_path", "mock_output_path")
        satsure_core.satelite.gdal._raster_ops.subprocess.check_output.assert_called_with(
            expected_command,
            stderr=satsure_core.satelite.gdal._raster_ops.subprocess.STDOUT,
            shell=True,
        )

    def test_mask_command_with_custom_nodatavalue(self, mocker):
        mocker.patch("satsure_core.satelite.gdal._raster_ops.subprocess")

        expected_command = 'gdal_calc.py -A mock_raster_path -B mock_mask_raster_path --outfile=mock_output_path --calc="A*B" --NoDataValue=1'

        mask(
            "mock_raster_path",
            "mock_mask_raster_path",
            "mock_output_path",
            no_data_value=1,
        )
        satsure_core.satelite.gdal._raster_ops.subprocess.check_output.assert_called_with(
            expected_command,
            stderr=satsure_core.satelite.gdal._raster_ops.subprocess.STDOUT,
            shell=True,
        )

    def test_retval_is_none(self, mocker):
        mocker.patch("satsure_core.satelite.gdal._raster_ops.subprocess")
        retval = mask("mock_raster_path", "mock_mask_raster_path", "mock_output_path")
        assert retval is None
