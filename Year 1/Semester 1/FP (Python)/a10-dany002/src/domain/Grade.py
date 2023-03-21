
class Grade:
    def __init__(self, student_id, discipline_id, grade_value):
        self.__grade_value = grade_value
        self.__student_id = student_id
        self.__discipline_id = discipline_id

    @property
    def student_id(self):
        return self.__student_id
    
    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    @property
    def discipline_id(self):
        return self.__discipline_id
    
    @discipline_id.setter
    def discipline_id(self, discipline_id):
        self.__discipline_id = discipline_id

    @property
    def grade_value(self):
        return self.__grade_value

    @grade_value.setter
    def grade_value(self, grade_value):
        self.__grade_value = grade_value

    def __eq__(self, other_grade):
        if self.grade_value == other_grade.grade_value:
            if self.discipline_id == other_grade.discipline_id:
                if self.student_id == other_grade.student_id:
                    return True
        return False

    def __str__(self):
        return f'Student id: ' + str(self.student_id) + '  Discipline id: ' + str(self.discipline_id) + '  Grade: ' + str(self.grade_value)
