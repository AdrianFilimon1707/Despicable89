from Students.Controller.StudentController import StudentController
from Students.Menu.StudentsMenu import Menu
from Students.Repository.StudentRepository import Repository
from Students.utils.read_utils import read_input


def main():
    menu = Menu()
    repo = Repository()
    ctrl = StudentController(repo)
    option = -1
    while option != 0:
        menu.print_menu()
        option = read_input("OPTION: ")
        if str(option).isnumeric():
            option = int(option)
            if option == 1:
                sid = read_input("Add Student ID: ")
                student_existance = ctrl.check_if_student_exist_c(sid)
                if student_existance is not None and  student_existance == False:
                    name = read_input("Student name: ")
                    group = read_input("Student group: ")
                    ctrl.add_student_c(sid, name, group)
                elif student_existance:
                    print(" Already exist !")

            elif option == 2:
                ctrl.print_all_students_c()
            elif option == 3:
                group = read_input("Find your group: ")
                ctrl.filter_all_students_c(group)
            elif option == 4:
                ctrl.undo_c()
            elif option == 0:
                print("GOOD_BYE")
                break
            else:
                print("INVALID_OPTION")


if __name__ == '__main__':
    main()
