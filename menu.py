from Actions.borrow_report import generate_return_report
from Actions.student_actions import add_student_menu, search_student_by_first_name_menu, search_student_by_last_name_menu, \
    show_students
from Actions.book_actions import search_book_by_title_menu, search_book_by_author_menu, show_books, add_book, remove_book, \
    borrow_book, return_book


def show_menu(library):

    while True:
        print("\n=== MENU BIBLIOTEKI ===")
        print("1. Menu zarządzania studentami")
        print("2. Menu zarzadzania książkami")
        print("3. Wypożycz książke")
        print("4. Zwróć książke")
        print("5. Generuj raport zwrotu")
        print("0. Wyjdź")

        choice = input("Wybierz opcję: \n").strip()

        match choice:

            case "1":
                show_student_menu(library)

            case "2":
                show_book_menu(library)

            case "3":
                borrow_book(library)

            case "4":
                return_book(library)

            case "5":
                generate_return_report(library)

            case "0":
                print("Wyłaczono")
                break

            case _:
                print("Nie ma takiej opcji")

def show_student_menu(library):

    while True:

        print("\n=== MENU ZARZĄDZANIA STUDENTAMI ===")
        print("1. Dodaj studenta")
        print("2. Wyświetl liste wszystkich studentów")
        print("3. Wyszukaj studenta")
        print("0. Powrót do menu głównego")

        choice = input("Wybierz opcję: \n").strip()

        match choice:

            case "1":
                add_student_menu(library)

            case "2":
                if not library.students:
                    print("Error")
                else:
                    show_students(library)

            case "3":
                selected_student = find_students_menu(library)
                if selected_student:
                    student_menu(selected_student)

            case "0":
                break

            case _:
                print("Nie ma takiej opcji")


def show_book_menu(library):
    while True:
        print("\n=== MENU ZARZĄDZANIA KSIAŻKAMI ===")
        print("1. Wyświetl liste wszystkich książek")
        print("2. Wyszukaj książke")
        print("3. Dodaj tytuł do zasobów biblioteki")
        print("4. Usuń tytuł z zasobów biblioteki")
        print("0. Powrót do menu głównego")

        choice = input("Wybierz opcję: \n").strip()

        match choice:
            case "1":
                show_books(library)

            case "2":
                find_books_menu(library)

            case "3":
                add_book(library)

            case "4":
                remove_book(library)

            case "0":
                break

            case _:
                print("Nie ma takiej opcji")


def find_students_menu(library):
    print("1. Wyszukaj po imieniu ")
    print("2. Wyszukaj po nazwisku ")

    search = input("Wybierz opcję: ").strip()

    if search == "1":
        return search_student_by_first_name_menu(library)

    elif search == "2":
        return search_student_by_last_name_menu(library)

    else:
        print("Nie ma takiej opcji")
        return None

def find_books_menu(library):
    print("1. Wyszukaj książke po tytule  ")
    print("2. Wyszukaj ksiażki po imieniu i nazwisku autora ")

    search = input("Wybierz opcję: ").strip()

    if search == "1":
        search_book_by_title_menu(library)

    elif search == "2":
        search_book_by_author_menu(library)

def student_menu(student):
    while True:
        print(f"\n=== MENU STUDENTA: {student.first_name} {student.last_name} ===")
        print("1. Wyświetl wypożyczone książki")
        print("0. Powrót do menu zarządania studentami")

        choice = input("Wybierz opcję: ").strip()

        match choice:
            case "1":
                if student.borrowed_books:
                    print("Wypożyczone książki:")
                    for book in student.borrowed_books:
                        print(f"- {book.title} by {book.author_first_name} {book.author_last_name}")
                else:
                    print("Brak wypożyczonych książek.")
            case "0":
                break
            case _:
                print("Nie ma takiej opcji.")
