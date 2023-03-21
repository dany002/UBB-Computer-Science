import unittest

from domain.Grade import Grade

class TestGrade(unittest.TestCase):

    def test_grade__with_valid_data__setters_and_getters(self):
        grade = Grade(15, 20, 7)
        self.assertEqual(grade.student_id, 15)
        self.assertEqual(grade.discipline_id, 20)
        self.assertEqual(grade.grade_value, 7)
        grade.student_id = 48
        grade.discipline_id = 13
        grade.grade_value = 10
        self.assertEqual(grade.student_id, 48)
        self.assertEqual(grade.discipline_id, 13)
        self.assertEqual(grade.grade_value, 10)

    def test_str__with_valid_data__is_going_to_print_in_a_specific_format(self):
        grade = Grade(15, 20, 7)
        self.assertEqual(str(grade), 'Student id: 15  Discipline id: 20  Grade: 7')

    def test_eq__with_valid_data__is_going_to_check_if_two_grades_are_equal_or_not(self):
        grade = Grade(15, 20, 7)
        another_grade = Grade(15, 20, 7)
        self.assertEqual(grade, another_grade)
        another_grade_not_equal = Grade(34, 19, 5)
        self.assertNotEqual(grade, another_grade_not_equal)

    def test_grade(self):
        self.test_grade__with_valid_data__setters_and_getters()
        self.test_str__with_valid_data__is_going_to_print_in_a_specific_format()
        self.test_eq__with_valid_data__is_going_to_check_if_two_grades_are_equal_or_not()