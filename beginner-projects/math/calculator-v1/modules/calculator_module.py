from modules.operations_module import *

def show_operators():
    operators = ["+", "-", "*", "/"]

    for index, operator in enumerate(operators):
        print(f"{index + 1}. {operator}")

def calculate(a, b, operator):
    match operator:
        case 1:
            return sum(a, b)
        case 2:
            return subtract(a, b)
        case 3:
            return muliply(a, b)
        case 4: 
            return divide(a, b)
        case _:
            raise ValueError(f"Unknow operator: {operator}")