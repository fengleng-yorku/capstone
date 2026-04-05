from app.models import Grade

enrollment_id = 1
assignment_id = 2
mark = 80


def testCreateGradeAndReturnDetails():
    grade = Grade(enrollment_id, assignment_id, mark)
    assert grade.getGradeDetails() == mark
