from Model.book import Book
from Actions.student_actions import choose_student_from_list
from File.student_file import save_students_to_file
from File.book_file import save_books_to_file
from datetime import date
from Actions.borrowedBookInfo import BorrowedBookInfo

def add_book(library):

    print("Dodaj ksiażke: ")
    title = input("Tytuł: ")
    author = input("Autor: ")
    release_date = input("Data wydania: ")
    pages = input("Liczba stron: ")
    total_copies = int(input("Liczba kopie: "))
    available_copies = total_copies

    new_book = Book(title, author, release_date, pages, total_copies, available_copies)
    library.books.append(new_book)

    print(f"\nDodano książke: ")
    print(f""
          f"Tytuł: {new_book.title} | "
          f"Autor: {new_book.author} | "
          f"\nRok wydania: {new_book.release_date} | "
          f"\nLiczba stron: {new_book.pages} | "
          f"\nIlosć wszystkich egzemplarzy: {new_book.total_copies} | "
          f"\nDostępne egzemplarze: {new_book.available_copies}"
          "\n --------------------------------------------------------"
          "\n"
          )

def remove_book(library):
    title = input("Podaj tytuł książki do usunięcia: ").strip()
    found_books = library.find_book_by_title(title)

    if found_books:
        print("Znalezione książki:")
        for index, book in enumerate(found_books, 1):
            print(f"{index}. Tytuł: {book.title} Autor: {book.author} ")

        choice = input("Podaj numer książki do usunięcia: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(found_books):
                book_to_remove = found_books[choice - 1]
                library.books.remove(book_to_remove)
                print(f"Usunięto książkę: Tytuł: {book_to_remove.title} Autor: {book_to_remove.author}")
            else:
                print("Nieprawidłowy wybór.")
        else:
            print("Anulowano usuwanie.")
    else:
        print("Nie znaleziono żadnych pasujących tytułów.")


def show_books(library):

    print("\n=== ZASOBY BIBLIOTEKI ===")
    for book in library.books:
        print(f""
              f"Tytuł: {book.title} | "
              f"Autor: {book.author} | "
              f"\nRok wydania: {book.release_date} | "
              f"\nLiczba stron: {book.pages} | "
              f"\nIlosć wszystkich egzemplarzy: {book.total_copies} | "
              f"\nDostępne egzemplarze: {book.available_copies}"
              "\n --------------------------------------------------------"
              "\n"
              )


def search_book_by_title_menu(library):

    title = input("Podaj tytuł książki: ").strip()
    found = library.find_book_by_title(title)

    if found:
        print("\nZnalezione książki w bibliotece: \n")

        for book in found:
            print(f""
                  f"Tytuł: {book.title} | "
                  f"Autor: {book.author} | "
                  f"\nRok wydania: {book.release_date} | "
                  f"\nLiczba stron: {book.pages} | "
                  f"\nIlosć wszystkich egzemplarzy: {book.total_copies} | "
                  f"\nDostępne egzemplarze: {book.available_copies}"
                  "\n --------------------------------------------------------"
                  "\n"
                  )


    else:
        print("\nNie znaleziono żadanych pasujacy tytułów.")



def search_book_by_author_menu(library):

    author = input("Podaj autora książki: ").strip()
    found = library.find_book_by_author(author)

    if found:
        print(f"\nZnalezione książki tego authora {author} w bibliotece: \n")

        for book in found:
            print(f""
                  f"Tytuł: {book.title} | "
                  f"Autor: {book.author} | "
                  f"\nRok wydania: {book.release_date} | "
                  f"\nLiczba stron: {book.pages} | "
                  f"\nIlosć wszystkich egzemplarzy: {book.total_copies} | "
                  f"\nDostępne egzemplarze: {book.available_copies}"
                  "\n --------------------------------------------------------"
                  "\n"
                  )

    else:
        print("\nNie znaleziono żadanych pasujacy książek.")


def choose_book_from_list_by_title(books):
    if not books:
        return None

    while True:
        try:
            title = input("Wpisz dokładny tytuł książki lub zero by się cofnać: ").strip()

            if title == "0":
                return None

            for book in books:
                if book.title.lower() == title.lower():
                    return book

        except ValueError:
            print("Nie znaleziono książki o takim tytule.")


def borrow_book(library):
    while True:
        name = input("Podaj nazwisko studenta: ").strip()
        found_students = library.find_student_by_last_name(name)

        if found_students:
            print("Znalezieni studenci:")
            for student in found_students:
                print(f"{student.id}: {student.first_name} {student.last_name}")

            selected_student = choose_student_from_list(found_students)
            if selected_student:
                break
        else:
            choice = input("Nie znaleziono studentów o takim nazwisku. Aby zakończyć wybierz zero: ")
            if choice == "0":
                return

    while True:
        title = input("Podaj tytuł książki: ").strip()
        found_books = library.find_book_by_title(title)

        if found_books:
            print("Znalezione książki:")
            for book in found_books:
                print(f""
                      f"Tytuł: {book.title} | "
                      f"Autor: {book.author} | "
                      f"\nRok wydania: {book.release_date} | "
                      f"\nDostępne egzemplarze: {book.available_copies}"
                      "\n --------------------------------------------------------"
                      "\n"
                      )

            selected_book = choose_book_from_list_by_title(found_books)
            if selected_book:
                break
        else:
            choice = input("Nie znaleziono żadnych pasujących tytułów. Aby zakończyć wybierz zero: ")
            if choice == "0":
                return

    if selected_book.available_copies <= 0:
        print("Brak dostępnych egzemplarzy tej książki.")
        return

    if len(selected_student.borrowed_books) >= 5:
        print("Student nie może wypożyczyć więcej niż 5 książek.")
        return

    for borrowed in selected_student.borrowed_books:
        if borrowed.title == selected_book.title and borrowed.author == selected_book.author:
            print("Student już wypożyczył tę książkę.")
            return

    borrowed_info = BorrowedBookInfo(
        title = selected_book.title,
        author = selected_book.author,
        borrowed_date = date.today()
    )
    selected_student.borrowed_books.append(borrowed_info)
    selected_book.available_copies -= 1

    print(f"Student {selected_student.first_name} {selected_student.last_name} wypożyczył książkę: {selected_book.title}")

    save_students_to_file(library.students)
    save_books_to_file(library.books)

def return_book(library):

    while True:
        name = input("Podaj nazwisko studenta: ").strip()
        found_students = library.find_student_by_last_name(name)

        if found_students:
            print("Znalezieni studenci:")
            for student in found_students:
                print(f"{student.id}: {student.first_name} {student.last_name}")

            selected_student = choose_student_from_list(found_students)
            if selected_student:
                break
        else:
            choice = input("Nie znaleziono studentów o takim nazwisku. Aby zakończyć wybierz zero: ")
            if choice == "0":
                return

    if not selected_student.borrowed_books:
        print("Ten student nie ma wypożyczonych książek.")
        return

    print("Wypożyczone książki:")
    for i, borrowed in enumerate(selected_student.borrowed_books, start = 1):
        print(f"{i}. {borrowed.title} ({borrowed.author}) - wypożyczono: {borrowed.borrowed_date}")

    while True:
        try:
            index = int(input("Wybierz numer książki do zwrotu: ")) - 1
            if 0 <= index < len(selected_student.borrowed_books):
                selected_borrowed = selected_student.borrowed_books[index]
                break
            else:
                print("Niepoprawny numer.")
        except ValueError:
            print("Wprowadź poprawny numer.")

    found_books = library.find_book_by_title(selected_borrowed.title)
    book_to_return = None
    for book in found_books:
        if book.author == selected_borrowed.author:
            book_to_return = book
            break

    if not book_to_return:
        print("Nie znaleziono książki w katalogu.")
        return

    if book_to_return.available_copies < book_to_return.total_copies:
        book_to_return.available_copies += 1

    selected_student.borrowed_books.remove(selected_borrowed)

    print(f"Książka '{selected_borrowed.title}' została zwrócona przez {selected_student.first_name} {selected_student.last_name}.")

    save_students_to_file(library.students)
    save_books_to_file(library.books)