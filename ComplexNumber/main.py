from ComplexNumber.controller.ComplexNumberController import ComplexNumberController
from ComplexNumber.data.constants import INVALID_OPTION, GOOD_BYE, REAL_NUMBER, IMAGINARY_NUMBER, OPTION, START, END
from ComplexNumber.menu.Menu import Menu
from ComplexNumber.repository.ComplexNumberRepository import ComplexNumberRepository
from ComplexNumber.utils.read_utils import read_input


def main():
    menu = Menu()
    repo = ComplexNumberRepository()
    ctrl = ComplexNumberController(repo)
    option = -1
    while option != 0:
        menu.print_menu()
        option = read_input(OPTION)
        if str(option).isnumeric():
            option = int(option)
            if option == 1:
                a = read_input(REAL_NUMBER)
                b = read_input(IMAGINARY_NUMBER)
                ctrl.add_complex_number_c(a, b)
            elif option == 2:
                ctrl.print_all_complex_numbers()
            elif option == 3:
                start = read_input(START)
                end = read_input(END)
                ctrl.print_filtered_list_by_bounds(start, end)
            elif option == 4:
                ctrl.undo_c()
            elif option == 0:
                print(GOOD_BYE)
                break
            else:
                print(INVALID_OPTION)


if __name__ == '__main__':
    main()
