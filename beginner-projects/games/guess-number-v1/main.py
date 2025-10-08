from modules.controllers.guess_controller import guess_number
from modules.number_generator import generate_random_number
from modules.controllers.check_files_controller import check_on_saves_exists
from modules.controllers.win_controller import get_win

def main():
    check_on_saves_exists()

    min_range = int(input("Enter min range: "))
    max_range = int(input("Enter max range: "))

    generate_random_number(min_range, max_range)

    while get_win != 1:
        try:
            number = int(input("Guess number: "))
            guess_number(number)
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()