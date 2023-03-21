import unittest

from domain.Grade import Grade
from repository.GradeBinFileRepository import GradeBinFileRepository
import os.path

class TestGradeBinFileRepository(unittest.TestCase):

    def setUp(self) -> None:
        file_name = "grades_bin_test"
        self.__grade_repository = GradeBinFileRepository(file_name)

    def tearDown(self) -> None:
        if os.path.exists("grades_bin_test"):
            os.remove("grades_bin_test")

    """
        TESTS FOR ADD
    """
    def test_add_a_grade__with_valid_data__is_going_to_grade_a_student_id_to_a_discipline_id_with_a_grade_value(self):
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(3, 5, 10))
        self.__grade_repository.add_a_grade_for_a_student(Grade(3, 5, 10))
        self.assertEqual(self.__grade_repository.list_of_grades(), list_of_expected_grades)

    """
        TESTS FOR REMOVE
    """

    def test_remove_grades_for_a_student__with_valid_data__is_going_to_remove_all_the_grades_for_a_given_student_id(self):
        self.__grade_repository.add_a_grade_for_a_student(Grade(3, 5, 10))
        self.__grade_repository.add_a_grade_for_a_student(Grade(4, 8, 6))
        self.__grade_repository.add_a_grade_for_a_student(Grade(3, 7, 9))
        self.__grade_repository.add_a_grade_for_a_student(Grade(10, 5, 8))
        self.__grade_repository.remove_grades_for_a_student(3)
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(4, 8, 6))
        list_of_expected_grades.append(Grade(10, 5, 8))
        self.assertEqual(self.__grade_repository.list_of_grades(), list_of_expected_grades)

    def test_remove_grades_for_a_discipline__with_valid_data__is_going_to_remove_all_the_grades_for_a_given_discipline_id(self):
        self.__grade_repository.add_a_grade_for_a_student(Grade(3, 5, 10))
        self.__grade_repository.add_a_grade_for_a_student(Grade(4, 8, 6))
        self.__grade_repository.add_a_grade_for_a_student(Grade(3, 7, 9))
        self.__grade_repository.add_a_grade_for_a_student(Grade(10, 5, 8))
        self.__grade_repository.remove_grades_for_a_discipline(5)
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(4, 8, 6))
        list_of_expected_grades.append(Grade(3, 7, 9))
        self.assertEqual(self.__grade_repository.list_of_grades(), list_of_expected_grades)

    def test_remove_grade_for_a_student_at_a_discipline__with_valid_data__is_going_to_remove_the_grade_for_that_student_at_that_discipline_with_that_grade(self):
        self.__grade_repository.add_a_grade_for_a_student(Grade(3, 5, 10))
        self.__grade_repository.add_a_grade_for_a_student(Grade(4, 8, 6))
        self.__grade_repository.add_a_grade_for_a_student(Grade(3, 5, 9))
        self.__grade_repository.add_a_grade_for_a_student(Grade(10, 5, 8))
        self.__grade_repository.remove_a_grade_for_a_student_at_a_discipline(3, 5, 9)
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(3, 5, 10))
        list_of_expected_grades.append(Grade(4, 8, 6))
        list_of_expected_grades.append(Grade(10, 5, 8))
        self.assertEqual(self.__grade_repository.list_of_grades(), list_of_expected_grades)


    """
        TESTS FOR LENGTH
    """

    def test_length_of_grades_list__with_valid_data__is_going_to_return_the_length_of_grades_list(self):
        self.__grade_repository.add_a_grade_for_a_student(Grade(3, 5, 10))
        self.__grade_repository.add_a_grade_for_a_student(Grade(4, 8, 6))
        self.__grade_repository.add_a_grade_for_a_student(Grade(3, 7, 9))
        self.__grade_repository.add_a_grade_for_a_student(Grade(10, 5, 8))
        self.assertEqual(self.__grade_repository.length_of_grades(), 4)

    """
        TESTS FOR INDEX
    """

    def test_get_index_of_grades_list__with_valid_data__is_going_to_return_the_indexth_element_of_the_grades_list(self):
        self.__grade_repository.add_a_grade_for_a_student(Grade(3, 5, 10))
        self.__grade_repository.add_a_grade_for_a_student(Grade(4, 8, 6))
        self.__grade_repository.add_a_grade_for_a_student(Grade(3, 7, 9))
        self.__grade_repository.add_a_grade_for_a_student(Grade(10, 5, 8))
        self.assertEqual(self.__grade_repository.get_index_of_grades_list(2), Grade(3, 7, 9))
