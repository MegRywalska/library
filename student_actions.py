from student import Student
from student_file import save_students_to_file, get_next_student_id

def add_student_menu(library):

    print("\nDodaj nowego studenta: ")
    new_id = get_next_student_id(library.students)
    first_name = input("Imię: ").strip()
    last_name = input("Nazwisko: ").strip()
    borrowed_book = []

    new_student = Student(id=new_id, first_name=first_name, last_name=last_name, borrowed_books=borrowed_book)
    library.students.append(new_student)

    save_students_to_file(new_student)

    print(f"Dodano studenta: {new_student.first_name} {new_student.last_name} (ID: {new_student.id})")

def show_students(library):

    for student in library.students:
        print(f"Student ID: {student.id}: {student.first_name} {student.last_name}")

def search_student_by_first_name_menu(library):

    name = input("Podaj imię studenta: ").strip()
    found = library.find_student_by_first_name(name)

    if found:
        print("Znalezieni studenci: ")

        for student in found:
            print(f"{student.id}: {student.first_name} {student.last_name}")
    else:
        print("Nie znaleziono studentów o takim imieniu")

def search_student_by_last_name_menu(library):
    name = input("Podaj nazwisko studenta: ").strip()
    found = library.find_student_by_last_name(name)

    if found:
        print("Znalezieni studenci: ")

        for student in found:
            print(f"{student.id}: {student.first_name} {student.last_name}")
    else:
        print("Nie znaleziono studentów o takim nazwisku")