import unittest

from domain.Grade import Grade
from repository.StudentRepository import StudentRepository
from repository.DisciplineRepository import DisciplineRepository
from repository.GradeRepository import GradeRepository
from services.GradesService import GradesService
from services.StudentsService import StudentsService
from services.DisciplinesService import DisciplinesService
from domain.Validators import GradeError, StudentIdError, DisciplineIdError, StudentIdNotFoundError, \
    DisciplineIdNotFoundError


class TestGradesService(unittest.TestCase):
    def setUp(self) -> None:
        self.__student_repository = StudentRepository()
        self.__disciplines_repository = DisciplineRepository()
        self.__grade_repository = GradeRepository()
        self.__grade_service = GradesService(self.__student_repository, self.__disciplines_repository, self.__grade_repository)
        self.__student_service = StudentsService(self.__student_repository, self.__grade_repository)
        self.__disciplines_service = DisciplinesService(self.__disciplines_repository, self.__grade_repository)

        self.__student_service.add_a_student("11","Dani")
        self.__student_service.add_a_student("12","Alin")
        self.__student_service.add_a_student("13","George")
        self.__student_service.add_a_student("14","Florin")
        self.__student_service.add_a_student("15","Alexandra")

        self.__disciplines_service.add_a_discipline("11","FP")
        self.__disciplines_service.add_a_discipline("12","Logic")
        self.__disciplines_service.add_a_discipline("13","Math")
        self.__disciplines_service.add_a_discipline("14","Chinese")
        self.__disciplines_service.add_a_discipline("15","Russian")

    def tearDown(self) -> None:
        pass

    """
        TESTS FOR ADD
    """

    def test_add_a_grade__with_valid_data__is_going_to_be_added_in_the_class(self):
        self.__grade_service.add_a_grade("15","13","10")
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(15, 13, 10))
        self.assertEqual(self.__grade_service.list_of_grades(), list_of_expected_grades)

    def test_add_a_grade__raise_exception_GradeError__grade_contains_letters(self):
        with self.assertRaises(GradeError) as exc:
            self.__grade_service.add_a_grade("15","13","1o")
        self.assertEqual(str(exc.exception), "Grade must be a positive integer.")

    def test_add_a_grade__raise_exception_StudentIdError__student_id_contains_letters(self):
        with self.assertRaises(StudentIdError) as exc:
            self.__grade_service.add_a_grade("1e","13","10")
        self.assertEqual(str(exc.exception), "Student id must be a positive integer.")

    def test_add_a_grade__raise_exception_DisciplineIdError__discipline_id_contains_letters(self):
        with self.assertRaises(DisciplineIdError) as exc:
            self.__grade_service.add_a_grade("12","l3","7")
        self.assertEqual(str(exc.exception), "Discipline id must be a positive integer.")

    def test_add_a_grade__raise_exception_StudentIdNotFoundError__student_id_is_not_in_the_students_list(self):
        with self.assertRaises(StudentIdNotFoundError) as exc:
            self.__grade_service.add_a_grade("30","13","8")
        self.assertEqual(str(exc.exception), "Student id wasn't found.")

    def test_add_a_grade__raise_exception_DisciplineIdNotFoundError__discipline_id_is_not_in_the_disciplines_list(self):
        with self.assertRaises(DisciplineIdNotFoundError) as exc:
            self.__grade_service.add_a_grade("13", "30", "7")
        self.assertEqual(str(exc.exception), "Discipline id wasn't found.")

    """
        TESTS FOR REMOVE
    """

    def test_remove_grades_for_a_student__with_valid_data__is_going_to_remove_the_grades_for_a_given_student_id(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("13","15","7")
        self.__grade_service.remove_grades_for_a_student("11")
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(13, 15, 7))
        self.assertEqual(self.__grade_service.list_of_grades(), list_of_expected_grades)

    def test_remove_grades_for_a_discipline__with_valid_data__is_going_to_remove_the_grades_for_a_given_discipline_id(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("13","15","7")
        self.__grade_service.add_a_grade("14","12","7")
        self.__grade_service.remove_grades_for_a_discipline("12")
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(11, 13, 8))
        list_of_expected_grades.append(Grade(13, 15, 7))
        self.assertEqual(self.__grade_service.list_of_grades(), list_of_expected_grades)

    def test_remove_a_grade_for_a_student_at_a_discipline__with_valid_data__is_going_to_remove_a_given_grade_for_a_given_discipline_for_a_given_student(self):
        self.__grade_service.add_a_grade("11", "12", "10")
        self.__grade_service.add_a_grade("11", "13", "8")
        self.__grade_service.add_a_grade("13", "15", "7")
        self.__grade_service.add_a_grade("14", "12", "7")
        self.__grade_service.remove_a_grade_for_a_student_at_a_discipline("13", "15", "7")
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(11, 12, 10))
        list_of_expected_grades.append(Grade(11, 13, 8))
        list_of_expected_grades.append(Grade(14, 12, 7))
        self.assertEqual(self.__grade_service.list_of_grades(), list_of_expected_grades)


    """
        TESTS FOR STATISTICS
    """

    def test_statistics_for_all_students_failing_at_one_or_more_disciplines__with_valid_data__is_going_to_return_a_list_with_all_the_students_that_failed_at_least_one_discipline(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("13","15","3")
        self.__grade_service.add_a_grade("14","12","7")
        list_of_expected_student = []
        list_of_expected_student.append(13)
        self.assertEqual(self.__grade_service.statistics_for_all_students_failing_at_one_or_more_disciplines(), list_of_expected_student)

    def test_compute_aggregated_average_for_a_student_at_a_given_discipline__with_valid_data__is_going_to_return_the_aggregated_average_for_a_student_at_a_discipline(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("11","13","6")
        self.__grade_service.add_a_grade("11","13","10")
        self.__grade_service.add_a_grade("13","15","3")
        self.__grade_service.add_a_grade("14","12","7")
        self.assertEqual(self.__grade_service.compute_aggregated_average_for_a_student_at_a_given_discipline("11", "13"), 8)
        self.assertEqual(self.__grade_service.compute_aggregated_average_for_a_student_at_a_given_discipline("11","14"), 0)

    def test_compute_aggregated_average_for_a_student__with_valid_data__is_going_to_return_the_aggregated_average_for_a_student(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("11","13","6")
        self.__grade_service.add_a_grade("11","13","10")
        self.__grade_service.add_a_grade("13","15","3")
        self.__grade_service.add_a_grade("14","12","7")
        self.assertEqual(self.__grade_service.compute_aggregated_average_for_a_student("11"), 9)
        self.assertEqual(self.__grade_service.compute_aggregated_average_for_a_student("12"), 0)

    def test_all_students_that_have_at_least_a_grade__with_valid_data__is_going_to_return_the_set_with_all_students_id_that_have_at_least_a_grade(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("11","13","6")
        self.__grade_service.add_a_grade("11","13","10")
        self.__grade_service.add_a_grade("13","15","3")
        self.__grade_service.add_a_grade("14","12","7")
        list_of_expected_students = []
        list_of_expected_students.append(11)
        list_of_expected_students.append(13)
        list_of_expected_students.append(14)
        self.assertEqual(self.__grade_service.all_students_that_have_at_least_a_grade(), list_of_expected_students)

    def test_statistics_for_students_with_best_school_situation__with_valid_data__is_going_to_return_a_sorted_list_with_students_id_that_have_the_biggest_aggregated_average(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("11","13","6")
        self.__grade_service.add_a_grade("11","13","10")
        self.__grade_service.add_a_grade("13","15","3")
        self.__grade_service.add_a_grade("12","15","10")
        self.__grade_service.add_a_grade("14","12","7")
        list_of_expected_students = []
        list_of_expected_students.append(12)
        list_of_expected_students.append(11)
        list_of_expected_students.append(14)
        list_of_expected_students.append(13)
        self.assertEqual(self.__grade_service.statistics_for_students_with_best_school_situation(), list_of_expected_students)

    def test_all_disciplines_that_have_at_least_a_grade__with_valid_data__is_going_to_return_the_list_of_all_disciplines_with_at_least_a_grade(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("11","13","6")
        self.__grade_service.add_a_grade("11","13","10")
        self.__grade_service.add_a_grade("13","15","3")
        self.__grade_service.add_a_grade("12","15","10")
        self.__grade_service.add_a_grade("14","12","7")
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(12)
        list_of_expected_disciplines.append(13)
        list_of_expected_disciplines.append(15)
        self.assertEqual(self.__grade_service.all_disciplines_that_have_at_least_a_grade(), list_of_expected_disciplines)

    def test_compute_average_grade_for_a_discipline__with_valid_data__is_going_to_return_the_average_grade_for_a_discipline(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("11","13","6")
        self.__grade_service.add_a_grade("11","13","10")
        self.__grade_service.add_a_grade("13","15","3")
        self.__grade_service.add_a_grade("12","15","10")
        self.__grade_service.add_a_grade("14","12","7")
        self.assertEqual(self.__grade_service.compute_average_grade_for_a_discipline("12"), 8.5)
        self.assertEqual(self.__grade_service.compute_average_grade_for_a_discipline("17"), 0)

    def test_statistics_for_all_disciplines_with_at_least_one_grade__with_valid_data__is_going_to_return_all_the_disciplines_id_with_at_least_a_grade(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("11","13","6")
        self.__grade_service.add_a_grade("11","13","10")
        self.__grade_service.add_a_grade("13","15","3")
        self.__grade_service.add_a_grade("12","15","10")
        self.__grade_service.add_a_grade("14","12","7")
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(12)
        list_of_expected_disciplines.append(13)
        list_of_expected_disciplines.append(15)
        self.assertEqual(self.__grade_service.statistics_for_all_disciplines_with_at_least_one_grade(), list_of_expected_disciplines)

    """
        TESTS FOR LENGTH
    """

    def test_length_of_grades__with_valid_data__is_going_to_return_the_length_of_grades_list(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("13","15","7")
        self.assertEqual(self.__grade_service.length_of_grades(), 3)

    """
        TESTS FOR INDEX
    """

    def test_get_index_of_grades_list__with_valid_data__is_going_to_return_the_indexth_element_from_grades_list(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("13","15","7")
        self.assertEqual(self.__grade_service.get_index_of_grades_list(2), Grade(13, 15, 7))

    """
        TESTS FOR LIST
    """

    def test_get_all_grades_for_a_given_student__with_valid_data__is_going_to_return_a_list_with_all_the_grades_for_a_given_student(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("11","13","6")
        self.__grade_service.add_a_grade("11","13","10")
        self.__grade_service.add_a_grade("13","15","3")
        self.__grade_service.add_a_grade("12","15","10")
        self.__grade_service.add_a_grade("14","12","7")
        new_list_with_grades = self.__grade_service.get_all_grades_for_a_given_student("11")
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(11, 12, 10))
        list_of_expected_grades.append(Grade(11, 13, 8))
        list_of_expected_grades.append(Grade(11, 13, 6))
        list_of_expected_grades.append(Grade(11, 13, 10))

        self.assertEqual(new_list_with_grades, list_of_expected_grades)

    def test_get_all_grades_for_a_given_discipline__with_valid_data__is_going_to_return_a_list_with_all_the_grade_for_a_given_discipline(self):
        self.__grade_service.add_a_grade("11","12","10")
        self.__grade_service.add_a_grade("11","13","8")
        self.__grade_service.add_a_grade("11","13","6")
        self.__grade_service.add_a_grade("11","13","10")
        self.__grade_service.add_a_grade("13","15","3")
        self.__grade_service.add_a_grade("12","15","10")
        self.__grade_service.add_a_grade("14","12","7")
        new_list_with_grades = self.__grade_service.get_all_grades_for_a_given_discipline("12")
        list_of_expected_grades = []
        list_of_expected_grades.append(Grade(11, 12, 10))
        list_of_expected_grades.append(Grade(14, 12, 7))
        self.assertEqual(list_of_expected_grades, new_list_with_grades)