from dataclasses import dataclass
from typing import Union


@dataclass
class Book:
    title: str
    author: str
    release_date: str
    pages: Union[int, str]
    total_copies: int
    available_copies: int
