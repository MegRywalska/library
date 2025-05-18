from library import Library
from student_file import load_students_from_file
from fetch_books import get_books_from_api
from menu import *

def main():

    books = get_books_from_api("fantasy", 10)

    students = load_students_from_file()
    library = Library(books=books, students=students)

    # print("\nBook: ")
    # for book in library.books:
    #     print(f"{book.title} ({book.author}, {book.release_date}, {book.pages}, {book.total_copies}, {book.available_copies})")
    #
    # print("\nStudent: ")
    # for student in library.students:
    #     print(f"{student.id} {student.first_name} {student.last_name}")
    #

    show_menu(library)

if __name__ == "__main__":
    main()
