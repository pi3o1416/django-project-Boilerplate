import os
from pathlib import Path
from environ import Env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DEV_CONFIG_PATH = os.path.join(BASE_DIR, 'dev.env')
PROD_CONFIG_PATH = os.path.join(BASE_DIR, '.env')
assert os.path.exists(DEV_CONFIG_PATH) ^ os.path.exists(PROD_CONFIG_PATH), \
    "Either create a file dev.env of .env but not both"

if os.path.exists(PROD_CONFIG_PATH):
    Env.read_env(PROD_CONFIG_PATH)
    from .prod import *
else:
    Env.read_env(DEV_CONFIG_PATH)
    from .dev import *
