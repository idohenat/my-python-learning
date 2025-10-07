from modules.rectangle_calculator import *
from modules.square_calculator import *

def print_error(error):
    print(f"Error: {error}")

def calculate(selected_formula):
    match selected_formula:
        case 1:
            calculate_rectangle()
        case 2:
            calculate_square()
        case 3:
            calculate_square_area()
        case _:
            raise ValueError(f"Invalid operator: {selected_formula}")

def calculate_rectangle():
    try:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))

        print(calculate_rectangle_area(length, width))
    except ValueError as e:
        print_error(e)

def calculate_square():
    try:
        side_length = float(input("Enter side length: "))

        print(calculate_square_area(side_length))
    except ValueError as e:
        print_error(e)

def calculate_square_diagonally():
    try:
        side_length = float(input("Enter side length: "))

        print(calculate_square_diagonally_area(side_length))
    except ValueError as e:
        print_error(e)