import re
from pathlib import Path

import pytest

import satsure_core.satelite.gdal._projection
from satsure_core.satelite.gdal import get_projection


class TestGetProjection:
    """test get projection"""

    def test_get_projection(self, datadir: Path) -> None:
        """get the projection

        Args:
            datadir (Path): input path
        """
        input_file = datadir / "input1.tif"
        projection = get_projection(str(input_file))
        assert projection == "EPSG:32644"

    def test_error(self, mocker):
        mocker.patch("satsure_core.satelite.gdal._projection.subprocess")
        satsure_core.satelite.gdal._projection.subprocess.check_output.return_value = (
            "Error: Test exception".encode("utf-8")
        )

        with pytest.raises(Exception) as exc_info:
            projection = get_projection("mock_file_path")
        assert str(exc_info.value) == "Error: Test exception"

    def test_no_projection_code(self, mocker, datadir):
        mocker.patch("re.findall")
        re.findall.return_value = []

        file_path = str(datadir / "input1.tif")
        with pytest.raises(Exception) as exc_info:
            projection = get_projection(file_path)
        assert (
            str(exc_info.value)
            == "Cannot find projection, currently supports only EPSG based projections"
        )
