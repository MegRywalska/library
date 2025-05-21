from Model.library import Library
from File.student_file import load_students_from_file
from File.fetch_books import get_books_from_api
from menu import *
from File.book_file import save_books_to_file,load_books_from_file

def main():

    books = load_books_from_file()

    if not books:
        genres = ["fantasy", "history", "science-fiction", "romance", "horror"]
        for genre in genres:
            books += get_books_from_api(genre, 10)
        save_books_to_file(books)

    students = load_students_from_file()
    library = Library(books=books, students=students)

    generate_return_report(library)
    show_menu(library)
    save_books_to_file(library.books)

if __name__ == "__main__":
    main()
