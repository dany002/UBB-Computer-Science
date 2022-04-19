
class Error(Exception):
    pass

class StudentNameError(Error):
    pass

class StudentIdError(Error):
    pass

class StudentUniqueIdError(Error):
    pass

class StudentValidator:
    @staticmethod
    def validate(student_id, student_name):
        if student_name.isalpha() == False and student_name.find(" ") == -1:
            raise StudentNameError
        if int(student_id) < 0:
            raise StudentIdError


class DisciplineNameError(Error):
    pass

class DisciplineIdError(Error):
    pass

class DisciplineUniqueIdError(Error):
    pass

class DisciplineValidator:
    @staticmethod
    def validate(discipline_id, discipline_name):
        if discipline_name.isalpha() == False and discipline_name.find(" ") == -1:
            raise DisciplineNameError
        if int(discipline_id) < 0:
            raise DisciplineIdError


class StudentOrDisciplineError(Error):
    pass

class StudentsOrDisciplinesOrGradesError(Error):
    pass

class NameOrId(Error):
    pass

class GradeError(Error):
    pass

class GradeValidator:
    @staticmethod
    def validate(student_id, discipline_id, grade_value):
        if int(student_id) < 0:
            raise StudentIdError
        if int(discipline_id) < 0:
            raise DisciplineIdError
        if int(grade_value) < 0 or int(grade_value) > 10:
            raise GradeError

class StudentIdNotFoundError(Error):
    pass

class DisciplineIdNotFoundError(Error):
    pass