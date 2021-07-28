from College.data.constants import OPTION, STUDENT_ID, STUDENT_NAME
from College.exception.OptionExceptions.OptionValueException import OptionValueException
from College.validator.OptionValidator import OptionValidator

def read_option():
    try:
        option = input(OPTION)
        option_validator = OptionValidator(option)
        option_validator.verify_option()
        return int(option)
    except OptionValueException as exception:
        print(exception)
    return -1

def read_input(message=''):
    user_input = input('\t' + message)
    return user_input

def read_student_information():
    student_id = read_input(STUDENT_ID)
    name = read_input(STUDENT_NAME)
    return student_id, name
