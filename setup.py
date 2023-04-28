from setuptools import setup

setup(
    name='my-package',
    version='0.1',
    author='BillowDev',
    author_email='akkarapon@billowdev.com',
    description='just a generate lat lng value within given range',
    packages=['random_lat_lng_point'],
    install_requires=[
        'geopy',
    ],
)
