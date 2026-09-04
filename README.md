School Management System (SQLite & Python)
A simple CLI-based School Management System built using Python and SQLite. The system allows managing student records and their enrolled lessons using relational database design principles (many-to-many relationship).

Features
Add Student (a):

Validates user input (letters-only names, positive integer age, valid YYYY-MM-DD date format).

Automatically generates and displays the newly created Student ID.

Adds comma-separated lessons without duplicating existing lesson titles.

Delete Student (d):

Removes a student record by ID with automatic cascade deletion of linked lesson enrollments.

Update Student (u):

Allows updating specific fields (First Name, Last Name, Age, Grade) while retaining existing values if left blank.

Show Student Info (s):

Displays complete student details along with all enrolled lessons retrieved via SQL JOIN.

Data Integrity:

Foreign key constraints enabled to maintain relational integrity.

Case-insensitive lesson formatting to avoid duplication.

Database Architecture
The system uses three main relational tables:

students: Stores primary student details (id, firstname, lastname, age, grade, reg_date).

lessons: Stores unique lesson titles (id, title).

student_lessons: Junction table handling the many-to-many relationship between students and lessons (student_id, lesson_id).

Getting Started
Prerequisites
Python 3.x

SQLite3 (Included with standard Python installation)

How to Run
Clone the repository:
git clone https://github.com/your-username/your-repository-name.git

Navigate to the project directory:
cd your-repository-name

Run the application:
python main.py

Usage Example
=== School Management System ===
a - Add New Student
d - Delete Student
u - Update Student Info
s - Show Student Info
q - Quit Program

License
This project is open source and available for educational purposes.
