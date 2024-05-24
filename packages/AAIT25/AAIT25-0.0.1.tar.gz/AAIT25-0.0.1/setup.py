#pypi-AgEIcHlwaS5vcmcCJGUzNzMyY2Y2LWI3NTAtNGI4Zi1iYzg1LWM3N2ZmMjk4NWFjNwACKlszLCIzMzliODczOC0yN2EwLTRlNzUtOGIwYi01ZTY3ZGQzNTJkOGEiXQAABiCSIWaaQx6SJ-eUbj6VSMw10g8Wt55CZldeWkw2whOk2Q

from setuptools import setup, find_packages

# Nom du package PyPI
NAME = "AAIT25"

# Version du package PyPI
VERSION = "0.0.1"  # la version doit être supérieure à la précédente sinon la publication sera refusée

# Facultatif / Adaptable à souhait
AUTHOR = "Orange community"
AUTHOR_EMAIL = ""
URL = ""
DESCRIPTION = ("Advanced Artificial Intelligence Tools is a package meant to develop "
               "and enable advanced AI functionalities in Orange Data Mining.")
LICENSE = ""

# 'orange3 add-on' permet de rendre l'addon téléchargeable via l'interface addons d'Orange 
KEYWORDS = ("orange3 add-on",)

# Tous les packages python existants dans le projet
PACKAGES = find_packages()

# Fichiers additionnels aux fichiers .py (comme les icons ou des .ows)
# PACKAGE_DATA = {
# 	"orangecontrib.AAIT.widgets.base": ["designer/*", "icons/*"],
# 	"orangecontrib.AAIT.widgets.encapsulation": ["designer/*", "icons/*"],
# 	"orangecontrib.AAIT.widgets.llm": ["designer/*", "icons/*"],
# 	"orangecontrib.AAIT.widgets.optimiser": ["designer/*", "icons/*"],
# }
#

# Dépendances
INSTALL_REQUIRES = ["sentence-transformers==2.5.1"]

# Spécifie le dossier contenant les widgets et le nom de section qu'aura l'addon sur Orange
ENTRY_POINTS = {
    "orange.widgets": (
        "AAIT = orangecontrib.AAIT.widgets",
    )
}

NAMESPACE_PACKAGES = ["orangecontrib"]

setup(name=NAME,
      version=VERSION,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      url=URL,
      description=DESCRIPTION,
      license=LICENSE,
      keywords=KEYWORDS,
      packages=PACKAGES,
      # package_data=PACKAGE_DATA,
      install_requires=INSTALL_REQUIRES,
      entry_points=ENTRY_POINTS,
      namespace_packages=NAMESPACE_PACKAGES,
      )
