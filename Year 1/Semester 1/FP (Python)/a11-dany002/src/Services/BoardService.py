from domain.Validators import PlaneDoesntFit, ThereIsAlreadyAPlaneThere, NotNumber, NotInTheRangeAJ, CheckIfTheFirstCoordinateIsRight, CheckIfTheSecondCoordinateIsRight, IsNumber, NotInTheRange
import random

class BoardService:
    def __init__(self, board_repository):
        self.__repository = board_repository
        self.__number_of_planes = 0
        self.__bot_cabin = {'first coordinate': [], 'second coordinate': [], 'position': []}

    def up_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        try:
            CheckIfTheFirstCoordinateIsRight.validate(first_coordinate_of_cabin)
        except NotNumber:
            raise NotNumber
        except NotInTheRange:
            raise NotInTheRange
        try:
            CheckIfTheSecondCoordinateIsRight.validate(second_coordinate_of_cabin)
            second_coordinate_of_cabin = second_coordinate_of_cabin.upper()
            second_coordinate_of_cabin = ord(second_coordinate_of_cabin) - 64
            self.__repository.up_cabin(int(second_coordinate_of_cabin) - 1, int(first_coordinate_of_cabin) - 1)
            self.__number_of_planes += 1
        except PlaneDoesntFit:
            raise PlaneDoesntFit
        except ThereIsAlreadyAPlaneThere:
            raise ThereIsAlreadyAPlaneThere
        except NotInTheRangeAJ:
            raise NotInTheRangeAJ
        except IsNumber:
            raise IsNumber

    def down_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        try:
            CheckIfTheFirstCoordinateIsRight.validate(first_coordinate_of_cabin)
        except NotNumber:
            raise NotNumber
        except NotInTheRange:
            raise NotInTheRange

        try:
            CheckIfTheSecondCoordinateIsRight.validate(second_coordinate_of_cabin)
            second_coordinate_of_cabin = second_coordinate_of_cabin.upper()
            second_coordinate_of_cabin = ord(second_coordinate_of_cabin) - 64
            self.__repository.down_cabin(int(second_coordinate_of_cabin) - 1, int(first_coordinate_of_cabin) - 1)
            self.__number_of_planes += 1
        except PlaneDoesntFit:
            raise PlaneDoesntFit
        except ThereIsAlreadyAPlaneThere:
            raise ThereIsAlreadyAPlaneThere
        except NotInTheRangeAJ:
            raise NotInTheRangeAJ
        except IsNumber:
            raise IsNumber

    def left_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        try:
            CheckIfTheFirstCoordinateIsRight.validate(first_coordinate_of_cabin)
        except NotNumber:
            raise NotNumber
        except NotInTheRange:
            raise NotInTheRange

        try:
            CheckIfTheSecondCoordinateIsRight.validate(second_coordinate_of_cabin)
            second_coordinate_of_cabin = second_coordinate_of_cabin.upper()
            second_coordinate_of_cabin = ord(second_coordinate_of_cabin) - 64
            self.__repository.left_cabin(int(second_coordinate_of_cabin) - 1, int(first_coordinate_of_cabin) - 1)
            self.__number_of_planes += 1
        except PlaneDoesntFit:
            raise PlaneDoesntFit
        except ThereIsAlreadyAPlaneThere:
            raise ThereIsAlreadyAPlaneThere
        except NotInTheRangeAJ:
            raise NotInTheRangeAJ
        except IsNumber:
            raise IsNumber

    def right_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        try:
            CheckIfTheFirstCoordinateIsRight.validate(first_coordinate_of_cabin)
        except NotNumber:
            raise NotNumber
        except NotInTheRange:
            raise NotInTheRange

        try:
            CheckIfTheSecondCoordinateIsRight.validate(second_coordinate_of_cabin)
            second_coordinate_of_cabin = second_coordinate_of_cabin.upper()
            second_coordinate_of_cabin = ord(second_coordinate_of_cabin) - 64
            self.__repository.right_cabin(int(second_coordinate_of_cabin) - 1, int(first_coordinate_of_cabin) - 1)
            self.__number_of_planes += 1
        except PlaneDoesntFit:
            raise PlaneDoesntFit
        except ThereIsAlreadyAPlaneThere:
            raise ThereIsAlreadyAPlaneThere
        except NotInTheRangeAJ:
            raise NotInTheRangeAJ
        except IsNumber:
            raise IsNumber

    def how_many_planes_are_on_board(self):
        return self.__number_of_planes

    def create_board_for_bot(self):

        while self.__number_of_planes < 3:
            first_coordinate = random.randint(0, 9)
            second_coordinate = random.randint(0, 9)
            cabin = random.randint(0, 3)
            try:
                if cabin == 0:
                    self.__repository.right_cabin(first_coordinate, second_coordinate)
                    self.__bot_cabin["first coordinate"].append(second_coordinate)
                    self.__bot_cabin["second coordinate"].append(first_coordinate)
                    self.__bot_cabin["position"].append("right")
                    self.__number_of_planes += 1
                elif cabin == 1:
                    self.__repository.left_cabin(first_coordinate, second_coordinate)
                    self.__bot_cabin["first coordinate"].append(second_coordinate)
                    self.__bot_cabin["second coordinate"].append(first_coordinate)
                    self.__bot_cabin["position"].append("left")
                    self.__number_of_planes += 1
                elif cabin == 2:
                    self.__repository.up_cabin(first_coordinate, second_coordinate)
                    self.__bot_cabin["first coordinate"].append(second_coordinate)
                    self.__bot_cabin["second coordinate"].append(first_coordinate)
                    self.__bot_cabin["position"].append("up")
                    self.__number_of_planes += 1
                elif cabin == 3:
                    self.__repository.down_cabin(first_coordinate, second_coordinate)
                    self.__bot_cabin["first coordinate"].append(second_coordinate)
                    self.__bot_cabin["second coordinate"].append(first_coordinate)
                    self.__bot_cabin["position"].append("down")
                    self.__number_of_planes += 1
            except ThereIsAlreadyAPlaneThere:
                pass
            except PlaneDoesntFit:
                pass


    def get_the_list_of_bot_cabin(self):
        return self.__bot_cabin

    def plane_found(self, first_coordinate, second_coordinate, position):
        if position == "left":
            self.__repository.plane_found_left_cabin(second_coordinate, first_coordinate)
            self.__number_of_planes -= 1
        elif position == "right":
            self.__repository.plane_found_right_cabin(second_coordinate, first_coordinate)
            self.__number_of_planes -= 1
        elif position == "up":
            self.__repository.plane_found_up_cabin(second_coordinate, first_coordinate)
            self.__number_of_planes -= 1
        elif position == "down":
            self.__repository.plane_found_down_cabin(second_coordinate, first_coordinate)
            self.__number_of_planes -= 1


    def guess_the_plane(self, first_coordinate, second_coordinate):
        try:
            CheckIfTheFirstCoordinateIsRight.validate(first_coordinate)
            CheckIfTheSecondCoordinateIsRight.validate(second_coordinate)
        except NotNumber:
            raise NotNumber
        except NotInTheRange:
            raise NotInTheRange
        except NotInTheRangeAJ:
            raise NotInTheRangeAJ
        except IsNumber:
            raise IsNumber
        second_coordinate = second_coordinate.upper()
        second_coordinate = ord(second_coordinate) - 64
        first_coordinate = int(first_coordinate) - 1
        second_coordinate = int(second_coordinate) - 1

        for index in range(3):
            if first_coordinate == self.__bot_cabin["first coordinate"][index] and second_coordinate == self.__bot_cabin["second coordinate"][index]:
                self.plane_found(first_coordinate, second_coordinate, self.__bot_cabin["position"][index])
                return 2
        if self.__repository.guess_the_plane(second_coordinate, first_coordinate) == True:
            return 1
        return 0

    def guess_the_plane_bot(self, first_coordinate, second_coordinate, player_cabin):
        for index in range(3):
            if first_coordinate == player_cabin["first coordinate"][index] and second_coordinate == \
                    player_cabin["second coordinate"][index]:
                self.plane_found(first_coordinate, second_coordinate, player_cabin["position"][index])
                self.__number_of_planes -= 1
                return 2
        if self.__repository.guess_the_plane(second_coordinate, first_coordinate) == True:
            return 1
        return 0

    def is_game_won(self):
        if self.__number_of_planes == 0:
            return True
        return False

    def get_element(self, row, column):
        return self.__repository.get_element(row, column)

    def get_all(self):
        return self.__repository.get_all()

    def get_row(self, row):
        return self.__repository.get_row(row)
