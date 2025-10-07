from modules.calculate_manager import calculate, print_error

def show_formuls():
    formuls = ["rectangle", "square", "square_diagonally"]

    for index, formula in enumerate(formuls):
        print(f"{index + 1}. {formula}")

def main():
    while True:
        try:
            show_formuls()
        
            selected_formula = int(input("Select formula: "))
        
            calculate(selected_formula)
        except ValueError as e:
            print_error(e)

if __name__ == "__main__":
    main()