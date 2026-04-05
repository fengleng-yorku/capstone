from app.models import Enrollment
from app.collections import Enrollments


enrollments = Enrollments()


def testBulkLoadEnrollments():
    enrollments.allEnrollments.clear()
    assert enrollments.bulkLoad() == 10


def testAddOneEnrollment():
    enrollment = Enrollment(1, 2, 3)
    assert enrollments.addEnrollment(enrollment) == True
