import unittest

from domain.Student import Student
from repository.StudentRepository import StudentRepository
from repository.RepositoryException import RepositoryException, RepositoryException2

class TestStudentRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.__student_repository = StudentRepository()

    def tearDown(self) -> None:
        pass
    """
        TESTS FOR ADD
    """
    def test_add_a_student__with_valid_data__student_is_going_to_be_added_in_the_class(self):
        list_of_expected_students = []
        list_of_expected_students.append(Student(15,"Dani"))
        self.__student_repository.add_a_student(Student(15,"Dani"))
        self.assertEqual(list_of_expected_students, self.__student_repository.list_of_students())

    def test_add_a_student__raise_exception_RepositoryException__student_id_is_already_taken(self):
        self.__student_repository.add_a_student(Student(15,"Dani"))
        with self.assertRaises(RepositoryException) as re:
            self.__student_repository.add_a_student(Student(15,"Alin"))
        self.assertEqual(str(re.exception), "Student ID is not unique.")

    """
        TESTS FOR REMOVE
    """

    def test_remove_a_student__with_valid_data__student_is_going_to_be_removed_from_the_class(self):
        list_of_expected_students = []
        list_of_expected_students.append(Student(15,"Dani"))
        list_of_expected_students.append(Student(19,"George"))
        self.__student_repository.add_a_student(Student(15,"Dani"))
        self.__student_repository.add_a_student(Student(17,"Alin"))
        self.__student_repository.add_a_student(Student(19,"George"))
        self.__student_repository.remove_a_student(17)
        self.assertEqual(list_of_expected_students, self.__student_repository.list_of_students())

    def test_remove_a_student__raise_exception_RepositoryException__student_id_is_not_found(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        with self.assertRaises(RepositoryException) as re:
            self.__student_repository.remove_a_student(23)
        self.assertEqual(str(re.exception), "Student ID is not found.")



    """
        TESTS FOR SEARCH
    """

    def test_search_a_student_by_student_id__with_valid_data__is_going_to_return_a_list_with_the_student_id_and_name(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        list_of_student_found = []
        list_of_student_found.append(Student(15,"Dani"))
        self.assertEqual(self.__student_repository.search_a_student_by_student_ID(15),list_of_student_found)

    def test_search_a_student_by_student_id__raise_exception_RepositoryException__student_id_is_not_found(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        with self.assertRaises(RepositoryException) as re:
            self.__student_repository.search_a_student_by_student_ID(20)
        self.assertEqual(str(re.exception), "Student id wasn't found.")


    def test_search_a_student_by_name__with_valid_data__is_going_to_return_a_list_with_the_student_id_and_name(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        list_of_student_found = [{'id': 15, 'name': "Dani"}]
        self.assertEqual(self.__student_repository.search_a_student_by_name("Dani"),list_of_student_found)

    def test_search_a_student_by_name__raise_exception_RepositoryException__student_name_is_not_found(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        with self.assertRaises(RepositoryException) as re:
            self.__student_repository.search_a_student_by_name("Bobo")
        self.assertEqual(str(re.exception), "Student name wasn't found.")

    def test_search_a_student_by_name__raise_exception_RepositoryException2__student_name_contains_letters(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        with self.assertRaises(RepositoryException2) as re:
            self.__student_repository.search_a_student_by_name("B0b0")
        self.assertEqual(str(re.exception), "Student name has to contain only letters.")



    """
        TESTS FOR UPDATE
    """

    def test_update_a_student_by_name__with_valid_data__is_going_to_update_the_student_id_for_that_student_name(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        self.__student_repository.update_a_student_by_name("Alin", 23)
        list_of_expected_students = []
        list_of_expected_students.append(Student(15,"Dani"))
        list_of_expected_students.append(Student(23,"Alin"))
        list_of_expected_students.append(Student(19,"George"))
        self.assertEqual(self.__student_repository.list_of_students(), list_of_expected_students)

    def test_update_a_student_by_name__raise_exception_RepositoryException__Student_Id_is_already_taken(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        with self.assertRaises(RepositoryException) as re:
            self.__student_repository.update_a_student_by_name("Alin",19)
        self.assertEqual(str(re.exception), "Student ID is already taken.")

    def test_update_a_student_by_name__raise_exception_RepositoryException2__There_is_no_name_to_be_updated(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        with self.assertRaises(RepositoryException2) as re:
            self.__student_repository.update_a_student_by_name("Bobo",30)
        self.assertEqual(str(re.exception), "There is no name to be updated.")

    def test_update_a_student_by_id__with_valid_data__is_going_to_update_the_name_for_the_student_with_that_given_id(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        self.__student_repository.update_a_student_by_id(17, "Bobo")
        list_of_expected_students = []
        list_of_expected_students.append(Student(15,"Dani"))
        list_of_expected_students.append(Student(17,"Bobo"))
        list_of_expected_students.append(Student(19,"George"))
        self.assertEqual(self.__student_repository.list_of_students(), list_of_expected_students)

    def test_update_a_student_by_id__raise_exception_RepositoryException__there_is_no_id_to_be_updated(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        with self.assertRaises(RepositoryException) as re:
            self.__student_repository.update_a_student_by_id(20, "Bobo")
        self.assertEqual(str(re.exception), "The given id is not in the list of students.")

    """
        TESTS FOR LENGTH
    """

    def test_length_of_students_list__with_valid_data__is_going_to_return_the_length_of_the_students_list(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        self.assertEqual(self.__student_repository.length_of_students(), 3)

    """
        TESTS FOR INDEX
    """

    def test_get_index_of_students_list__with_valid_data__is_going_to_return_the_indexth_element_of_the_students_list(self):
        self.__student_repository.add_a_student(Student(15, "Dani"))
        self.__student_repository.add_a_student(Student(17, "Alin"))
        self.__student_repository.add_a_student(Student(19, "George"))
        self.assertEqual(self.__student_repository.get_index_of_students_list(1), Student(17,"Alin"))