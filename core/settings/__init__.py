import os
from pathlib import Path
from environ import Env

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
CONFIG_PATH = os.path.join(BASE_DIR, '.env')
Env.read_env(CONFIG_PATH)
env = Env()
if env is not None:
    current_stage = env('STAGE')
    if current_stage == 'PROD':
        from .prod import *
    elif current_stage == 'DEV':
        from .dev import *
else:
    raise FileNotFoundError('Env file does not exist')
