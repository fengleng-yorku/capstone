import csv
from app.models.enrollment import Enrollment
from app.utilities import Utilities


class Enrollments:

    def __init__(self):
        self.allEnrollments = []

    def addEnrollment(self, enrollment):
        if enrollment.enrollment_id > 0:
            self.allEnrollments.append(enrollment)
            return True
        return False

    def bulkLoad(self, conn=None):
        if Utilities.isItTest():
            with open('./../TestData/SampleEnrollmentData.csv', 'r') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                row_counter = 0
                for row in readCSV:
                    row_counter += 1
                    if row_counter > 1:
                        self.allEnrollments.append(
                            Enrollment(row[0], row[1], row[2])
                        )
        else:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Enrollments")
            for (enrollment_id, course_id, student_id) in cur:
                self.allEnrollments.append(Enrollment(enrollment_id, course_id, student_id))
        return len(self.allEnrollments)
