from dataclasses import dataclass
from typing import List
from student import Student
from book import Book

@dataclass
class Library:

    books: List[Book]
    students: List[Student]

    def find_book_by_title(self, title: str):
        found_book = [book for book in self.books if title.lower() in book.title.lower()]
        return found_book

    def find_book_by_author(self, author: str):
        found_book = [book for book in self.books if author.lower() in book.author.lower()]
        return found_book

    def find_student_by_first_name(self, first_name: str):
        found_student = [student for student in self.students if first_name.lower() in student.first_name.lower()]
        return found_student

    def find_student_by_last_name(self, last_name: str):
        found_student = [student for student in self.students if last_name.lower() in student.last_name.lower()]
        return found_student


