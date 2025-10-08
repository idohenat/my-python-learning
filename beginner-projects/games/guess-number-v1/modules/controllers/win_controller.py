from modules.controllers.SaveControllers.save_controller import write_save_file, read_save_file
from config import win_state_file

def set_win():
    write_save_file(win_state_file, 1)

def get_win():
    return read_save_file(win_state_file)