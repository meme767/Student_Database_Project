import sqlite3


def create_tables():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute('''CREATE TABLE IF NOT EXISTS students
     (id integer PRIMARY KEY, firstname text not null,
    lastname text not null, age integer not null,
    grade text not null, reg_date text not null)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS lessons(id integer PRIMARY KEY autoincrement,
    title text not null unique)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS student_lessons(student_id integer, lesson_id integer,
    primary key (student_id, lesson_id), foreign key(student_id) references students(id) on delete cascade,
    foreign key(lesson_id) references lessons(id) on delete cascade)''')

    conn.commit()
    conn.close()


def delete_student():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    print("\n- Delete Student -")
    student_id = input("Enter student ID to delete: ").strip()

    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if student:
        cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
        conn.commit()
        print(f"Student with ID {student_id} deleted successfully!")
    else:
        print("Sorry, no student found with this ID.")

    conn.close()


def show_student():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    print("\n- Display Student Info -")
    student_id = input("Enter student ID to display: ").strip()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if student:
        cursor.execute('''
            SELECT lessons.title 
            FROM lessons 
            JOIN student_lessons ON lessons.id = student_lessons.lesson_id 
            WHERE student_lessons.student_id = ?
        ''', (student_id,))
        lessons = cursor.fetchall()

        lessons_list = ", ".join([lesson[0] for lesson in lessons]) if lessons else "No enrolled lessons"

        print("\n- Student Info -")
        print(f"ID: {student[0]}")
        print(f"Full Name: {student[1]} {student[2]}")
        print(f"Age: {student[3]}")
        print(f"Grade: {student[4]}")
        print(f"Registration Date: {student[5]}")
        print(f"Enrolled Lessons: {lessons_list}")
    else:
        print("Sorry, no student found with this ID.")

    conn.close()


def add_student():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    print("\n- Add New Student -")
    firstname = input("Enter first name: ").strip()
    lastname = input("Enter last name: ").strip()
    age = int(input("Enter age: "))
    grade = input("Enter grade: ").strip()
    reg_date = input("Enter registration date (YYYY-MM-DD): ").strip()

    cursor.execute('''
        INSERT INTO students (firstname, lastname, age, grade, reg_date)
        VALUES (?, ?, ?, ?, ?)
    ''', (firstname, lastname, age, grade, reg_date))

    student_id = cursor.lastrowid

    lessons_input = input("Enter lessons separated by commas (e.g., Math, Physics): ").strip()

    if lessons_input:
        lessons_list = [l.strip() for l in lessons_input.split(",") if l.strip()]

        for lesson_name in lessons_list:
            cursor.execute("INSERT OR IGNORE INTO lessons (title) VALUES (?)", (lesson_name,))
            cursor.execute("SELECT id FROM lessons WHERE title = ?", (lesson_name,))
            lesson_id = cursor.fetchone()[0]
            cursor.execute("INSERT OR IGNORE INTO student_lessons (student_id, lesson_id) VALUES (?, ?)",
                           (student_id, lesson_id))

    conn.commit()
    conn.close()
    print("Student and lessons added successfully!")


def update_student():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    print("\n- Update Student Info -")
    student_id = input("Enter student ID to update: ").strip()
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if student:
        print(f"Current Info: {student[1]} {student[2]} - Age: {student[3]} - Grade: {student[4]}")
        print("Enter new info (or press Enter to keep current value):")
        new_firstname = input(f"New First Name [{student[1]}]: ").strip() or student[1]
        new_lastname = input(f"New Last Name [{student[2]}]: ").strip() or student[2]
        age_input = input(f"New Age [{student[3]}]: ").strip()
        new_age = int(age_input) if age_input else student[3]
        new_grade = input(f"New Grade [{student[4]}]: ").strip() or student[4]
        cursor.execute('''
            UPDATE students
            SET firstname = ?, lastname = ?, age = ?, grade = ?
            WHERE id = ?
        ''', (new_firstname, new_lastname, new_age, new_grade, student_id))

        conn.commit()
        print("Student info updated successfully!")
    else:
        print("Sorry, no student found with this ID.")

    conn.close()


def main_menu():
    create_tables()

    while True:
        print("\n=== School Management System ===")
        print("a - Add New Student")
        print("d - Delete Student")
        print("u - Update Student Info")
        print("s - Show Student Info")
        print("q - Quit Program")

        choice = input("Select an option: ").lower().strip()

        if choice == 'a':
            add_student()
        elif choice == 'd':
            delete_student()
        elif choice == 'u':
            update_student()
        elif choice == 's':
            show_student()
        elif choice == 'q':
            print("Exited the program successfully.")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main_menu()