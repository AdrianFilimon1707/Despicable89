class BookModel:
    def __init__(self, isbn: str, author: str, title: str):
        self.__isbn = isbn
        self.__author = author
        self.__title = title

    def get_isbn(self):
        return self.__isbn

    def get_author(self):
        return self.__author

    def get_title(self):
        return self.__title

    def __str__(self):
        return "Book (isbn = " + self.__isbn + ", Author = " + self.__author + ", Title = " + self.__title + ")"
