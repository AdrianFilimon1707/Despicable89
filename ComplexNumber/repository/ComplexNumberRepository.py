from ComplexNumber.model.ComplexNumber import ComplexNumber


class ComplexNumberRepository:
    def __init__(self):
        self.__repository = []
        self.__prev_repo = None

    def add_complex_number(self, complex_number: ComplexNumber):
        self.__prev_repo = self.__repository.copy()
        self.__repository.append(complex_number)

    def get_all_complex_numbers(self):
        return self.__repository

    def filter_by_bounds(self, start: int, end: int):
        filtered_list = []
        complex_number: ComplexNumber
        for complex_number in self.__repository:
            a = complex_number.get_real_number()
            if (a > start) and (a < end):
                filtered_list.append(complex_number)
        return filtered_list

    def undo(self):
        if self.__prev_repo is not None:
            self.__repository = self.__prev_repo.copy()
            self.__prev_repo = None
            return True
        else:
            return False

