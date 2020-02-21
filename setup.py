from setuptools import setup, find_packages
from numpy.distutils.core import setup
from numpy.distutils.extension import Extension
#import distutils.extension

extensions_list=[]

setup(
    name='REMD_testbed',
    version='0.0.1',
    author='UIBCDF Lab',
    author_email='uibcdf@gmail.com',
    package_dir={'remd_testbed': 'remd_testbed'},
    packages=find_packages(),
    ext_modules=extensions_list,
    package_data={'remd_testbed': []},
    scripts=[],
    url='http://uibcdf.org',
    download_url ='https://github.com/uibcdf/REMD_testbed',
    license='MIT',
    description="---",
    long_description="---",
)

