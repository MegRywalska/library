from dataclasses import dataclass
from datetime import date

@dataclass
class BorrowedBookInfo:
    title: str
    author: str
    borrowed_date: date