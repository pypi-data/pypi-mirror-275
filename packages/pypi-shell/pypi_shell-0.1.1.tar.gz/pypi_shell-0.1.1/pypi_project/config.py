import os

PACKAGE_NAME = "pypi-shell"
COMMAND_NAME = "pypi"
PACKAGE_VERSION = '0.1.1'
PACKAGE_PATH = os.path.dirname(__file__)
DATA_PATH = os.path.join(PACKAGE_PATH, 'data')
os.makedirs(DATA_PATH, exist_ok=True)
