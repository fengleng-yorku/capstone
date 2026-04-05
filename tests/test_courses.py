from app.models import Course
from app.collections import Courses


courses = Courses()


def testBulkLoadCourses():
    courses.allCourses.clear()
    assert courses.bulkLoad() == 12


def testAddOneCourse():
    course = Course(1, "Introduction to Python", "Novice")
    assert courses.addCourse(course) == True
