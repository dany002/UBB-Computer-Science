import unittest

from domain.Validators import StudentValidator, StudentIdError, StudentNameError, DisciplineValidator,\
    DisciplineIdError, DisciplineNameError, GradeValidator, GradeError

class TestValidators(unittest.TestCase):

    def test_StudentValidator__raise_exception_Student_Name_Error__student_name_contains_digits(self):
        with self.assertRaises(StudentNameError):
            StudentValidator.validate(15, "Al1n")

    def test_StudentValidator__raise_exception_Student_Id_Error__student_id_is_negative(self):
        with self.assertRaises(StudentIdError):
            StudentValidator.validate(-5,"Alin")

    def test_StudentValidator(self):
        self.test_StudentValidator__raise_exception_Student_Name_Error__student_name_contains_digits()
        self.test_StudentValidator__raise_exception_Student_Id_Error__student_id_is_negative()


    def test_DisciplineValidator__raise_exception_Discipline_Name_Error__discipline_name_contains_digits(self):
        with self.assertRaises(DisciplineNameError):
            DisciplineValidator.validate(15,"Math3")

    def test_DisciplineValidator__raise_exception_Discipline_Id_Error__discipline_id_is_negative(self):
        with self.assertRaises(DisciplineIdError):
            DisciplineValidator.validate(-48, "Math")

    def test_DisciplineValidator(self):
        self.test_DisciplineValidator__raise_exception_Discipline_Id_Error__discipline_id_is_negative()
        self.test_DisciplineValidator__raise_exception_Discipline_Name_Error__discipline_name_contains_digits()


    def test_GradeValidator__raise_exception_Student_Id_Error__student_id_is_negative(self):
        with self.assertRaises(StudentIdError):
            GradeValidator.validate(-3,15,10)

    def test_GradeValidator__raise_exception_Discipline_Id_Error__discipline_id_is_negative(self):
        with self.assertRaises(DisciplineIdError):
            GradeValidator.validate(12,-9,7)

    def test_GradeValidator__raise_exception_Grade_Error__grade_value_is_not_in_range_1_10(self):
        with self.assertRaises(GradeError):
            GradeValidator.validate(13,24,12)

    def test_GradeValidator(self):
        self.test_GradeValidator__raise_exception_Discipline_Id_Error__discipline_id_is_negative()
        self.test_GradeValidator__raise_exception_Grade_Error__grade_value_is_not_in_range_1_10()
        self.test_GradeValidator__raise_exception_Student_Id_Error__student_id_is_negative()

    def test_validators(self):
        self.test_StudentValidator()
        self.test_DisciplineValidator()
        self.test_GradeValidator()