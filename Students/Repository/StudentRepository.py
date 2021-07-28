from Students.Model.Student import Student


class Repository:
    def __init__(self):
        self.__students = []
        self.__undo = []

    def add_students(self, student: Student):
        self.__undo.append(self.__students.copy())
        self.__students.append(student)

    def get_all_students(self):
        return self.__students

    def filter_students_by_group(self, group: int):
        filtered_list = []
        student: Student
        for student in self.__students:
            if student.get_group() != group:
                filtered_list.append(student)

        return filtered_list

    def check_if_student_exist(self, sid: int):
        for student in self.__students:
            if student.get_sid() == sid:
                return True
        return False

    def undo(self):
        if len(self.__undo) > 0:
            first_undo = self.__undo.pop()
            self.__students = first_undo.copy()
            return True

        else:
            return False


