# coding=utf-8

from model.course import Course
from base.base import Session, engine, Base

Base.metadata.create_all(engine)

session = Session()

courses = [
    Course('Python', 0),
    Course('ReactJs', 0),
    Course('Tests', 0)
]

for course in courses:
    session.add(course)

session.commit()
session.close()
