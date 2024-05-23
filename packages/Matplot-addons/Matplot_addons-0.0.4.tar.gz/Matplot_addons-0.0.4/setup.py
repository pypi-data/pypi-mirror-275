import pathlib
from setuptools import find_packages, setup


# Data
HERE = pathlib.Path(__file__).parent

VERSION = '0.0.4' 
PACKAGE_NAME = 'Matplot_addons' # NName of the folder
AUTHOR = 'Sergio de Avila' 
AUTHOR_EMAIL = 'sergiodeavilacabral@gmail.com' 
URL = 'https://github.com/Sergiodeavilac' 

LICENSE = 'GPL-3.0' 
DESCRIPTION = 'Matplotlib addons for simplify life' # Short description
LONG_DESCRIPTION = (HERE.parent / "README.md").read_text(encoding='utf-8') #Reference to the readme file
LONG_DESC_TYPE = "text/markdown"


# Install requirements
INSTALL_REQUIRES = [
      'matplotlib'
      ]

# Setup of the lib 
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)