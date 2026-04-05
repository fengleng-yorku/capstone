from app.models import Grade
from app.collections import Grades


grades = Grades()


def testBulkLoadGrades():
    grades.allGrades.clear()
    assert grades.bulkLoad() == 13


def testAddOneGrade():
    grade = Grade(1, 2, 3)
    assert grades.addGrade(grade) == True
