import unittest
from domain.Discipline import Discipline
from repository.DisciplineRepository import DisciplineRepository
from repository.GradeRepository import GradeRepository
from services.DisciplinesService import DisciplinesService
from domain.Validators import DisciplineIdError

class TestDisciplineService(unittest.TestCase):

    def setUp(self) -> None:
        self.__discipline_repository = DisciplineRepository()
        self.__grade_repository = GradeRepository()
        self.__discipline_services = DisciplinesService(self.__discipline_repository, self.__grade_repository)

    def tearDown(self) -> None:
        pass

    """
        TESTS FOR ADD
    """

    def test_add_a_discipline__with_valid_data__is_going_to_be_added_in_the_class(self):
        self.__discipline_services.add_a_discipline("15","FP")
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(15,"FP"))
        self.assertEqual(self.__discipline_services.list_of_disciplines(), list_of_expected_disciplines)

    def test_add_a_discipline__raise_exception_DisciplineIdError__discipline_id_is_not_a_number(self):
        with self.assertRaises(DisciplineIdError) as exc:
            self.__discipline_services.add_a_discipline("9dw8a", "FP")
        self.assertEqual(str(exc.exception), "Discipline id has to be a positive integer.")

    """
        TESTS FOR SEARCH
    """

    def test_search_a_discipline_by_discipline_ID__with_valid_data__is_going_to_return_a_list_with_the_disciplines_with_that_id(self):
        self.__discipline_services.add_a_discipline("15", "FP")
        self.__discipline_services.add_a_discipline("17", "Math")
        self.__discipline_services.add_a_discipline("19", "Logic")
        new_list_with_the_searched_disciplines_by_id = self.__discipline_services.search_a_discipline_by_discipline_ID("17")
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(17,"Math"))
        self.assertEqual(new_list_with_the_searched_disciplines_by_id, list_of_expected_disciplines)

    def test_search_a_discipline_by_discipline_ID__raise_exception_DisciplineIdError__discipline_id_contains_letters(self):
        self.__discipline_services.add_a_discipline("15", "FP")
        self.__discipline_services.add_a_discipline("17", "Math")
        self.__discipline_services.add_a_discipline("19", "Logic")
        with self.assertRaises(DisciplineIdError) as exc:
            self.__discipline_services.search_a_discipline_by_discipline_ID("l5")
        self.assertEqual(str(exc.exception), "Discipline id must be a positive integer.")

    def test_search_a_discipline_by_name__with_valid_data__is_going_to_return_a_list_with_the_disciplines_that_contains_that_name(self):
        self.__discipline_services.add_a_discipline("15", "FP")
        self.__discipline_services.add_a_discipline("17", "Math")
        self.__discipline_services.add_a_discipline("19", "Logic")
        self.__discipline_services.add_a_discipline("21", "Physics")
        new_list_with_the_searched_disciplines_by_name = self.__discipline_services.search_a_discipline_by_name("ic")
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(19,"Logic"))
        list_of_expected_disciplines.append(Discipline(21,"Physics"))
        self.assertEqual(new_list_with_the_searched_disciplines_by_name, list_of_expected_disciplines)

    """
        TESTS FOR UPDATE
    """

    def test_update_a_discipline_by_id__with_valid_data__is_going_to_update_the_name_for_the_discipline_with_that_given_id(self):
        self.__discipline_services.add_a_discipline("15", "FP")
        self.__discipline_services.add_a_discipline("17", "Math")
        self.__discipline_services.add_a_discipline("19", "Logic")
        self.__discipline_services.update_a_discipline_by_id("15", "History")
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(15, "History"))
        list_of_expected_disciplines.append(Discipline(17, "Math"))
        list_of_expected_disciplines.append(Discipline(19, "Logic"))
        self.assertEqual(self.__discipline_services.list_of_disciplines(), list_of_expected_disciplines)

    def test_update_a_discipline_by_name__with_valid_data__is_going_to_update_the_id_for_the_discipline_with_that_given_name(self):
        self.__discipline_services.add_a_discipline("15", "FP")
        self.__discipline_services.add_a_discipline("17", "Math")
        self.__discipline_services.add_a_discipline("19", "Logic")
        self.__discipline_services.update_a_discipline_by_name("FP","20")
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(20, "FP"))
        list_of_expected_disciplines.append(Discipline(17, "Math"))
        list_of_expected_disciplines.append(Discipline(19, "Logic"))
        self.assertEqual(self.__discipline_services.list_of_disciplines(), list_of_expected_disciplines)

    """
        TESTS FOR REMOVE
    """

    def test_remove_a_discipline__with_valid_data__is_going_to_remove_the_discipline_from_the_class(self):
        self.__discipline_services.add_a_discipline("15", "FP")
        self.__discipline_services.add_a_discipline("17", "Math")
        self.__discipline_services.add_a_discipline("19", "Logic")
        self.__discipline_services.remove_a_discipline("19")
        list_of_expected_disciplines = []
        list_of_expected_disciplines.append(Discipline(15, "FP"))
        list_of_expected_disciplines.append(Discipline(17, "Math"))
        self.assertEqual(self.__discipline_services.list_of_disciplines(), list_of_expected_disciplines)

    """
        TESTS FOR LENGTH
    """

    def test_length_of_disciplines__with_valid_data__is_going_to_return_the_length_of_disciplines_list(self):
        self.__discipline_services.add_a_discipline("15", "FP")
        self.__discipline_services.add_a_discipline("17", "Math")
        self.__discipline_services.add_a_discipline("19", "Logic")
        self.assertEqual(self.__discipline_services.length_of_disciplines(), 3)

    """
        TESTS FOR INDEX
    """

    def test_get_index_of_disciplines_list__with_valid_data__is_going_to_return_the_indexth_element_from_the_disciplines_list(self):
        self.__discipline_services.add_a_discipline("15", "FP")
        self.__discipline_services.add_a_discipline("17", "Math")
        self.__discipline_services.add_a_discipline("19", "Logic")
        self.assertEqual(self.__discipline_services.get_index_of_disciplines_list(1), Discipline(17,"Math"))