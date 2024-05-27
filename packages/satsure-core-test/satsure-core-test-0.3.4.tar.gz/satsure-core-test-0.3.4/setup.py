from setuptools import setup, find_packages


setup(
    name='satsure-core-test',
    version='0.3.4',
    description='satsure core package',
    author='Satsure',
    author_email='kmstpm@email.com',
    packages=find_packages(),
    install_requires=['awscli','boto3', 'fiona','gdal==3.6.2', 'google-cloud-storage', 'pandas',
                      'pyproj', 'pystac','pystac-client', 'python-dotenv', 'rasterstats',
                      'rasterio', 'requests', 'requests', 'sqlalchemy', 'wget']
)
