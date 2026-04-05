"""Helper class used to combine data from grades, courses and enrollments."""

from app.collections.grades import Grades
from app.collections.courses import Courses
from app.collections.enrollments import Enrollments


class GradingHelper:

    def __init__(self, grades, courses, enrollments):
        self.grades = grades
        self.courses = courses
        self.enrollments = enrollments

    def listGradesByStudentID(self, student_id):
        """Return a list of [student_id, course_name, assignment_id, mark] for the given student."""
        students_grades = []
        for enrollment in self.enrollments.allEnrollments:
            if int(enrollment.student_id) == student_id:
                for course in self.courses.allCourses:
                    if enrollment.course_id == course.course_id:
                        for grade in self.grades.allGrades:
                            if enrollment.enrollment_id == grade.enrollment_id:
                                students_grades.append([
                                    student_id,
                                    course.course_name,
                                    grade.assignment_id,
                                    grade.mark,
                                ])
        return students_grades
