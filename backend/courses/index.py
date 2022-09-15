from flask import Flask, jsonify
from courses.base.base import Session

from courses.model.course import Course, CourseSchema

app = Flask(__name__)


@app.route("/courses")
def get_courses():
    session = Session()

    courses_result = session.query(Course).all()

    schema = CourseSchema(many=True)

    courses = schema.dump(courses_result)

    return jsonify(courses)


if __name__ == "__main__":
    app.run()
