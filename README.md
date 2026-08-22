School Management System

This project is a simple School Management System made using Python and SQLite.

The program allows the user to manage student information and their enrolled lessons.

The main functions of the program are:

- Add a new student
- Delete a student
- Update student information
- Display student information
- Add lessons to students
- Store all information in an SQLite database

Technologies Used:

Python 3
SQLite3

Database:

The program uses three tables:

1. students
Stores the student's ID, first name, last name, age, grade, and registration date.

2. lessons
Stores the lesson ID and lesson title.

3. student_lessons
Connects students with their enrolled lessons.

Main Functions:

create_tables()
Creates the database tables when the program starts.

add_student()
Adds a new student and allows the user to enter the lessons they are enrolled in.

delete_student()
Deletes a student using their ID. If the student does not exist, a message is displayed.

update_student()
Updates the student's first name, last name, age, or grade. The user can press Enter to keep the current value.

show_student()
Displays the student's information and the lessons they are enrolled in.

main_menu()
Displays the main menu and allows the user to choose what operation they want to perform.

How to Run:

Make sure Python 3 is installed, then run:

python main.py

The program will automatically create the school.db database and the required tables.

Main Menu:

a - Add New Student
d - Delete Student
u - Update Student Info
s - Show Student Info
q - Quit Program

The project also includes the pseudocode and flowchart to explain the program logic.


This project was created for educational purposes.
