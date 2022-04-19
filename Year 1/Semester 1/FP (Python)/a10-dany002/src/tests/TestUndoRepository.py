import unittest

from repository.UndoRepository import UndoRepository
from repository.RepositoryException import RepositoryException

class TestUndoRepository(unittest.TestCase):

    def setUp(self) -> None:
        self.__undo_repository = UndoRepository()

    def tearDown(self) -> None:
        pass

    def test_add__with_valid_data__is_going_to_add_in_the_class(self):
        self.__undo_repository.add(17)
        list_of_expected_command = []
        list_of_expected_command.append(17)
        self.assertEqual(self.__undo_repository.get_all(), list_of_expected_command)

    def test_remove_last_action__with_valid_data__is_going_to_remove_the_last_action_from_the_class(self):
        self.__undo_repository.add(13)
        self.__undo_repository.add(15)
        self.__undo_repository.add(17)
        self.__undo_repository.remove_last_action()
        list_of_expected_command = []
        list_of_expected_command.append(13)
        list_of_expected_command.append(15)
        self.assertEqual(self.__undo_repository.get_all(), list_of_expected_command)

    def test_remove_last_action__raise_exception_RepositoryException__list_is_empty(self):
        with self.assertRaises(RepositoryException) as re:
            self.__undo_repository.remove_last_action()
        self.assertEqual(str(re.exception), "List is empty.")

    def test_get_by_index__with_valid_data__is_going_to_return_the_indexth_element_from_the_list(self):
        self.__undo_repository.add(13)
        self.__undo_repository.add(15)
        self.__undo_repository.add(17)
        self.assertEqual(self.__undo_repository.get_by_index(1), 15)

    def test_length__with_valid_data__is_going_to_return_the_length_of_the_list(self):
        self.__undo_repository.add(13)
        self.__undo_repository.add(15)
        self.__undo_repository.add(17)
        self.assertEqual(self.__undo_repository.__len__(), 3)

    def test_equality__with_valid_data__is_going_to_return_False_the_lists_are_not_equal(self):
        self.__undo_repository.add(13)
        self.__undo_repository.add(15)
        list_of_elements = []
        list_of_elements.append(13)
        list_of_elements.append(14)
        true_or_false = self.__undo_repository.__eq__(list_of_elements)
        self.assertEqual(true_or_false, False)

    def test_str__with_valid_data__is_going_to_print_the_list(self):
        self.__undo_repository.add(13)
        self.__undo_repository.add(14)
        self.assertEqual(self.__undo_repository.get_all().__str__(), "[13, 14]")

    def test_eqaulity__with_valid_data__is_going_to_return_True_the_lists_are_equal(self):
        self.__undo_repository.add(13)
        self.__undo_repository.add(14)
        self.__undo_repository.add(15)
        list_of_expected_elements = []
        list_of_expected_elements.append(13)
        list_of_expected_elements.append(14)
        list_of_expected_elements.append(15)
        self.assertEqual(self.__undo_repository.get_all(), list_of_expected_elements)