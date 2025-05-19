from dataclasses import dataclass, field
from book import Book
from typing import List

@dataclass
class Student():

    id: int
    first_name: str
    last_name: str
    borrowed_books: List[str] = field(default_factory=list)
