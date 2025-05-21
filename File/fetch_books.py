import requests
from Model.book import Book

def get_books_from_api(query, limit):

    url = f"https://openlibrary.org/search.json?q={query}&limit={limit}"
    response = requests.get(url)

    books = []

    if response.status_code == 200:
        data = response.json()
        for item in data.get('docs', []):
            title = item.get('title', '')
            author = item.get('author_name', ['Unknown'])[0]
            year = str(item.get('first_publish_year', 'Unknown'))
            pages = item.get('number_of_pages_median')

            if pages is None:
                pages = "Unknown"

            total_copies = 5
            available_copies = total_copies

            book = Book(
                title=title,
                author=author,
                release_date=year,
                pages=pages,
                total_copies=total_copies,
                available_copies=available_copies
            )

            books.append(book)
    else:
        print("Download error")

    return books

