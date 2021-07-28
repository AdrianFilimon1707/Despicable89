class Student:
    def __init__(self, sid: int, name: str):
        self.__sid = sid
        self.__name = name

    def get_student_id(self):
        return self.__sid

    def get_student_name(self):
        return self.__name

    def set_student_id(self, new_sid):
        self.__sid = new_sid

    def setStudentName(self, new_name):
        self.__name = new_name

    def __str__(self):
        return "Student(sid = " + str(self.__sid) + ", name = " + self.__name + ")"
