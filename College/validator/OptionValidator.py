from College.data.constants import GENERAL_ERROR_MESSAGE
from College.exception.OptionExceptions.OptionValueException import OptionValueException


class OptionValidator:
    def __init__(self, option):
        self.__option = option

    def verify_option(self):
        if str(self.__option).isnumeric() or int(self.__option) < 0:
            raise OptionValueException(GENERAL_ERROR_MESSAGE)
