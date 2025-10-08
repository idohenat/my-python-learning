from modules.controllers.SaveControllers.save_controller import read_save_file, write_save_file
from config import attemps_save_file

def add_attemp():
    attemps = int(read_save_file(attemps_save_file))
    write_save_file(attemps_save_file, attemps + 1)

def get_attemps():
    return read_save_file(attemps_save_file)