import pathlib
from typing import Dict, List
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '0.0.1'  # Muy importante, deberéis ir cambiando la versión de vuestra librería según incluyáis nuevas funcionalidades
PACKAGE_NAME = 'altair_easeviz'  # Debe coincidir con el nombre de la carpeta
AUTHOR = 'Miguel Huayllas'  # Modificar con vuestros datos
AUTHOR_EMAIL = 'mhuaylch10@alumnes.ub.edu'  # Modificar con vuestros datos
URL = 'https://www.linkedin.com/in/miguel-huayllas/'  # Modificar con vuestros datos

LICENSE = 'MIT'  # Tipo de licencia
DESCRIPTION = 'Librería para leer ficheros PDFs y extraer la información en formato str'  # Descripción corta
LONG_DESCRIPTION = (HERE / "README.md").read_text(
    encoding='utf-8')  # Referencia al documento README con una descripción más elaborada
LONG_DESC_TYPE = "text/markdown"

# Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado


ENTRY_POINTS: Dict[str, List[str]] = {
    # Group: https://github.com/altair-viz/altair/blob/v4.2.0/altair/vegalite/v4/theme.py#L35
    "altair.vegalite.v5.theme": [
        "accessible_theme = altair_easeviz.themes:accessible_theme",
        "dark_accessible_theme = altair_easeviz.themes:dark_accessible_theme",
        "filler_pattern_theme = altair_easeviz.themes:filler_pattern_theme",
        "print_theme = altair_easeviz.themes:print_friendly_theme",
    ],
}
DEPENDENCIES: List[str] = ["altair==5.*", "typing-extensions>=4.0, <5", "jinja2==3.*"]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=DEPENDENCIES,
    entry_points=ENTRY_POINTS,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)
