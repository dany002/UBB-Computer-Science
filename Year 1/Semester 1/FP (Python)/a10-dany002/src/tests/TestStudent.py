import unittest

from domain.Student import Student

class TestStudent(unittest.TestCase):

    def test_student__with_valid_data__setters_and_getters(self):
        student = Student(23,"Dani")
        self.assertEqual(student.student_id, 23)
        self.assertEqual(student.name, "Dani")
        student.student_id = 48
        student.name = "Alex"
        self.assertEqual(student.student_id, 48)
        self.assertEqual(student.name, "Alex")

    def test_str__with_valid_data__is_going_to_print_in_a_specific_format(self):
        student = Student(23,"Dani")
        self.assertEqual(str(student), 'Student id: 23  Student name: Dani')

    def test_eq__with_valid_data__is_going_to_check_if_two_students_are_equal_or_not(self):
        student = Student(23,"Dani")
        another_student = Student(23,"Dani")
        self.assertEqual(student, another_student)
        another_student_not_equal = Student(34,"Alin")
        self.assertNotEqual(student, another_student_not_equal)

    def test_student(self):
        self.test_student__with_valid_data__setters_and_getters()
        self.test_eq__with_valid_data__is_going_to_check_if_two_students_are_equal_or_not()
        self.test_str__with_valid_data__is_going_to_print_in_a_specific_format()