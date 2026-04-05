import json
from app.collections.enrollments import Enrollments
from app.collections.students import Students


class EnrollmentHelper:

    def __init__(self, enrollments, students):
        self.enrollments = enrollments
        self.students = students

    def listStudentsByCourseID(self, course_id):
        enrolled_students = []
        for enrollment in self.enrollments.allEnrollments:
            if int(enrollment.course_id) == course_id:
                for student in self.students.allStudents:
                    if student.student_id == enrollment.student_id:
                        enrolled_students.append(student)

        json_string = ""
        for student in enrolled_students:
            json_string += '\n' + json.dumps(student.student_to_dict(), indent=4, default=str)
        return json_string
