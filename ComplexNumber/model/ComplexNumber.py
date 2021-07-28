# Complex number : a + bi
class ComplexNumber:
    def __init__(self, a: int, b: int):
        self.__real = a
        self.__imaginary = b

    def get_real_number(self):
        return self.__real

    def get_imaginary_number(self):
        return self.__imaginary

    def set_real_number(self, new_a):
        self.__real = new_a

    def set_imaginary_number(self, new_b):
        self.__imaginary = new_b

    def __str__(self):
        return str(self.__real) + " + " + str(self.__imaginary) + "i"
