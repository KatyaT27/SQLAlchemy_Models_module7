from sqlalchemy import func, desc, literal, text
from sqlalchemy.orm import Session
from models import Student, Subject, Grade, Group, Tutor, Course
from models import *

def select_1(session: Session):
    return session.query((Student.first_name + ' ' + Student.last_name).label('fullname'),
                         func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .group_by(Student.id) \
        .order_by(desc('avg_grade')) \
        .limit(5) \
        .all()
    return result or None

def select_2(session: Session, subject_name: str):
    return session.query((Student.first_name + ' ' + Student.last_name).label('student_name'),
                         func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Subject.name == subject_name) \
        .group_by(Student.first_name, Student.last_name) \
        .order_by(desc('average_grade')) \
        .limit(1) \
        .first()

def select_3(session: Session, subject_name: str):
    return session.query(Group.name.label('group_name'),
                         func.round(func.avg(Grade.grade), 2).label('average_grade')) \
        .join(Student, Group.id == Student.group_id) \
        .join(Grade, Student.id == Grade.student_id) \
        .join(Subject, Grade.subject_id == Subject.id) \
        .filter(Subject.name == subject_name) \
        .group_by(Group.name) \
        .order_by(desc('average_grade')) \
        .all()

def select_4(session: Session):
    return session.query(func.avg(Grade.grade).label('average_grade')).scalar()


def select_5(session: Session):
    return session.query(
        Tutor.first_name,
        Tutor.last_name,
        func.group_concat(Subject.name, ', ').label('subjects_taught')
    ).outerjoin(Subject, Tutor.id == Subject.tutor_id) \
     .group_by(Tutor.first_name, Tutor.last_name) \
     .all()




def select_6(session: Session):
    subquery = session.query(
        Student.group_id,
        func.group_concat(literal(' ').concat(Student.first_name).concat(' ').concat(Student.last_name), ', ').label('students_in_group')
    ).group_by(Student.group_id).subquery()

    return session.query(
        Group.name.label('group_name'),
        subquery.c.students_in_group
    ).join(subquery, Group.id == subquery.c.group_id).all()



def select_7(session: Session, subject_name: str):
    return session.query(
        Group.name.label('group_name'),
        (Student.first_name + ' ' + Student.last_name).label('student_name'),
        Grade.grade,
        Grade.date
    ).join(Student, Group.id == Student.group_id) \
     .join(Grade, Student.id == Grade.student_id) \
     .join(Subject, Grade.subject_id == Subject.id) \
     .filter(Subject.name == subject_name) \
     .order_by(Grade.date) \
     .all()

def select_8(session: Session):
    return session.query(Tutor.first_name, Tutor.last_name,
                         func.avg(Grade.grade).label('average_grade')) \
        .join(Subject, Tutor.id == Subject.tutor_id) \
        .join(Grade, Subject.id == Grade.subject_id) \
        .group_by(Tutor.first_name, Tutor.last_name) \
        .all()

def select_9(session: Session):
    return session.query(Student.first_name, Student.last_name,
                         func.group_concat(Subject.name, ', ').label('courses_attended')) \
        .outerjoin(Grade, Student.id == Grade.student_id) \
        .outerjoin(Subject, Grade.subject_id == Subject.id) \
        .group_by(Student.first_name, Student.last_name) \
        .all()

def select_10(session):
    query = (
        session.query(
            Tutor.first_name.label('tutor_first_name'),
            Tutor.last_name.label('tutor_last_name'),
            (Student.first_name + ' ' + Student.last_name).label('student_name'),
            func.group_concat(Subject.name, ', ').label('subjects_taught')
        )
        .join(Subject, Tutor.id == Subject.tutor_id)
        .join(Grade, Subject.id == Grade.subject_id)
        .join(Student, Grade.student_id == Student.id)
        .group_by(
            Tutor.first_name,
            Tutor.last_name,
            Student.first_name,
            Student.last_name,
        )
    )

    return query.all()