from pathlib import Path

import pandas as pd
import pytest

import satsure_core.satelite.core.extraction
from satsure_core.satelite.core import extract
from satsure_core.satelite.gdal import get_projection, reproject_vector


class TestExtraction:
    """Test stats extraction command"""

    def test_extraction(self, mocker):
        mocker.patch("satsure_core.satelite.core.extraction.subprocess")
        extract(
            "mock_raster_path",
            "mock_polygon_path",
            "test_field",
            "test_stat_fn",
            "mock_output_path",
        )

        expected_command = "exactextract -r RASTER:mock_raster_path -p mock_polygon_path -f 'test_field' -s 'stat_value=test_stat_fn(RASTER)' -o mock_output_path"
        satsure_core.satelite.core.extraction.subprocess.check_output.assert_called_with(
            expected_command,
            stderr=satsure_core.satelite.core.extraction.subprocess.STDOUT,
            shell=True,
        )

    def test_exception(self):
        with pytest.raises(Exception) as exc_info:
            extract(
                "mock_raster_path",
                "mock_polygon_path",
                "test_field",
                "test_stat_fn",
                "mock_output_path",
            )

        assert (
            str(exc_info.value)
            == "ERROR 4: mock_raster_path: No such file or directory\nError: Failed to open mock_raster_path\n"
        )

    def test_extracted_output(self, extraction_testdata_dir):
        raster_path = f"{extraction_testdata_dir}/extraction_raster.tif"
        polygon_path = f"{extraction_testdata_dir}/extraction_polygon.geojson"
        reprojected_polygon_path = (
            f"{extraction_testdata_dir}/reprojected_polygon.geojson"
        )
        output_path = f"{extraction_testdata_dir}/extraction_output.csv"

        raster_projection = get_projection(raster_path)
        reproject_vector(polygon_path, reprojected_polygon_path, raster_projection)

        extract(raster_path, reprojected_polygon_path, "rid", "mean", output_path)

        columns = ["rid", "stat_value"]
        data = [
            ("91028021003015", "160.251617431641"),
            ("91028021003049", "159.133560180664"),
        ]
        expected_df = pd.DataFrame(data=data, columns=columns)
        output_df = pd.read_csv(output_path, dtype=str)

        pd.testing.assert_frame_equal(output_df, expected_df)

        Path(reprojected_polygon_path).unlink()
        Path(output_path).unlink()
