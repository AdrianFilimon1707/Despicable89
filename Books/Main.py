# Manage a list of books. Each book has an isbn (string, unique), an author and a title (strings). Provide the
# user the following features:
# 1. Add a new book to the list. Book data is read from the console.
# 2. Show the list of books on the console.
# 3. Filter the list so that book titles starting with a given word are deleted from the list.
# 4. Undo the last operation that modified program data. This step can be repeated.
from Books.Controller.BooksCotroller import BooksController
from Books.Menu.BooksMenu import BooksMenu
from Books.Repo.BooksRepository import BooksRepository
from Books.Utility.read_utils import read_input


def main():
    menu = BooksMenu()
    repo = BooksRepository()
    controller = BooksController(repo)

    option = -1
    while option != 0:
        menu.print_menu()
        option = read_input("OPTION: ")
        if str(option).isnumeric():
            option = int(option)
            if option == 1:
                isbn = read_input("isbn = ")
                author = read_input("author = ")
                title = read_input("title = ")
                controller.add_book_c(isbn, author, title)
            elif option == 2:
                controller.print_all_books_c()
            elif option == 3:
                title = read_input("title = ")
                controller.filter_all_books_c(title)
            elif option == 4:
                controller.undo_c()
            elif option == 5:
                controller.redo_c()
            elif option == 0:
                print("GOOD_BYE")
                break
            else:
                print("INVALID_OPTION")


if __name__ == '__main__':
    main()
