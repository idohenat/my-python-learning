from modules.calculator_module import *

def main():
    try:
        first_number = float(input("Enter first number: "))
        second_number = float(input("Enter second number: "))
        
        show_operators()

        operator = int(input("Select operator(Enter operator index!): "))
        answer = calculate(first_number, second_number, operator)
        
        print(f"Your answer: {answer}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()