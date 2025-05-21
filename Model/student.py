from dataclasses import dataclass, field
from typing import List
from Actions.borrowedBookInfo import BorrowedBookInfo


@dataclass
class Student:

    id: int
    first_name: str
    last_name: str
    borrowed_books: List[BorrowedBookInfo] = field(default_factory=list)
