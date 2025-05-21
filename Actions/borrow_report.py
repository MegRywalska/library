from datetime import date


def generate_return_report(library):

    today = date.today()
    print("\n PRZYPOMNIENIE O TERMINACH ZWROTU KSIAŻEK")

    reminder_found = False

    for student in library.students:
        for borrowed_book in student.borrowed_books:
            days_passed = (today - borrowed_book.borrowed_date ).days
            days_remaining = 30 - days_passed

            if 0 < days_remaining <= 7 or days_remaining == 0:
                reminder_found = True
                print(f"{student.id}, {student.first_name} {student.last_name}: ")
                print(f"Książka: {borrowed_book.title} - {borrowed_book.author}")
                print(f"Pozostało dni do oddania: {days_remaining if days_remaining >= 0 else 0}")

    if not reminder_found:
        print("W najbliższym czasie na ma żadnego terminu zwrotu")


    return
