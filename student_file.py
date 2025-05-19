import json
from dataclasses import asdict
from typing import List

from student import Student

def load_students_from_file(json_file='sample_students.json'):
    students = []

    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

            for item in data:
                students.append(Student(
                    id=item['id'],
                    first_name=item['first_name'],
                    last_name=item['last_name'],
                    borrowed_books=item.get('borrowed_books', [])
                ))
    except FileNotFoundError:
        print("Plik nie istnieje. Zostanie utworzony nowy przy zapisie.")

    except json.JSONDecodeError:
        print("Błąd w formacie JSON.")

    return students


def save_students_to_file(students: List[Student], json_file='sample_students.json'):
    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump([asdict(student) for student in students], file, indent=4, ensure_ascii=False)


def get_next_student_id(students: List[Student]):
    if not students:
        return 1
    return max(student.id for student in students) + 1