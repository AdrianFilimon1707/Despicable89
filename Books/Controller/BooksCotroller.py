from Books.Model.BooksModel import BookModel
from Books.Repo.BooksRepository import BooksRepository


class BooksController:
    def __init__(self, repo: BooksRepository):
        self.__repo = repo

    def add_book_c(self, isbn, author, title):

        book = BookModel(isbn, author, title)
        self.__repo.add_book(book)
        print("Action done succesfully")

    def print_all_books_c(self):
        books = self.__repo.get_all_books()
        if len(books) > 0:
            for book in books:
                print(book)

    def filter_all_books_c(self, title):
        filtered_books = self.__repo.filtered_books_by_title(title)
        if len(filtered_books) > 0:
            for book in filtered_books:
                print(book)
        else:
            print("No such BOOK")

    def check_if_student_exist_c(self, isbn):
        return self.__repo.check_if_isbn_exist(isbn)

    def undo_c(self):
        undo_done = self.__repo.undo()
        if undo_done:
            print("Success")
        else:
            print("Not available")

    def redo_c(self):
        redo_done = self.__repo.redo()
        if redo_done:
            print("Success")
        else:
            print("Not available")
