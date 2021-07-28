from Books.Model.BooksModel import BookModel


class BooksRepository:
    def __init__(self):
        self.__books = []
        self.__undo = []
        self.__redo = []

    def add_book(self, book: BookModel):
        self.__undo.append(self.__books.copy())
        self.__books.append(book)

    def get_all_books(self):
        return self.__books

    def filtered_books_by_title(self, title):
        filtered_list = []
        book : BookModel
        for book in self.__books:
            if not book.get_title().startswith(title):
                filtered_list.append(book)

        return filtered_list

    def check_if_isbn_exist(self, isbn):
        for book in self.__books:
            if book.get_insb() == isbn:
                return True
        return False

    def undo(self):
        if len(self.__undo) > 0:
            self.__redo.append(self.__books.copy())
            first_undo = self.__undo.pop()
            self.__books = first_undo.copy()
            return True

        else:
            return False

    def redo(self):
        if len(self.__redo) > 0:
            first_redo = self.__redo.pop()
            self.__undo.append(self.__books.copy())
            self.__books = first_redo.copy()
            return True

        else:
            return False