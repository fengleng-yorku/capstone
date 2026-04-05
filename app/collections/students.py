import csv
from app.models.student import Student
from app.utilities import Utilities


class Students:

    def __init__(self):
        self.allStudents = []

    def addStudent(self, student):
        if student.student_id > 0:
            self.allStudents.append(student)
            return True
        return False

    def bulkLoad(self, conn=None):
        if Utilities.isItTest():
            with open('./../TestData/SampleStudentData.csv', 'r') as csvfile:
                readCSV = csv.reader(csvfile, delimiter=',')
                row_counter = 0
                for row in readCSV:
                    row_counter += 1
                    if row_counter > 1:
                        self.allStudents.append(
                            Student(row[0], row[1], row[2], row[3])
                        )
        else:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Students")
            for (student_id, first_name, surname, date_of_birth) in cur:
                self.allStudents.append(Student(student_id, first_name, surname, date_of_birth))
        return len(self.allStudents)
