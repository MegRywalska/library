from book import Book

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