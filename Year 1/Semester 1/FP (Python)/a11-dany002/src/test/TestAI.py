import unittest
from AI.BotMoves import BotMoves
from Services.BoardService import BoardService
from Repository.BoardRepository import BoardRepository


class TestAI(unittest.TestCase):
    def setUp(self) -> None:
        board_repository_for_player = BoardRepository()
        
        self.__board_service_for_player = BoardService(board_repository_for_player)

        self.__BotMoves = BotMoves(self.__board_service_for_player)

    def test_make_move__with_valid_data__is_going_to_make_the_AI_move(self):
        self.__board_service_for_player.left_cabin("1", "C")
        self.__board_service_for_player.right_cabin("10", "C")
        self.__board_service_for_player.down_cabin("4", "J")
        for index in range(85):
            self.__BotMoves.make_move({'first coordinate' : [1, 10, 4], 'second coordinate' : [3, 3, 10], 'position' : ["left", "right", "down"]})
