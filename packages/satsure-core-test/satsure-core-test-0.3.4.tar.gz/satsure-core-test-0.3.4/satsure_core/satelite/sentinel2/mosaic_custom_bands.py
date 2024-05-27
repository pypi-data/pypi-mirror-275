from dataclasses import dataclass
from os import environ
from pathlib import Path, PosixPath
from typing import List

import boto3
import rasterio
from rasterio.merge import merge as rio_merge
from rasterio.session import AWSSession


@dataclass
class MosaicCustomBands:
    input_files: List[PosixPath]
    output_folder: PosixPath
    output_name: PosixPath
    output_nodata_value: int = 0
    output_datatype: str = "uint8"

    def mosaic_custom(self):
        """
            mosaic custom bands
        :return:
        """
        output_folder = Path(self.output_folder)
        output_folder.mkdir(exist_ok=True, parents=True)
        output_path = Path(f"{output_folder}/{self.output_name}")

        boto3_session = boto3.Session(aws_access_key_id=environ.get("AWS_ACCESS_KEY_ID", None),
                                      aws_secret_access_key=environ.get("AWS_SECRET_ACCESS_KEY", None),
                                      region_name=environ.get("AWS_DEFAULT_REGION", None))
        with rasterio.Env(AWSSession(boto3_session), AWS_REQUEST_PAYER='requester'):
            src_files_to_mosaic = []
            for path in self.input_files:
                final = rasterio.open(path)
                src_files_to_mosaic.append(final)
            rio_merge(src_files_to_mosaic,
                      nodata=self.output_nodata_value,
                      dtype=self.output_datatype,
                      method='max',
                      dst_path=output_path)
