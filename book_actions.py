from book import Book
from student_actions import choose_student_from_list
from student_file import save_students_to_file
from book_file import save_books_to_file

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

    print(f"Dodano książke: {new_book.title} {new_book.author} {new_book.release_date} {new_book.pages} {new_book.total_copies}")

def remove_book(library):
    title = input("Podaj tytuł książki do usunięcia: ").strip()
    found_books = library.find_book_by_title(title)

    if found_books:
        print("Znalezione książki:")
        for index, book in enumerate(found_books, 1):
            print(f"{index}. {book.title} {book.author}")

        choice = input("Podaj numer książki do usunięcia: ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(found_books):
                book_to_remove = found_books[choice - 1]
                library.books.remove(book_to_remove)
                print(f"Usunięto książkę: {book_to_remove.title} {book_to_remove.author}")
            else:
                print("Nieprawidłowy wybór.")
        else:
            print("Anulowano usuwanie.")
    else:
        print("Nie znaleziono żadnych pasujących tytułów.")


def show_books(library):

    for book in library.books:
        print(f"{book.title} ({book.author}, {book.release_date}, {book.pages}, {book.total_copies}, {book.available_copies})")

def search_book_by_title_menu(library):

    title = input("Podaj tytuł książki: ").strip()
    found = library.find_book_by_title(title)

    if found:
        print("Znalezione książki w bibliotece: ")

        for book in found:
            print(f"{book.title} ({book.author}, {book.release_date}, {book.pages}, {book.total_copies}, {book.available_copies})")


    else:
        print("Nie znaleziono żadanych pasujacy tytułów.")



def search_book_by_author_menu(library):

    author = input("Podaj autora książki: ").strip()
    found = library.find_book_by_author(author)

    if found:
        print(f"Znalezione książki tego authora {author} w bibliotece: ")

        for book in found:
            print(
                f"{book.title} ({book.author}, {book.release_date}, {book.pages}, {book.total_copies}, {book.available_copies})")

    else:
        print("Nie znaleziono żadanych pasujacy książek.")


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
            choice = input("Nie znaleziono studentów o takim nazwisku. Aby zakonczyć wybierz zero.")
            if choice == "0":
                return

    while True:
        title = input("Podaj tytuł książki: ").strip()
        found_books = library.find_book_by_title(title)

        if found_books:
            print("Znalezione książki:")
            for book in found_books:
                print(f"{book.title} ({book.author}, {book.release_date}, {book.pages}, {book.total_copies}, {book.available_copies})")

            selected_book = choose_book_from_list_by_title(found_books)
            if selected_book:
                break
        else:

            choice = input("Nie znaleziono żadnych pasujących tytułów. Aby zakonczyć wybierz zero.")
            if choice == "0":
                return

    if selected_book.available_copies <= 0:
        print("Brak dostępnych egzemplarzy tej książki.")
        return

    if len(selected_student.borrowed_books) >= 5:
        print("Student nie może wypożyczyć więcej niż 5 książek.")
        return

    if selected_book.title in selected_student.borrowed_books:
        print("Student już wypożyczył tę książkę.")
        return

    selected_book.available_copies -= 1
    selected_student.borrowed_books.append(selected_book.title)

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
            choice =  input("Nie znaleziono studentów o takim nazwisku. Aby zakonczyć wybierz zero.")
            if choice == "0":
                return


    if not selected_student.borrowed_books:
        print("Ten student nie ma wypożyczonych książek.")
        return

    print("Wypożyczone książki:")
    for i, title in enumerate(selected_student.borrowed_books, start=1):
        print(f"{i}. {title}")

    while True:
        try:
            index = int(input("Wybierz numer książki do zwrotu: ")) - 1
            if 0 <= index < len(selected_student.borrowed_books):
                selected_book_title = selected_student.borrowed_books[index]
                break
            else:
                print("Niepoprawny numer.")
        except ValueError:
            print("Wprowadź poprawny numer.")


    found_books = library.find_book_by_title(selected_book_title)
    if not found_books:
        print("Nie znaleziono książki w katalogu.")
        return

    book_to_return = found_books[0]

    if book_to_return.available_copies < book_to_return.total_copies:
        book_to_return.available_copies += 1

    selected_student.borrowed_books.remove(selected_book_title)

    print(f"Książka '{selected_book_title}' została zwrócona przez {selected_student.first_name} {selected_student.last_name}.")


    save_students_to_file(library.students)
    save_books_to_file(library.books)