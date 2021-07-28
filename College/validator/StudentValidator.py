from College.exception.StudentExceptions.StudentNameException import StudentNameException
from College.exception.StudentExceptions.StudentIdException import StudentIdException

class StudentValidator:
    def __init__(self, student_id=None, student_name=None):
        self.__student_id = student_id
        self.__student_name = student_name

    def verify_student_data(self):
        self.verify_id()
        self.verify_name()

    def verify_id(self):
        if self.__student_id is not None and (not str(self.__student_id).isnumeric() or int(self.__student_id) <= 0):
            raise StudentIdException('\tInvalid student id !')

    def verify_name(self):
        if self.__student_name is not None and not self.__student_name.isalpha():
            raise StudentNameException('\tInvalid student name !')
