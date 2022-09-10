import datetime as dt

from marshmallow import Schema, fields


class Course():
    def __init__(self, description,
                 time) -> None:
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
