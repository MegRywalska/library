from Model.student import Student
from File.student_file import save_students_to_file, get_next_student_id

def add_student_menu(library):

    print("\nDodaj nowego studenta: ")
    new_id = get_next_student_id(library.students)
    first_name = input("Imię: ").strip()
    last_name = input("Nazwisko: ").strip()
    borrowed_book = []

    new_student = Student(id=new_id, first_name=first_name, last_name=last_name, borrowed_books=borrowed_book)
    library.students.append(new_student)

    save_students_to_file(library.students)

    print(f"Dodano studenta: {new_student.first_name} {new_student.last_name} (ID: {new_student.id})")

def show_students(library):
    for student in library.students:
        print(f"Student ID: {student.id}: {student.first_name} {student.last_name}")
        print("Wypożyczone książki:\n")

        if student.borrowed_books:
            for book in student.borrowed_books:
                print(f"""Tytuł: {book.title} | Autor: {book.author}
                Data wypożyczenia: {book.borrowed_date}""")
                print("--------------------------------------------------------")
        else:
            print("Brak wypożyczonych książek.")
            print("--------------------------------------------------------")



def search_student_by_first_name_menu(library):
    name = input("Podaj imię studenta: ").strip()
    found = library.find_student_by_first_name(name)

    if found:
        print("\nZnalezieni studenci:\n")

        for student in found:
            print(f"Student ID: {student.id}: {student.first_name} {student.last_name}")
            print("Wypożyczone książki:\n")

            if student.borrowed_books:
                for book in student.borrowed_books:
                    print(f"""Tytuł: {book.title} | Autor: {book.author}
                    Data wypożyczenia: {book.borrowed_date}
--------------------------------------------------------""")
            else:
                print("Brak wypożyczonych książek.")
                print("--------------------------------------------------------\n")

    else:
        print("Nie znaleziono studentów o takim imieniu.")


def search_student_by_last_name_menu(library):
    name = input("Podaj nazwisko studenta: ").strip()
    found = library.find_student_by_last_name(name)

    if found:
        print("\nZnalezieni studenci:\n")

        for student in found:
            print(f"Student ID: {student.id}: {student.first_name} {student.last_name}")
            print("Wypożyczone książki:\n")

            if student.borrowed_books:
                for book in student.borrowed_books:
                    print(f"""Tytuł: {book.title} | Autor: {book.author}
                    Data wypożyczenia: {book.borrowed_date}
--------------------------------------------------------""")
            else:
                print("Brak wypożyczonych książek.")
                print("--------------------------------------------------------\n")

    else:
        print("Nie znaleziono studentów o takim nazwisku.")



def choose_student_from_list(students):
    if not students:
        return None

    while True:
        try:
            choice = int(input("Wpisz ID by wybrać studenta: "))
            for student in students:
                if student.id == choice:
                    return student

            print("Nie ma studenta o takim ID.")

        except ValueError:
            print("Nie ma studenta o takim ID.")


