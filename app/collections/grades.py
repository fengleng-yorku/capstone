import csv
from app.models.grade import Grade
from app.utilities import Utilities


class Grades:

    def __init__(self):
        self.allGrades = []

    def addGrade(self, grade):
        if grade.assignment_id > 0:
            self.allGrades.append(grade)
            return True
        return False

    def bulkLoad(self, conn=None):
        if Utilities.isItTest():
            with open('./../TestData/SampleGradeData.csv', 'r') as csvfile:
                read_csv = csv.reader(csvfile, delimiter=',')
                row_counter = 0
                for row in read_csv:
                    row_counter += 1
                    if row_counter > 1:
                        self.allGrades.append(
                            Grade(row[0], row[1], row[2])
                        )
        else:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Grades")
            for (enrollment_id, assignment_id, mark) in cur:
                self.allGrades.append(Grade(enrollment_id, assignment_id, mark))
        return len(self.allGrades)
