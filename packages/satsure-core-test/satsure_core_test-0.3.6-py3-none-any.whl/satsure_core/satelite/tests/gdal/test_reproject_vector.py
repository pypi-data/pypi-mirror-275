import pytest

import satsure_core.satelite.gdal._projection
from satsure_core.satelite.gdal import reproject_vector


class TestReprojectVector:
    """Test reprojecting a vector to a specified CRS"""

    def test_reproject_vector_command(self, mocker):
        mocker.patch("satsure_core.satelite.gdal._projection.subprocess")

        expected_command = "ogr2ogr -t_srs EPSG:XXXX mock_output_path mock_vector_path"

        reproject_vector("mock_vector_path", "mock_output_path", "EPSG:XXXX")
        satsure_core.satelite.gdal._projection.subprocess.check_output.assert_called_with(
            expected_command,
            stderr=satsure_core.satelite.gdal._projection.subprocess.STDOUT,
            shell=True,
        )

    def test_error(self, mocker):
        mocker.patch("satsure_core.satelite.gdal._projection.subprocess")
        satsure_core.satelite.gdal._projection.subprocess.check_output.return_value = (
            "Error: Test exception".encode("utf-8")
        )

        with pytest.raises(Exception) as exc_info:
            reproject_vector("mock_vector_path", "mock_output_path", "EPSG:XXXX")
        assert str(exc_info.value) == "Error: Test exception"

    def test_retval(self, mocker):
        mocker.patch("satsure_core.satelite.gdal._projection.subprocess")
        retval = reproject_vector("mock_vector_path", "mock_output_path", "EPSG:XXXX")
        assert retval is None
