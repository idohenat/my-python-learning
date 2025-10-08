from config import attemps_save_file, numbers_save_file, win_state_file
from modules.controllers.SaveControllers.save_controller import write_save_file

def write_defaults(default_number=0):
    write_save_file(attemps_save_file, default_number)
    write_save_file(numbers_save_file, default_number)
    write_save_file(win_state_file, default_number)