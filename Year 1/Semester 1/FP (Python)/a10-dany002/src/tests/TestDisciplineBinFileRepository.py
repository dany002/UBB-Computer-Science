import unittest

from domain.Discipline import Discipline
from repository.DisciplineBinFileRepository import DisciplineBinFileRepository
from repository.RepositoryException import RepositoryException, RepositoryException2
import os.path

class TestDisciplineBinFileRepository(unittest.TestCase):

    def setUp(self) -> None:
        file_name = "disciplines_bin_test"
        self.__discipline_repository = DisciplineBinFileRepository(file_name)

    def tearDown(self) -> None:
        if os.path.exists("disciplines_bin_test"):
            os.remove("disciplines_bin_test")


    """
        TESTS FOR ADD
    """

    def test_add_a_discipline__with_valid_data__discipline_is_going_to_be_added_in_the_class(self):
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(10,"Math"))
        self.__discipline_repository.add_a_discipline(Discipline(10,"Math"))
        self.assertEqual(self.__discipline_repository.list_of_disciplines(), list_of_expected_disciplines)

    def test_add_a_discipline__raise_exception_RepositoryException__discipline_id_is_already_taken(self):
        self.__discipline_repository.add_a_discipline(Discipline(10, "Math"))
        with self.assertRaises(RepositoryException) as re:
            self.__discipline_repository.add_a_discipline(Discipline(10,"Logic"))
        self.assertEqual(str(re.exception), "Discipline ID is already taken.")


    """
        TESTS FOR REMOVE
    """

    def test_remove_a_discipline__with_valid_data__discipline_is_going_to_be_removed_from_the_class(self):
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(15,"FP"))
        list_of_expected_disciplines.append(Discipline(19,"Math"))
        self.__discipline_repository.add_a_discipline(Discipline(15,"FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17,"Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19,"Math"))

        self.__discipline_repository.remove_a_discipline(17)
        self.assertEqual(list_of_expected_disciplines, self.__discipline_repository.list_of_disciplines())

    def test_remove_a_discipline__raise_exception_RepositoryException__discipline_id_is_not_found(self):
        self.__discipline_repository.add_a_discipline(Discipline(15,"FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17,"Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19,"Math"))
        with self.assertRaises(RepositoryException) as re:
            self.__discipline_repository.remove_a_discipline(23)
        self.assertEqual(str(re.exception), "Discipline ID is not found.")

    """
        TESTS FOR SEARCH
    """

    def test_search_a_discipline_by_discipline_id__with_valid_data__is_going_to_return_a_list_with_the_discipline_id_and_name(self):
        self.__discipline_repository.add_a_discipline(Discipline(15,"FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17,"Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19,"Math"))
        list_of_discipline_found = []
        list_of_discipline_found.append(Discipline(19,"Math"))
        self.assertEqual(self.__discipline_repository.search_a_discipline_by_discipline_ID(19), list_of_discipline_found)

    def test_search_a_discipline_by_discipline_id__raise_exception_RepositoryException__discipline_id_is_not_found(self):
        self.__discipline_repository.add_a_discipline(Discipline(15,"FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17,"Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19,"Math"))
        with self.assertRaises(RepositoryException) as re:
            self.__discipline_repository.search_a_discipline_by_discipline_ID(30)
        self.assertEqual(str(re.exception), "Discipline id is not found.")


    def test_search_a_discipline_by_name__with_valid_data__is_going_to_return_a_list_with_the_discipline_id_and_name(self):
        self.__discipline_repository.add_a_discipline(Discipline(15,"FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17,"Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19,"Math"))
        list_of_discipline_found = [{'id': 15, 'name': "FP"}]
        self.assertEqual(self.__discipline_repository.search_a_discipline_by_name("FP"), list_of_discipline_found)

    def test_search_a_discipline_by_name__raise_exception_RepositoryException__discipline_name_is_not_found(self):
        self.__discipline_repository.add_a_discipline(Discipline(15,"FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17,"Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19,"Math"))
        with self.assertRaises(RepositoryException) as re:
            self.__discipline_repository.search_a_discipline_by_name("Sport")
        self.assertEqual(str(re.exception), "Discipline name is not found.")

    def test_search_a_discipline_by_name__raise_exception_RepositoryException2__discipline_name_contains_letters(self):
        self.__discipline_repository.add_a_discipline(Discipline(15,"FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17,"Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19,"Math"))
        with self.assertRaises(RepositoryException2) as re:
            self.__discipline_repository.search_a_discipline_by_name("123")
        self.assertEqual(str(re.exception), "Discipline name has to contain only letters.")


    """
        TESTS FOR UPDATE
    """

    def test_update_a_discipline_by_name__with_valid_data__is_going_to_update_the_discipline_id_for_that_discipline_name(self):
        self.__discipline_repository.add_a_discipline(Discipline(15, "FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17, "Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19, "Math"))
        self.__discipline_repository.update_a_discipline_by_name("FP",30)
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(30,"FP"))
        list_of_expected_disciplines.append(Discipline(17,"Logic"))
        list_of_expected_disciplines.append(Discipline(19,"Math"))
        self.assertEqual(self.__discipline_repository.list_of_disciplines(), list_of_expected_disciplines)

    def test_update_a_discipline_by_name__raise_exception_RepositoryException__Discipline_id_is_already_taken(self):
        self.__discipline_repository.add_a_discipline(Discipline(15, "FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17, "Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19, "Math"))
        with self.assertRaises(RepositoryException) as re:
            self.__discipline_repository.update_a_discipline_by_name("FP", 17)
        self.assertEqual(str(re.exception), "Discipline ID is already taken.")

    def test_update_a_discipline_by_name_raise_exception_RepositoryException2__there_is_no_name_to_be_updated(self):
        self.__discipline_repository.add_a_discipline(Discipline(15, "FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17, "Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19, "Math"))
        with self.assertRaises(RepositoryException2) as re:
            self.__discipline_repository.update_a_discipline_by_name("Russian", 16)
        self.assertEqual(str(re.exception), "There is no name to be updated.")

    def test_update_a_discipline_by_id__with_valid_data__is_going_to_update_the_name_for_the_discipline_with_that_given_id(self):
        self.__discipline_repository.add_a_discipline(Discipline(15, "FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17, "Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19, "Math"))
        self.__discipline_repository.update_a_discipline_by_id(17, "English")
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(15,"FP"))
        list_of_expected_disciplines.append(Discipline(17,"English"))
        list_of_expected_disciplines.append(Discipline(19,"Math"))
        self.assertEqual(self.__discipline_repository.list_of_disciplines(), list_of_expected_disciplines)

    def test_update_a_discipline_by_id__raise_exception_RepositoryException__there_is_no_id_to_be_updated(self):
        self.__discipline_repository.add_a_discipline(Discipline(15, "FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17, "Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19, "Math"))
        with self.assertRaises(RepositoryException) as re:
            self.__discipline_repository.update_a_discipline_by_id(20,"English")
        self.assertEqual(str(re.exception), "There is no id to be updated.")

    """
        TESTS FOR LENGTH
    """

    def test_length_of_disciplines_list__with_valid_data__is_going_to_return_the_length_of_the_disciplines_list(self):
        self.__discipline_repository.add_a_discipline(Discipline(15, "FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17, "Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19, "Math"))
        self.assertEqual(self.__discipline_repository.length_of_disciplines(), 3)

    """
        TESTS FOR INDEX
    """

    def test_get_index_of_disciplines_list__with_valid_data__is_going_to_return_the_indexth_element_of_the_disciplines_list(self):
        self.__discipline_repository.add_a_discipline(Discipline(15, "FP"))
        self.__discipline_repository.add_a_discipline(Discipline(17, "Logic"))
        self.__discipline_repository.add_a_discipline(Discipline(19, "Math"))
        self.assertEqual(self.__discipline_repository.get_index_of_disciplines_list(1), Discipline(17,"Logic"))