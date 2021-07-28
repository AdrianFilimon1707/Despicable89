# from Students.Model.StudentModel import Student
from Students.Model.Student import Student
from Students.Repository import StudentRepository


class StudentController:
    def __init__(self, repo: StudentRepository):
        self.__repo = repo

    def add_student_c(self, sid, name, group):
        if str(sid).isnumeric() and int(sid) > 0 and str(name).isalpha() and int(group) > 0:
            student = Student(int(sid), name, int(group))
            self.__repo.add_students(student)
            print("added student")
        else:
            print("student not added")

    def print_all_students_c(self):
        students = self.__repo.get_all_students()
        if len(students) > 0:
            for student in students:
                print(student)

    def filter_all_students_c(self, group):
        if str(group).isnumeric() and int(group) > 0:
            filtered_students = self.__repo.filter_students_by_group(int(group))
            if len(filtered_students) > 0:
                for student in filtered_students:
                    print(student)
            else:
                print("No such student")
        else:
            print("Not a valid group nr")

    def check_if_student_exist_c(self, sid):
        if str(sid).isnumeric() and int(sid) > 0:
            existing_student = self.__repo.check_if_student_exist(int(sid))
            return existing_student
        else:
            print("Not a good ID")
        return None

    def undo_c(self):
        undo_done = self.__repo.undo()
        if undo_done:
            print("Success")
        else:
            print("Not available")