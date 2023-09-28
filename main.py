import datetime
from sqlalchemy import create_engine, func, desc
from sqlalchemy.orm import Session

from models import Base, Student, Subject, Grade, Group, Tutor, Course
from my_select import select_1, select_2, select_3, select_4, select_5, select_6, select_7, select_8, select_9, select_10
from models import *


# Create the database tables
Base.metadata.create_all(engine)

# Create a session to interact with the database (assuming the engine is already defined in models.py)
Session = sessionmaker(bind=engine)
session = Session()

# Define your queries here (select_1, select_2, ..., select_10)

menu_options = {
    1: "Find 5 students with the highest average grade from all subjects",
    2: "Find a student with the highest average grade in a specific subject",
    3: "Find average grades within groups for a specific subject",
    4: "Find the average grade across all grades",
    5: "Find what courses each Tutor reads",
    6: "Find groups and the students in each group",
    7: "Find group names, student names, grades, and dates for a specific subject",
    8: "Find teachers and their average grades for subjects they teach",
    9: "Find students and the subjects they attended",
    10: "Find teachers, students, and the subjects taught by each teacher to each student"
}

subject_name = ""

while True:
    print("Select a query to execute:")
    for key, value in menu_options.items():
        print(f"{key}: {value}")

    # Get user input
    user_choice = input("Enter the number of the query you want to execute (1-10), or 'q' to quit: ")

    if user_choice == 'q':
        break

    # Execute the selected query
    if user_choice.isdigit():  # Check if the input is a digit
        query_number = int(user_choice)

        if query_number in menu_options:
            if query_number in {2, 3, 7}:
                # Retrieve the list of subjects from the database
                subjects = session.query(Subject.name).all()

                # Display the list of subjects to the user
                print("Available subjects:")
                for i, subject in enumerate(subjects, start=1):
                    print(f"{i}: {subject[0]}")

                # Ask the user to select a subject from the list
                subject_choice = input("Enter the number of the subject you want to query: ")

                try:
                    subject_index = int(subject_choice)
                    if 1 <= subject_index <= len(subjects):
                        subject_name = subjects[subject_index - 1][0]
                    else:
                        print("Invalid subject selection.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number.")

            # Execute the selected query and print the result
            if query_number == 1:
                results = select_1(session)
                if results:
                    # Print the result for query 1
                    print("\nQuery Result for Query 1:")
                    for result in results:
                        print(f"{result.fullname}: {result.avg_grade}")
                else:
                    print("No result to display for query 1.")
            elif query_number == 2:
                if result := select_2(session, subject_name):
                    # Print the result for query 2
                    print("\nQuery Result for Query 2:")
                    print(f"Student with the highest average grade in '{subject_name}': {result[0]}")
                else:
                    print(f"No result to display for query 2 with subject '{subject_name}'.")
            elif query_number == 3:
                if result := select_3(session, subject_name):
                    # Print the result for query 3
                    print("\nQuery Result for Query 3:")
                    for row in result:
                        print(f"Group: {row.group_name}, Average Grade: {row.average_grade}")
                else:
                    print(f"No result to display for query 3 with subject '{subject_name}'.")
            elif query_number == 4:
                result = select_4(session)
                # Print the result for query 4
                print(f"\nQuery Result for Query 4:\nAverage Grade: {result}")

            elif query_number == 5:
                if result := select_5(session):
                    # Print the result for query 5
                    print("\nQuery Result for Query 5:")
                    for row in result:
                        print(f"Tutor: {row.first_name} {row.last_name}\nSubjects Taught: {row.subjects_taught}")
                else:
                    print("No result to display for query 5.")
            elif query_number == 6:
                if result := select_6(session):
                    # Print the result for query 6
                    print("\nQuery Result for Query 6:")
                    for row in result:
                        print(f"Group: {row.group_name}\nStudents: {row.students_in_group}")
                else:
                    print("No result to display for query 6.")
            elif query_number == 7:
                if result := select_7(session, subject_name):
                    # Print the result for query 7
                    print("\nQuery Result for Query 7:")
                    for row in result:
                        print(f"Group: {row.group_name}\nStudent: {row.student_name}\nGrade: {row.grade}\nDate: {row.date}")
                else:
                    print(f"No result to display for query 7 with subject '{subject_name}'.")
            elif query_number == 8:
                if result := select_8(session):
                    # Print the result for query 8
                    print("\nQuery Result for Query 8:")
                    for row in result:
                        print(f"Tutor: {row.first_name} {row.last_name}\nAverage Grade: {row.average_grade}")
                else:
                    print("No result to display for query 8.")
            elif query_number == 9:
                results = select_9(session)
                if results:
                    # Print the result for query 9
                    print("\nQuery Result for Query 9:")
                    for result in results:
                        first_name, last_name, courses_attended = result
                        print(f"Student: {first_name} {last_name}\nCourses Attended: {courses_attended}")
                else:
                    print("No result to display for query 9.")

            elif query_number == 10:
                results = select_10(session)
                if results:
                    # Print the result for query 10
                    print("\nQuery Result for Query 10:")
                    for result in results:
                        tutor_first_name, tutor_last_name, student_name, subjects_taught = result
                        print(f"Tutor: {tutor_first_name} {tutor_last_name}\nStudent: {student_name}\nSubjects Taught: {subjects_taught}")
                else:
                    print("No result to display for query 10.")
            else:
                print("Invalid choice. Please enter a valid option (1-10) or 'q' to quit.")

        else:
            print("Invalid input. Please enter a valid option (1-10) or 'q' to quit.")

# Close the session
session.close()