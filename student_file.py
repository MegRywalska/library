from student import Student

def load_students_from_file():

    students = []

    try:
        with open('sample_students.txt', encoding='utf-8') as file:

            for line in file:
                parts = line.strip().split(';')

                if len(parts) == 3:

                    student_id = int(parts[0])
                    first_name = parts[1]
                    last_name = parts[2]

                    students.append(Student(student_id, first_name, last_name))

    except FileNotFoundError:
        print('File not found')

    return students


def save_students_to_file(student: Student):
    with open('sample_students.txt', 'a', encoding='utf-8') as file:
        file.write(f"{student.id};{student.first_name};{student.last_name}\n")


def get_next_student_id(students):
    if not students:
        return 1
    return max(student.id for student in students) + 1