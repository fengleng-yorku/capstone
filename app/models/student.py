class Student:

    student_id = 0
    first_name = ""
    surname = ""
    date_of_birth = ""

    def __init__(self, student_id, first_name, surname, date_of_birth):
        self.student_id = student_id
        self.first_name = first_name
        self.surname = surname
        self.date_of_birth = date_of_birth

    def getSurname(self):
        return self.surname

    def student_to_dict(self):
        return {
            "student_ID": self.student_id,
            "first_Name": self.first_name,
            "surname": self.surname,
            "date_Of_Birth": self.date_of_birth,
        }
