import random

from modules.controllers.number_controller import write_number

def generate_random_number(min, max):
    write_number(random.randint(min, max))