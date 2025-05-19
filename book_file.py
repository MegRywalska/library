import json
from book import Book
from typing import List

def save_books_to_file(books: List[Book], file_name = "books.json"):
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump([book.__dict__ for book in books], file, ensure_ascii=False, indent=4)

def load_books_from_file(file_name = "books.json") -> List[Book]:
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Book(**book_dict) for book_dict in data]

    except FileNotFoundError:
        print("Plik nie istnieje. Zostanie utworzony nowy przy zapisie.")
        return []

    except json.JSONDecodeError:
        print("Błąd w formacie JSON.")
        return []