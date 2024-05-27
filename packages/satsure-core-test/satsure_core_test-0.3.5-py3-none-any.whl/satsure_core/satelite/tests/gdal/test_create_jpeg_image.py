import os.path
from pathlib import Path

from satsure_core.satelite.gdal import create_jpeg_image


class TestCreateJPEGImage:
    """create JPEG Images"""

    def test_create_jpeg_image(self, datadir: Path) -> None:
        """_summary_

        Args:
            datadir (Path): path of input
        """
        input_file = datadir / "input1.tif"
        output_file = datadir / "output_image.jpeg"
        create_jpeg_image(
            input_file=input_file, bands_position=("1"), output_file=str(output_file)
        )

        assert (
            output_file.suffix.lower() == ".jpg"
            or output_file.suffix.lower() == ".jpeg"
        )
        output_file.unlink()

    def test_output_file_is_none(self, datadir):
        input_file = datadir / "input1.tif"
        expected_output_file = datadir / "input1.jpg"

        assert not os.path.isfile(str(expected_output_file))
        create_jpeg_image(input_file=input_file, bands_position=("1"))
        assert os.path.isfile(str(expected_output_file))

        expected_output_file.unlink()
