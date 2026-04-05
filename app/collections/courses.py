import csv
from app.models.course import Course
from app.utilities import Utilities


class Courses:

    def __init__(self):
        self.allCourses = []

    def addCourse(self, course):
        if course.course_id > 0:
            self.allCourses.append(course)
            return True
        return False

    def bulkLoad(self, conn=None):
        if Utilities.isItTest():
            with open('./../TestData/SampleCourseData.csv', 'r') as csvfile:
                read_csv = csv.reader(csvfile, delimiter=',')
                row_counter = 0
                for row in read_csv:
                    row_counter += 1
                    if row_counter > 1:
                        self.allCourses.append(
                            Course(row[0], row[1], row[2])
                        )
        else:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Courses")
            for (course_id, course_name, level) in cur:
                self.allCourses.append(Course(course_id, course_name, level))
        return len(self.allCourses)
