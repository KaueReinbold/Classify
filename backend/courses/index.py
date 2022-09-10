from flask import Flask, jsonify

from courses.model.course import Course, CourseSchema

app = Flask(__name__)

courses_mock = [
    Course('Python', 0),
    Course('ReactJs', 0),
    Course('Tests', 0)
]


@app.route("/courses")
def get_courses():
    schema = CourseSchema(many=True)

    courses = schema.dump(courses_mock)

    return jsonify(courses)


if __name__ == "__main__":
    app.run()
