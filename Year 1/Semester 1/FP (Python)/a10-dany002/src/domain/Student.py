

class Student:
    def __init__(self, student_id, name):
        self.__student_id = student_id
        self.__name = name

        
    @property
    def student_id(self):
        return self.__student_id
    
    @student_id.setter
    def student_id(self, student_id):
        self.__student_id = student_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    def __eq__(self, other_student):
        if self.student_id == other_student.student_id:
            if self.name == other_student.name:
                return True
        return False


    def __str__(self):
        return f'Student id: ' + str(self.student_id) + '  Student name: ' + self.name
