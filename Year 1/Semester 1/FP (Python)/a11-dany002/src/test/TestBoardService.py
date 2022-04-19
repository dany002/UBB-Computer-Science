import unittest
from domain.Validators import NotNumber, NotInTheRangeAJ, NotInTheRange, PlaneDoesntFit, ThereIsAlreadyAPlaneThere, IsNumber
from Repository.BoardRepository import BoardRepository
from Services.BoardService import BoardService

class TestBoardService(unittest.TestCase):
    def setUp(self) -> None:
        self.__board_service = BoardService(BoardRepository())

    def test_up_cabin__with_valid_data__is_going_to_mark_with_1_the_place_where_will_be_the_plane(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_service.up_cabin("5", "E")
        self.assertEqual(self.__board_service.get_all(), result_list)

    def test_up_cabin__raise_exception_NotNumber__the_first_coordinate_is_not_a_number(self):
        with self.assertRaises(NotNumber):
            self.__board_service.up_cabin("1o", "D")

    def test_up_cabin__raise_exception_NotInTheRange__the_first_coordinate_is_not_between_1_and_10(self):
        with self.assertRaises(NotInTheRange):
            self.__board_service.up_cabin("11", "D")

    def test_up_cabin__raise_exception_IsNumber__the_second_coordinate_is_a_number(self):
        with self.assertRaises(IsNumber):
            self.__board_service.up_cabin("5", "4")
    
    def test_up_cabin__raise_exception_NotInTheRangeAJ__the_second_coordinate_is_not_between_A_and_J(self):
        with self.assertRaises(NotInTheRangeAJ):
            self.__board_service.up_cabin("5", "L")

    def test_up_cabin__raise_exception_PlaneDoesntFit__it_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_service.up_cabin("1", "H")

    def test_up_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_service.up_cabin("5", "E")
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_service.up_cabin("6", "F")

    def test_down_cabin__with_valid_data__is_going_to_mark_with_1_the_place_where_will_be_the_plane(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_service.down_cabin("5", "E")
        self.assertEqual(self.__board_service.get_all(), result_list)

    def test_down_cabin__raise_exception_NotNumber__the_first_coordinate_is_not_a_number(self):
        with self.assertRaises(NotNumber):
            self.__board_service.down_cabin("1o", "D")

    def test_down_cabin__raise_exception_NotInTheRange__the_first_coordinate_is_not_between_1_and_10(self):
        with self.assertRaises(NotInTheRange):
            self.__board_service.down_cabin("11", "D")

    def test_down_cabin__raise_exception_IsNumber__the_second_coordinate_is_a_number(self):
        with self.assertRaises(IsNumber):
            self.__board_service.down_cabin("5", "4")

    def test_down_cabin__raise_exception_NotInTheRangeAJ__the_second_coordinate_is_not_between_A_and_J(self):
        with self.assertRaises(NotInTheRangeAJ):
            self.__board_service.down_cabin("5", "L")

    def test_down_cabin__raise_exception_PlaneDoesntFit__it_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_service.down_cabin("1", "H")

    def test_down_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_service.down_cabin("5", "E")
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_service.down_cabin("6", "F")


    def test_left_cabin__with_valid_data__is_going_to_mark_with_1_the_place_where_will_be_the_plane(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_service.left_cabin("5", "E")
        self.assertEqual(self.__board_service.get_all(), result_list)

    def test_left_cabin__raise_exception_NotNumber__the_first_coordinate_is_not_a_number(self):
        with self.assertRaises(NotNumber):
            self.__board_service.left_cabin("1o", "D")

    def test_left_cabin__raise_exception_NotInTheRange__the_first_coordinate_is_not_between_1_and_10(self):
        with self.assertRaises(NotInTheRange):
            self.__board_service.left_cabin("11", "D")

    def test_left_cabin__raise_exception_IsNumber__the_second_coordinate_is_a_number(self):
        with self.assertRaises(IsNumber):
            self.__board_service.left_cabin("5", "4")

    def test_left_cabin__raise_exception_NotInTheRangeAJ__the_second_coordinate_is_not_between_A_and_J(self):
        with self.assertRaises(NotInTheRangeAJ):
            self.__board_service.left_cabin("5", "L")

    def test_left_cabin__raise_exception_PlaneDoesntFit__it_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_service.left_cabin("9", "H")

    def test_left_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_service.left_cabin("5", "E")
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_service.left_cabin("6", "F")

    def test_right_cabin__with_valid_data__is_going_to_mark_with_1_the_place_where_will_be_the_plane(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_service.right_cabin("5", "E")
        self.assertEqual(self.__board_service.get_all(), result_list)

    def test_right_cabin__raise_exception_NotNumber__the_first_coordinate_is_not_a_number(self):
        with self.assertRaises(NotNumber):
            self.__board_service.right_cabin("1o", "D")

    def test_right_cabin__raise_exception_NotInTheRange__the_first_coordinate_is_not_between_1_and_10(self):
        with self.assertRaises(NotInTheRange):
            self.__board_service.right_cabin("11", "D")

    def test_right_cabin__raise_exception_IsNumber__the_second_coordinate_is_a_number(self):
        with self.assertRaises(IsNumber):
            self.__board_service.right_cabin("5", "4")

    def test_right_cabin__raise_exception_NotInTheRangeAJ__the_second_coordinate_is_not_between_A_and_J(self):
        with self.assertRaises(NotInTheRangeAJ):
            self.__board_service.right_cabin("5", "L")

    def test_right_cabin__raise_exception_PlaneDoesntFit__it_doesnt_fit_in_the_board(self):
        with self.assertRaises(PlaneDoesntFit):
            self.__board_service.right_cabin("1", "H")

    def test_right_cabin__raise_exception_ThereIsAlreadyAPlaneThere__cant_add_a_plane_over_another(self):
        self.__board_service.right_cabin("5", "E")
        with self.assertRaises(ThereIsAlreadyAPlaneThere):
            self.__board_service.right_cabin("6", "F")

    def test_how_many_planes_are_on_board__with_valid_data__is_going_to_return_the_number_of_planes(self):
        self.assertEqual(self.__board_service.how_many_planes_are_on_board(), 0)
        self.__board_service.left_cabin("1","C")
        self.assertEqual(self.__board_service.how_many_planes_are_on_board(), 1)
        self.__board_service.right_cabin("10", "C")
        self.assertEqual(self.__board_service.how_many_planes_are_on_board(), 2)
        self.__board_service.down_cabin("4", "J")
        self.assertEqual(self.__board_service.how_many_planes_are_on_board(), 3)


    def test_plane_found__with_valid_data__is_going_to_mark_with_x_the_plane_with_the_cabin_that_was_guessed(self):
        self.__board_service.left_cabin("1", "C")
        self.__board_service.right_cabin("10", "C")
        self.__board_service.down_cabin("4", "J")
        self.__board_service.up_cabin("8", "F")
        result_list =  [[0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                        [1, 1, 1, 1, 0, 0, 1, 1, 1, 1],
                        [0, 1, 0, 1, 0, 0, 1, 0, 1, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.__board_service.get_all(), result_list)
        self.__board_service.plane_found(0, 2, "left")

        result_list =  [[0, 'x', 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 'x', 0, 'x', 0, 0, 1, 0, 1, 0],
                        ['x', 'x', 'x', 'x', 0, 0, 1, 1, 1, 1],
                        [0, 'x', 0, 'x', 0, 0, 1, 0, 1, 0],
                        [0, 'x', 0, 0, 0, 0, 0, 0, 1, 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.__board_service.get_all(), result_list)
        self.__board_service.plane_found(9, 2, "right")
        result_list =  [[0, 'x', 0, 0, 0, 0, 0, 0, 'x', 0],
                        [0, 'x', 0, 'x', 0, 0, 'x', 0, 'x', 0],
                        ['x', 'x', 'x', 'x', 0, 0, 'x', 'x', 'x', 'x'],
                        [0, 'x', 0, 'x', 0, 0, 'x', 0, 'x', 0],
                        [0, 'x', 0, 0, 0, 0, 0, 0, 'x', 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0],
                        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.__board_service.get_all(), result_list)

        self.__board_service.plane_found(3, 9, "down")
        result_list =  [[0, 'x', 0, 0, 0, 0, 0, 0, 'x', 0],
                        [0, 'x', 0, 'x', 0, 0, 'x', 0, 'x', 0],
                        ['x', 'x', 'x', 'x', 0, 0, 'x', 'x', 'x', 'x'],
                        [0, 'x', 0, 'x', 0, 0, 'x', 0, 'x', 0],
                        [0, 'x', 0, 0, 0, 0, 0, 0, 'x', 0],
                        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 'x', 'x', 'x', 1, 1, 1, 1, 1],
                        [0, 0, 0, 'x', 0, 0, 0, 1, 0, 0],
                        [0, 'x', 'x', 'x', 'x', 'x', 1, 1, 1, 0],
                        [0, 0, 0, 'x', 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.__board_service.get_all(), result_list)

        self.__board_service.plane_found(7, 5, "up")
        result_list =  [[0, 'x', 0, 0, 0, 0, 0, 0, 'x', 0],
                        [0, 'x', 0, 'x', 0, 0, 'x', 0, 'x', 0],
                        ['x', 'x', 'x', 'x', 0, 0, 'x', 'x', 'x', 'x'],
                        [0, 'x', 0, 'x', 0, 0, 'x', 0, 'x', 0],
                        [0, 'x', 0, 0, 0, 0, 0, 0, 'x', 0],
                        [0, 0, 0, 0, 0, 0, 0, 'x', 0, 0],
                        [0, 0, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
                        [0, 0, 0, 'x', 0, 0, 0, 'x', 0, 0],
                        [0, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 0],
                        [0, 0, 0, 'x', 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.__board_service.get_all(), result_list)

    def test_is_game_won__with_valid_data__is_going_to_return_True_if_there_arent_planes_on_board_anymore_else_False(self):
        self.__board_service.left_cabin("1", "C")
        self.__board_service.right_cabin("10", "C")
        self.__board_service.down_cabin("4", "J")
        self.assertEqual(self.__board_service.is_game_won(), False)
        self.__board_service.plane_found(0, 2, "left")
        self.__board_service.plane_found(9, 3, "right")
        self.__board_service.plane_found(3, 9, "down")
        self.assertEqual(self.__board_service.is_game_won(), True)

    def test_get_element__with_valid_data__is_going_to_return_the_element_from_the_list_with_the_given_coordinates(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_service.left_cabin("5", "E")
        self.assertEqual(self.__board_service.get_element(4, 5), 1)
        self.assertEqual(self.__board_service.get_element(7, 8), 0)

    def test_get_row__with_valid_data__is_going_to_return_the_whole_row_from_the_list(self):
        result_list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        self.__board_service.left_cabin("5", "E")
        self.assertEqual(self.__board_service.get_row(3), [0, 0, 0, 0, 0, 1, 0, 1, 0, 0])

    def test_create_board_for_bot__with_valid_data__is_going_to_create_3_planes_for_the_bot(self):
        for index in range(10):
            BoardService(BoardRepository()).create_board_for_bot()

    def test_guess_the_plane__with_valid_data__is_going_to_mark_all_the_cabin_because_the_cabin_was_hit(self):
        self.__board_service.create_board_for_bot()
        self.__board_service.get_the_list_of_bot_cabin()
        for index in range(10, 110):
            self.__board_service.guess_the_plane(str(index // 10), "A")
            self.__board_service.guess_the_plane(str(index // 10), "B")
            self.__board_service.guess_the_plane(str(index // 10), "C")
            self.__board_service.guess_the_plane(str(index // 10), "D")
            self.__board_service.guess_the_plane(str(index // 10), "E")
            self.__board_service.guess_the_plane(str(index // 10), "F")
            self.__board_service.guess_the_plane(str(index // 10), "G")
            self.__board_service.guess_the_plane(str(index // 10), "H")
            self.__board_service.guess_the_plane(str(index // 10), "I")
            self.__board_service.guess_the_plane(str(index // 10), "J")

    def test_guess_the_plane__raise_exception_NotNumber__the_first_coordinate_is_not_a_number(self):
        with self.assertRaises(NotNumber):
            self.__board_service.guess_the_plane("1o","A")

    def test_guess_the_plane__raise_exception_NotInTheRange__the_first_coordinate_is_not_between_1_and_10(self):
        with self.assertRaises(NotInTheRange):
            self.__board_service.guess_the_plane("13","C")

    def test_guess_the_plane__raise_exception_IsNumber__the_second_coordinate_is_a_number(self):
        with self.assertRaises(IsNumber):
            self.__board_service.guess_the_plane("7","8")

    def test_guess_the_plane__raise_exception_NotInTheRangeAJ__the_second_coordinate_is_not_between_A_and_J(self):
        with self.assertRaises(NotInTheRangeAJ):
            self.__board_service.guess_the_plane("6","M")
