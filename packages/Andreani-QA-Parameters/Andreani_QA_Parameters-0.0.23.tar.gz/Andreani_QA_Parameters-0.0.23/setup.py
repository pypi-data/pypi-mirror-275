import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.23'
PACKAGE_NAME = 'Andreani_QA_Parameters'  # Debe coincidir con el nombre de la carpeta
AUTHOR = 'AndreaniTesting'
AUTHOR_EMAIL = 'user_appglatest@andreani.com'
URL = ''

LICENSE = 'MIT'  # Tipo de licencia
DESCRIPTION = 'Parametros + Encriptor para ejecución de casos automatizados'  # Descripción corta
LONG_DESCRIPTION = ""
LONG_DESC_TYPE = "text/markdown"

# Paquetes necesarios para que funcione la librería. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
]

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
