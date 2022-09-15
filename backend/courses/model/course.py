import datetime as dt

from marshmallow import Schema, fields

from sqlalchemy import Column, String, Integer, DateTime

from courses.base.base import Base


class Course(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    description = Column(String)
    time = Column(Integer)
    created_on = Column(DateTime)
    modified_on = Column(DateTime)

    def __init__(
        self,
        description,
        time
    ) -> None:
        self.description = description
        self.time = time
        self.created_on = dt.datetime.now()
        self.modified_on = None

    def __repr__(self):
        return '<Course(name={self.description!r})>'.format(self=self)


class CourseSchema(Schema):
    description = fields.Str()
    time = fields.Number()
    created_on = fields.DateTime()
    modified_on = fields.DateTime()
