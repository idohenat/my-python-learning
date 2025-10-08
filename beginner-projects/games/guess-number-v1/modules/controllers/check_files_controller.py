import os 

from config import attemps_save_file, numbers_save_file
from modules.controllers.write_defaults_vars_contoller import write_defaults

def check_on_saves_exists():
    files = [attemps_save_file, numbers_save_file]

    for file in files:
        if os.path.exists(file):
            pass
        else:
            write_defaults()