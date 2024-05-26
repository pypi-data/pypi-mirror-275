
from satsure_core.satelite.sentinel2 import MosaicCustomBands

class TestMosaicCustomBands:



    def test_custom_bands(self):
        data ={'input_files': ['s3://satsure-satimg/IS18021/T43PCT/20240324_T43PCT_IS18021.tif',
                               's3://satsure-satimg/IS18021/T43PCT/20240329_T43PCT_IS18021.tif'],
               'output_folder': '/Users/meenakshisundaram/Documents/tc/TCX8021/T43PCT/',
               'output_name': '20240401_T43PCT_TCX8021.tif', 'output_nodata_value': 0, 'output_datatype': 'uint8'}
        MosaicCustomBands(**data).mosaic_custom()
