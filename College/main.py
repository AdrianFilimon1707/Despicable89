from College.controller.StudentController import StudentController
from College.data.constants import INVALID_OPTION, GOOD_BYE, STUDENT_ID, NEW_STUDENT_NAME
from College.menu.Menu import Menu
from College.utils.read_utils import read_option, read_student_information, read_input


def main():
    menu = Menu()
    student_controller = StudentController()
    option = -1
    while option != 0:
        menu.print_menu()
        option = read_option()
        if option == 1:
            student_id, student_name = read_student_information()
            student_controller.add_student(student_id, student_name)
        elif option == 2:
            student_controller.print_students()
        elif option == 3:
            student_id = read_input(STUDENT_ID)
            student_controller.delete_student(student_id)
        elif option == 4:
            student_id = read_input(STUDENT_ID)
            student_name = read_input(NEW_STUDENT_NAME)
            student_controller.update_student(student_id, student_name)
        elif option == 5:
            student_id = read_input(STUDENT_ID)
            student_controller.print_student_details_by_id(student_id)
        elif option == 0:
            print(GOOD_BYE)
            break
        else:
            print(INVALID_OPTION)


if __name__ == '__main__':
    main()
