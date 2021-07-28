from ComplexNumber.data.constants import INVALID_NUMBERS, NO_COMPLEX_NUMBERS, UNDO_SUCCESS, NO_UNDO_AVAILABLE
from ComplexNumber.model.ComplexNumber import ComplexNumber
from ComplexNumber.repository.ComplexNumberRepository import ComplexNumberRepository


class ComplexNumberController:
    def __init__(self, repository: ComplexNumberRepository):
        self.__repo = repository
        self.__prev_repo = None

    def add_complex_number_c(self, a, b):
        if str(a).isnumeric() and str(b).isnumeric():
            complex_number = ComplexNumber(int(a), int(b))
            self.__repo.add_complex_number(complex_number)
        else:
            print(INVALID_NUMBERS)

    def print_all_complex_numbers(self):
        complex_numbers = self.__repo.get_all_complex_numbers()
        self.print_complex_number_list(complex_numbers)

    def print_filtered_list_by_bounds(self, start, end):
        if str(start).isnumeric() and str(end).isnumeric():
            filtered_list = self.__repo.filter_by_bounds(int(start), int(end))
            self.print_complex_number_list(filtered_list)
        else:
            print(INVALID_NUMBERS)

    def print_complex_number_list(self, list):
        if len(list) == 0:
            print(NO_COMPLEX_NUMBERS)
        else:
            for complex_number in list:
                print(str(complex_number))

    def undo_c(self):
        was_done = self.__repo.undo()
        if was_done:
            print(UNDO_SUCCESS)
        else:
            print(NO_UNDO_AVAILABLE)
