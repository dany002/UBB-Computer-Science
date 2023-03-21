import unittest
from domain.Student import Student
from repository.StudentRepository import StudentRepository
from repository.GradeRepository import GradeRepository
from services.StudentsService import StudentsService
from domain.Validators import StudentIdError

class TestStudentService(unittest.TestCase):
    def setUp(self) -> None:
        self.__student_repository = StudentRepository()
        self.__grade_repository = GradeRepository()
        self.__student_services = StudentsService(self.__student_repository, self.__grade_repository)

    def tearDown(self) -> None:
        pass

    """
        TESTS FOR ADD
    """

    def test_add_a_student__with_valid_data__is_going_to_be_added_in_the_class(self):
        self.__student_services.add_a_student("13","Dani")
        list_of_expected_student = []
        list_of_expected_student.append(Student(13,"Dani"))
        self.assertEqual(self.__student_services.list_of_students(), list_of_expected_student)

    def test_add_a_student__raise_exception_StudentIdError__student_id_is_not_a_number(self):
        with self.assertRaises(StudentIdError) as exc:
            self.__student_services.add_a_student("l0", "Alin")
        self.assertEqual(str(exc.exception), "Student id must be a positive integer.")

    """
        TESTS FOR SEARCH
    """

    def test_search_a_student_by_student_id__with_valid_data__is_going_to_return_a_list_with_the_students_with_that_id(self):
        self.__student_services.add_a_student("13", "Dani")
        self.__student_services.add_a_student("15", "Alin")
        self.__student_services.add_a_student("17", "George")
        new_list_with_the_searched_student_by_id = self.__student_services.search_a_student_by_student_ID("15")
        list_of_expected_student = []
        list_of_expected_student.append(Student(15,"Alin"))
        self.assertEqual(new_list_with_the_searched_student_by_id, list_of_expected_student)

    def test_search_a_student_by_student_id__raise_exception_StudentIdError__student_id_contains_letters(self):
        self.__student_services.add_a_student("13", "Dani")
        self.__student_services.add_a_student("15", "Alin")
        self.__student_services.add_a_student("17", "George")
        with self.assertRaises(StudentIdError) as exc:
            self.__student_services.search_a_student_by_student_ID("2j")
        self.assertEqual(str(exc.exception), "Student id must be a positive integer.")

    def test_search_a_student_by_name__with_valid_data__is_going_to_return_a_list_with_the_students_that_contain_that_name(self):
        self.__student_services.add_a_student("13", "Dani")
        self.__student_services.add_a_student("15", "Marina")
        self.__student_services.add_a_student("17", "Florina")
        new_list_with_the_searched_student_by_name = self.__student_services.search_a_student_by_name("RiNa")
        list_of_expected_students = []
        list_of_expected_students.append(Student(15, "Marina"))
        list_of_expected_students.append(Student(17, "Florina"))
        self.assertEqual(new_list_with_the_searched_student_by_name, list_of_expected_students)

    """
        TESTS FOR UPDATE
    """

    def test_update_a_student_by_id__with_valid_data__is_going_to_update_the_name_for_the_student_with_that_given_id(self):
        self.__student_services.add_a_student("13", "Dani")
        self.__student_services.add_a_student("15", "Alin")
        self.__student_services.add_a_student("17", "George")
        self.__student_services.update_a_student_by_id("15", "Bobo")
        list_of_expected_students = []
        list_of_expected_students.append(Student(13, "Dani"))
        list_of_expected_students.append(Student(15, "Bobo"))
        list_of_expected_students.append(Student(17, "George"))
        self.assertEqual(self.__student_services.list_of_students(), list_of_expected_students)

    def test_update_a_student_by_name__with_valid_data__is_going_to_update_the_id_for_the_student_with_that_given_name(self):
        self.__student_services.add_a_student("13", "Dani")
        self.__student_services.add_a_student("15", "Alin")
        self.__student_services.add_a_student("17", "George")
        self.__student_services.update_a_student_by_name("Dani","20")
        list_of_expected_students = []
        list_of_expected_students.append(Student(20, "Dani"))
        list_of_expected_students.append(Student(15, "Alin"))
        list_of_expected_students.append(Student(17, "George"))
        self.assertEqual(self.__student_services.list_of_students(), list_of_expected_students)

    """
        TESTS FOR REMOVE
    """

    def test_remove_a_student__with_valid_data__is_going_to_remove_the_student_from_the_class(self):
        self.__student_services.add_a_student("13", "Dani")
        self.__student_services.add_a_student("15", "Alin")
        self.__student_services.add_a_student("17", "George")
        self.__student_services.remove_a_student("15")
        list_of_expected_students = []
        list_of_expected_students.append(Student(13, "Dani"))
        list_of_expected_students.append(Student(17, "George"))
        self.assertEqual(self.__student_services.list_of_students(), list_of_expected_students)

    """
        TESTS FOR LENGTH
    """

    def test_length_of_students__with_valid_data__is_going_to_return_the_length_of_students_list(self):
        self.__student_services.add_a_student("13", "Dani")
        self.__student_services.add_a_student("15", "Alin")
        self.__student_services.add_a_student("17", "George")
        self.assertEqual(self.__student_services.length_of_students(), 3)

    """
        TESTS FOR INDEX
    """

    def test_get_index_of_students_list__with_valid_data__is_going_to_return_the_indexth_element_from_students_list(self):
        self.__student_services.add_a_student("13", "Dani")
        self.__student_services.add_a_student("15", "Alin")
        self.__student_services.add_a_student("17", "George")
        self.assertEqual(self.__student_services.get_index_of_students_list(0), Student(13,"Dani"))