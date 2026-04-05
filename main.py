from flask import Flask, jsonify, request, render_template

from app.db import MariaDBConnect
from app.collections import Students, Grades, Enrollments, Courses
from app.helpers import EnrollmentHelper, GradingHelper


app = Flask(__name__)

mariaDBConnect = MariaDBConnect()
conn = mariaDBConnect.createConnection()

students = Students()
grades = Grades()
enrollments = Enrollments()
courses = Courses()

students.bulkLoad(conn)
grades.bulkLoad(conn)
enrollments.bulkLoad(conn)
courses.bulkLoad(conn)

enrollmentHelper = EnrollmentHelper(enrollments, students)
gradingHelper = GradingHelper(grades, courses, enrollments)


# ── UI Routes ──────────────────────────────────────────────

@app.route('/')
def dashboard():
    enrollment_counts = {}
    for e in enrollments.allEnrollments:
        key = str(e.course_id)
        enrollment_counts[key] = enrollment_counts.get(key, 0) + 1

    stats = {
        "students": len(students.allStudents),
        "courses": len(courses.allCourses),
        "enrollments": len(enrollments.allEnrollments),
        "grades": len(grades.allGrades),
    }
    return render_template(
        'index.html',
        stats=stats,
        courses=courses.allCourses,
        students=students.allStudents,
        enrollment_counts=enrollment_counts,
    )


@app.route('/students')
def students_page():
    course_ID = request.args.get('course_ID')
    enrolled = []
    if course_ID:
        for enrollment in enrollments.allEnrollments:
            if str(enrollment.course_id) == str(course_ID):
                for student in students.allStudents:
                    if student.student_id == enrollment.student_id:
                        enrolled.append(student)
    return render_template(
        'students.html',
        courses=courses.allCourses,
        students=enrolled,
        selected_id=course_ID,
    )


@app.route('/grades')
def grades_page():
    student_ID = request.args.get('student_ID')
    student_grades = []
    student_info = None
    if student_ID:
        student_grades = gradingHelper.listGradesByStudentID(int(student_ID))
        for s in students.allStudents:
            if str(s.student_id) == str(student_ID):
                student_info = s
                break
    return render_template(
        'grades.html',
        all_students=students.allStudents,
        grades=student_grades,
        student_info=student_info,
        selected_id=student_ID,
    )


# ── API Routes ─────────────────────────────────────────────

@app.route('/listStudentsByCourseID', methods=['GET'])
def get_listStudentsByCourseID_response():
    course_ID = request.args.get('course_ID')
    listOfStudents = enrollmentHelper.listStudentsByCourseID(int(course_ID))
    return jsonify({"response": listOfStudents})


@app.route('/listGradesByStudentID', methods=['GET'])
def get_listGradesByStudentID_response():
    student_ID = request.args.get('student_ID')
    student_grades = gradingHelper.listGradesByStudentID(int(student_ID))
    result = [
        {"student_id": g[0], "course": g[1], "assignment_id": g[2], "mark": g[3]}
        for g in student_grades
    ]
    return jsonify({"response": result})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
