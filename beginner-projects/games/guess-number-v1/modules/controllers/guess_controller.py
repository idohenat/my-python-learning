from modules.controllers.number_controller import get_write_number
from modules.controllers.attemps_controller import get_attemps, add_attemp
from modules.controllers.win_controller import set_win

def guess_number(number):
    secret_number = get_write_number()
    add_attemp()

    if number > secret_number:
        print(f"Less! Attemp: {get_attemps()}")
    elif number < secret_number:
        print(f"More! Attemp: {get_attemps()}")
    else:
        print(f"Yooo!! You win! Total attemps: {get_attemps()}")
        set_win()