import json
from dataclasses import asdict
from datetime import datetime, date
from typing import List
from Actions.borrowedBookInfo import BorrowedBookInfo
from Model.student import Student

def load_students_from_file(json_file='sample_students.json'):
    students = []

    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                borrowes_books = []

                for book in item.get('borrowed_books', []):
                    borrowes_books.append(BorrowedBookInfo(
                        title = book['title'],
                        author = book['author'],
                        borrowed_date = datetime.strptime(book['borrowed_date'], '%Y-%m-%d').date()
                        ))

                students.append(Student(
                    id=item['id'],
                    first_name = item['first_name'],
                    last_name = item['last_name'],
                    borrowed_books = borrowes_books
                ))
    except FileNotFoundError:
        print("Plik nie istnieje. Zostanie utworzony nowy przy zapisie.")

    except json.JSONDecodeError:
        print("Błąd w formacie JSON.")

    return students


def save_students_to_file(students: List[Student], json_file='sample_students.json'):
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump([convert_student(student) for student in students], file, indent=4, ensure_ascii=False)


def get_next_student_id(students: List[Student]):
    if not students:
        return 1
    return max(student.id for student in students) + 1

def convert_student(student: Student):

    student_dict = asdict(student)

    for book in student_dict.get('borrowed_books', []):

        if isinstance(book.get("borrowed_date"), date):
            book["borrowed_date"] = book["borrowed_date"].isoformat()

    return student_dict

