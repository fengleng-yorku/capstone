class Grade:

    enrollment_id = 0
    assignment_id = 0
    mark = 0

    def __init__(self, enrollment_id, assignment_id, mark):
        self.enrollment_id = enrollment_id
        self.assignment_id = assignment_id
        self.mark = mark

    def getGradeDetails(self):
        return self.mark
