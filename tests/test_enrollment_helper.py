from app.collections import Students, Enrollments
from app.helpers import EnrollmentHelper


enrollments = Enrollments()
students = Students()
enrollmentHelper = EnrollmentHelper(enrollments, students)


def loadTestData():
    enrollments.allEnrollments.clear()
    enrollments.bulkLoad()
    students.allStudents.clear()
    students.bulkLoad()


def testListStudentsByCourseID():
    loadTestData()
    listOfStudents = enrollmentHelper.listStudentsByCourseID(2)
    assert "Smith" in listOfStudents
    assert "Johnson" in listOfStudents
