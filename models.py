import datetime

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

import psycopg2
conn_string = "host='localhost' dbname='my_database' user='postgres' password='secret'"
DATABASE_URL = f"postgresql+psycopg2://postgres:secret@db:5432/postgres"


DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    name = Column(String)

    tutor_id = Column(Integer, ForeignKey('tutors.id'))
    tutor = relationship('Tutor', back_populates='courses')


class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)


class Person():
    first_name = Column(String(250))
    last_name = Column(String(250))


class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship(Group, backref="students")


subjects_to_tutors = Table('subjects_to_tutors', Base.metadata,
                           Column('id', Integer, primary_key=True),
                           Column('tutor_id', Integer,
                                  ForeignKey('tutors.id')),
                           Column('subject_id', Integer,
                                  ForeignKey('subjects.id'))
                           )


class Tutor(Base):
    __tablename__ = "tutors"
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    courses = relationship("Course", back_populates="tutor")


class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    
    # Add a foreign key relationship to Tutor
    tutor_id = Column(Integer, ForeignKey('tutors.id'))
    
    # Define the relationship
    tutor = relationship("Tutor", backref="subjects")


class Grade(Base):
    __tablename__ = "grades"
    id = Column(Integer, primary_key=True)
    grade = Column(Integer)
    date = Column(DateTime, default=datetime.datetime.utcnow)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship(Student, backref="grades")

    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject = relationship(Subject, backref="grades")


Base.metadata.bind = engine
