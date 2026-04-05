from app.models import Enrollment

enrollment_id = 1
course_id = 2
student_id = 3


def testCreateEnrollmentAndReturnDetails():
    enrollment = Enrollment(enrollment_id, course_id, student_id)
    enrolled_course_id, enrolled_student_id = enrollment.getEnrollmentDetails()
    assert enrolled_course_id == course_id
    assert enrolled_student_id == student_id
