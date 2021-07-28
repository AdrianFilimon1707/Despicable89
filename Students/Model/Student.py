# class Student:
#     def __int__(self, sid: int, name: str, group: int):
#         self.__id = sid
#         self.__name = name
#         self.__group = group
#
#     def get_sid(self):
#         return self.__id
#
#     def get_name(self):
#         return self.__name
#
#     def get_group(self):
#         return self.__group
#
#     def __str__(self):
#         return "student(sid = " + str.(self.__id) + " , name = " + self.__name  + " group = " + str(self.__group) + ")"

class Student:
    def __init__(self, sid: int, name: str, group: int):
        self.__id = sid
        self.__name = name
        self.__group = group

    def get_sid(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def __str__(self):
        return "Student(id = " + str(self.__id) + ", name = " + self.__name + ", group = " + str(self.__group) + ")"
