import itertools
import random
from faker import Faker
from models import Group, Student, Tutor, Subject, Grade, DBSession

fake = Faker()

def create_fake_data():
    session = DBSession()

    # Create groups
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)
    session.commit()

    # Create tutors
    tutors = [Tutor(first_name=fake.first_name(), last_name=fake.last_name()) for _ in range(5)]
    session.add_all(tutors)
    session.commit()

    # Create subjects
    subjects = [Subject(name=fake.word(), tutor=random.choice(tutors)) for _ in range(8)]
    session.add_all(subjects)
    session.commit()

    # Create students
    students = [Student(first_name=fake.first_name(), last_name=fake.last_name(), group=random.choice(groups)) for _ in range(30)]
    session.add_all(students)
    session.commit()

    # Create grades
    for student, subject in itertools.product(students, subjects):
        grade = Grade(grade=random.randint(1, 12), student=student, subject=subject)
        session.add(grade)
    session.commit()

    # Print grades
    grades = session.query(Grade).all()
    for grade in grades:
        print('****************')
        student_fullname = f"{grade.student.first_name} {grade.student.last_name}"
        print(student_fullname)
        print(grade.subject.name)
        print(grade.grade)
        print(grade.subject.tutor.first_name)

if __name__ == "__main__":
    create_fake_data()
