from modules.controllers.SaveControllers.save_controller import read_save_file, write_save_file
from config import numbers_save_file

def write_number(random_number):
    write_save_file(numbers_save_file, random_number)

def get_write_number():
    return int(read_save_file(numbers_save_file))