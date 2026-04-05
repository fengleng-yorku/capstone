from app.models import Student
from app.collections import Students


students = Students()


def testBulkLoadStudents():
    students.allStudents.clear()
    assert students.bulkLoad() == 25


def testAddOneStudent():
    student = Student(1, "Talvin", "Singh", "12/12/2000")
    assert students.addStudent(student) == True
