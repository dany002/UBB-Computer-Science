import unittest

from Repository.BoardRepository import BoardRepository
from domain.Validators import PlaneDoesntFit, ThereIsAlreadyAPlaneThere


class TestBoardRepository(unittest.TestCase):
    def setUp(self) -> None:
        self.__board_repository = BoardRepository()

    def tearDown(self) -> None:
        pass

    def test_is_there_place_for_a_plane_with_up_cabin__with_valid_data__is_going_to_return_True(self):
        self.assertEqual(self.__board_repository.is_there_place_for_a_plane_with_up_cabin(4, 5), True)

    def test_is_there_place_for_a_plane_with_up_cabin__raise_exception_PlaneDoesntFit__it_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_repository.is_there_place_for_a_plane_with_up_cabin(8, 1)

    def test_is_there_place_for_a_plane_with_up_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_repository.up_cabin(4, 4)
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_repository.is_there_place_for_a_plane_with_up_cabin(5, 3)

    def test_up_cabin__with_valid_data__is_going_to_create_the_plane_by_placing_1_where_the_plane_is(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_repository.up_cabin(4, 4)
        self.assertEqual(self.__board_repository.get_all(), result_list)

    def test_up_cabin__raise_exception_PlaneDoesntFit__the_plane_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_repository.up_cabin(8, 1)

    def test_up_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_repository.up_cabin(4, 4)
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_repository.up_cabin(5, 3)

    def test_is_there_place_for_a_plane_with_down_cabin__with_valid_data__is_going_to_return_True(self):
        self.assertEqual(self.__board_repository.is_there_place_for_a_plane_with_down_cabin(4, 5), True)

    def test_is_there_place_for_a_plane_with_down_cabin__raise_exception_PlaneDoesntFit__it_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_repository.is_there_place_for_a_plane_with_down_cabin(1, 8)

    def test_is_there_place_for_a_plane_with_down_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_repository.down_cabin(4, 4)
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_repository.is_there_place_for_a_plane_with_down_cabin(5, 3)

    def test_down_cabin__with_valid_data__is_going_to_create_the_plane_by_placing_1_where_the_plane_is(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_repository.down_cabin(4, 4)
        self.assertEqual(self.__board_repository.get_all(), result_list)

    def test_down_cabin__raise_exception_PlaneDoesntFit__it_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_repository.down_cabin(1, 8)

    def test_down_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_repository.down_cabin(4, 4)
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_repository.down_cabin(5, 3)

    def test_is_there_place_for_a_plane_with_left_cabin__with_valid_data__is_going_to_return_True(self):
        self.assertEqual(self.__board_repository.is_there_place_for_a_plane_with_left_cabin(4, 5), True)

    def test_is_there_place_for_a_plane_with_left_cabin__raise_exception_PlaneDoesntFit__it_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_repository.is_there_place_for_a_plane_with_left_cabin(1, 8)

    def test_is_there_place_for_a_plane_with_left_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_repository.left_cabin(4, 4)
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_repository.is_there_place_for_a_plane_with_left_cabin(5, 3)

    def test_left_cabin__with_valid_data__is_going_to_create_the_plane_by_placing_1_where_the_plane_is(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_repository.left_cabin(4, 4)
        self.assertEqual(self.__board_repository.get_all(), result_list)

    def test_left_cabin__raise_exception_PlaneDoesntFit__it_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_repository.left_cabin(1, 8)

    def test_left_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_repository.left_cabin(4, 4)
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_repository.left_cabin(5, 3)

    def test_is_there_place_for_a_plane_with_right_cabin__with_valid_data__is_going_to_return_True(self):
        self.assertEqual(self.__board_repository.is_there_place_for_a_plane_with_right_cabin(4, 5), True)

    def test_is_there_place_for_a_plane_with_right_cabin__raise_exception_PlaneDoesntFit__it_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_repository.is_there_place_for_a_plane_with_right_cabin(1, 8)

    def test_is_there_place_for_a_plane_with_right_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_repository.right_cabin(4, 4)
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_repository.is_there_place_for_a_plane_with_right_cabin(5, 3)

    def test_right_cabin__with_valid_data__is_going_to_create_the_plane_by_placing_1_where_the_plane_is(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                        [0, 1, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_repository.right_cabin(4, 4)
        self.assertEqual(self.__board_repository.get_all(), result_list)

    def test_right_cabin__raise_exception_PlaneDoesntFit__it_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_repository.right_cabin(1, 8)

    def test_right_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_repository.right_cabin(4, 4)
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_repository.right_cabin(5, 3)

    def test_plane_found_right_cabin__with_valid_data__is_going_to_put_x_where_was_the_plane_with_the_given_cabin(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 'x', 0, 0, 0, 0, 0, 0],
                       [0, 'x', 0, 'x', 0, 0, 0, 0, 0, 0], [0, 'x', 'x', 'x', 'x', 0, 0, 0, 0, 0],
                       [0, 'x', 0, 'x', 0, 0, 0, 0, 0, 0], [0, 0, 0, 'x', 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_repository.right_cabin(4, 4)
        self.__board_repository.plane_found_right_cabin(4, 4)
        self.assertEqual(self.__board_repository.get_all(), result_list)

    def test_plane_found_left_cabin__with_valid_data__is_going_to_put_x_where_was_the_plane_with_the_given_cabin(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 'x', 0, 0, 0, 0], [0, 0, 0, 0, 0, 'x', 0, 'x', 0, 0],
                       [0, 0, 0, 0, 'x', 'x', 'x', 'x', 0, 0], [0, 0, 0, 0, 0, 'x', 0, 'x', 0, 0], [0, 0, 0, 0, 0, 'x', 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_repository.left_cabin(4, 4)
        self.__board_repository.plane_found_left_cabin(4, 4)
        self.assertEqual(self.__board_repository.get_all(), result_list)

    def test_plane_found_up_cabin__with_valid_data__is_going_to_put_x_where_was_the_plane_with_the_given_cabin(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 'x', 0, 0, 0, 0, 0], [0, 0, 'x', 'x', 'x', 'x', 'x', 0, 0, 0], [0, 0, 0, 0, 'x', 0, 0, 0, 0, 0], [0, 0, 0, 'x', 'x', 'x', 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_repository.up_cabin(4, 4)
        self.__board_repository.plane_found_up_cabin(4, 4)
        self.assertEqual(self.__board_repository.get_all(), result_list)

    def test_plane_found_down_cabin__with_valid_data__is_going_to_put_x_where_was_the_plane_with_the_given_cabin(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 'x', 'x', 'x', 0, 0, 0, 0], [0, 0, 0, 0, 'x', 0, 0, 0, 0, 0], [0, 0, 'x', 'x', 'x', 'x', 'x', 0, 0, 0],
                       [0, 0, 0, 0, 'x', 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_repository.down_cabin(4, 4)
        self.__board_repository.plane_found_down_cabin(4, 4)
        self.assertEqual(self.__board_repository.get_all(), result_list)

    def test_guess_the_plane__with_valid_data__is_going_to_put_y_if_that_element_is_a_part_from_plane_but_not_the_cabin(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 'y', 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_repository.left_cabin(4, 4)
        self.__board_repository.guess_the_plane(4, 5)
        self.__board_repository.guess_the_plane(7, 8)
        self.assertEqual(self.__board_repository.get_all(), result_list)

    def test_get_element__with_valid_data__is_going_to_return_the_element_from_the_list_with_the_given_coordinates(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_repository.left_cabin(4, 4)
        self.assertEqual(self.__board_repository.get_element(4, 5), 1)
        self.assertEqual(self.__board_repository.get_element(7, 8), 0)

    def test_get_row__with_valid_data__is_going_to_return_the_whole_row_from_the_list(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_repository.left_cabin(4, 4)
        self.assertEqual(self.__board_repository.get_row(2), [0, 0, 0, 0, 0, 1, 0, 0, 0, 0])