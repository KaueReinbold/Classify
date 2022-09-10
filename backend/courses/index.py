from flask import Flask, jsonify

app = Flask(__name__)

courses = [
    'Python',
    'ReactJs',
    'Tests'
]

@app.route("/courses")
def get_courses():
    return jsonify(courses)
