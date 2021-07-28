from College.data.constants import NO_REGISTERED_STUDENTS, STUDENT_ID_ALREADY_EXISTS, STUDENT_DOES_NOT_EXIST, \
    SUCCESS_ADD, SUCCESS_DELETE, SUCCESS_UPDATE
from College.model.Student import Student
from College.validator.StudentValidator import StudentValidator
from College.exception.StudentExceptions.StudentIdException import StudentIdException
from College.exception.StudentExceptions.StudentNameException import StudentNameException

class StudentController:
    def __init__(self):
        self.__students = []

    def add_student(self, student_id, student_name):
        try:
            student_validator = StudentValidator(student_id, student_name)
            student_validator.verify_student_data()
            if not self.student_exists(int(student_id)):
                student = Student(int(student_id), student_name)
                self.__students.append(student)
                print(SUCCESS_ADD)
            else:
                print(STUDENT_ID_ALREADY_EXISTS)
        except StudentIdException as id_exception:
            print(str(id_exception))
        except StudentNameException as name_exception:
            print(str(name_exception))

    def delete_student(self, student_id):
        try:
            student_validator = StudentValidator(student_id, None)
            student_validator.verify_id()
            if self.student_exists(int(student_id)):
                student = self.get_student_by_id(int(student_id))
                self.__students.remove(student)
                print(SUCCESS_DELETE)
            else:
                print(STUDENT_DOES_NOT_EXIST)
        except StudentIdException as id_exception:
            print(str(id_exception))

    def update_student(self, student_id, student_new_name):
        try:
            student_validator = StudentValidator(student_id, student_new_name)
            student_validator.verify_student_data()
            if self.student_exists(int(student_id)):
                new_student = Student(int(student_id), student_new_name)
                student_list_position = self.get_student_position(student_id)
                current_student = self.__students[student_list_position]
                self.__students.remove(current_student)
                self.__students.insert(student_list_position, new_student)
                print(SUCCESS_UPDATE)
            else:
                print(STUDENT_DOES_NOT_EXIST)
        except StudentIdException as id_exception:
            print(str(id_exception))
        except StudentNameException as name_exception:
            print(str(name_exception))

    def print_student_details_by_id(self, student_id):
        try:
            student_validator = StudentValidator(student_id, None)
            student_validator.verify_id()
            if self.student_exists(int(student_id)):
                student = self.get_student_by_id(int(student_id))
                print('\t' + student)
            else:
                print(STUDENT_DOES_NOT_EXIST)
        except StudentIdException as id_exception:
            print(str(id_exception))

    def print_students(self):
        if self.are_students_registered():
            print()
            for student in self.__students:
                print('\t', student)
            print()
        else:
            print(NO_REGISTERED_STUDENTS)

    def are_students_registered(self):
        return len(self.__students) > 0

    def student_exists(self, student_id):
        for student in self.__students:
            if student.get_student_id() == student_id:
                return True
        return False

    def get_student_by_id(self, student_id):
        for student in self.__students:
            if student.get_student_id() == student_id:
                return student
        return None

    def get_student_position(self, student_id):
        pos = 0
        for student in self.__students:
            if student.get_student_id() == student_id:
                return pos
            pos += 1
        return -1
