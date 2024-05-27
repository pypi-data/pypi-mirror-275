from setuptools import setup
import sys,os,os.path

DESCRIPTION = "DStokuron report"
NAME = 'maps_restaurants'
AUTHOR = 'Gilles Sonntag'
AUTHOR_EMAIL = 's2222021@stu.musashino-u.ac.jp'
URL = 'https://github.com/SONNTAGGilles/PyPi-package/tree/main/my_python_packges'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/SONNTAGGilles/PyPi-package'
VERSION = '0.0.1'
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    'matplotlib>=3.3.4',
    'osmnx',
    'networkX',
    'notebook',
]

setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
    )