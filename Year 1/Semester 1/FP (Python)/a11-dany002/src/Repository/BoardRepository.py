from domain.Validators import PlaneDoesntFit, ThereIsAlreadyAPlaneThere

class BoardRepository:
    def __init__(self):
        self.__board_repository = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def is_there_place_for_a_plane_with_up_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        if first_coordinate_of_cabin > 6 or first_coordinate_of_cabin < 0 or second_coordinate_of_cabin < 2 or second_coordinate_of_cabin > 7:
            raise PlaneDoesntFit
        if self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 2] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 2] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 2][second_coordinate_of_cabin] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 3][second_coordinate_of_cabin] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 3][second_coordinate_of_cabin + 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 3][second_coordinate_of_cabin - 1] == 1:
            raise ThereIsAlreadyAPlaneThere
        return True

    def up_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        try:
            if self.is_there_place_for_a_plane_with_up_cabin(first_coordinate_of_cabin, second_coordinate_of_cabin) == True:
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] = 1
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin] = 1
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 1] = 1
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 2] = 1
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 1] = 1
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 2] = 1
                self.__board_repository[first_coordinate_of_cabin + 2][second_coordinate_of_cabin] = 1
                self.__board_repository[first_coordinate_of_cabin + 3][second_coordinate_of_cabin] = 1
                self.__board_repository[first_coordinate_of_cabin + 3][second_coordinate_of_cabin + 1] = 1
                self.__board_repository[first_coordinate_of_cabin + 3][second_coordinate_of_cabin - 1] = 1
        except PlaneDoesntFit:
            raise PlaneDoesntFit
        except ThereIsAlreadyAPlaneThere:
            raise ThereIsAlreadyAPlaneThere


    def is_there_place_for_a_plane_with_down_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        if first_coordinate_of_cabin < 3 or first_coordinate_of_cabin > 9 or second_coordinate_of_cabin < 2 or second_coordinate_of_cabin > 7:
            raise PlaneDoesntFit
        if self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 2] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 2] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 2][second_coordinate_of_cabin] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 3][second_coordinate_of_cabin] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 3][second_coordinate_of_cabin + 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 3][second_coordinate_of_cabin - 1] == 1:
            raise ThereIsAlreadyAPlaneThere
        return True

    def down_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        try:
            if self.is_there_place_for_a_plane_with_down_cabin(first_coordinate_of_cabin, second_coordinate_of_cabin) == True:
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] = 1
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin] = 1
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 1] = 1
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 2] = 1
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 1] = 1
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 2] = 1
                self.__board_repository[first_coordinate_of_cabin - 2][second_coordinate_of_cabin] = 1
                self.__board_repository[first_coordinate_of_cabin - 3][second_coordinate_of_cabin] = 1
                self.__board_repository[first_coordinate_of_cabin - 3][second_coordinate_of_cabin + 1] = 1
                self.__board_repository[first_coordinate_of_cabin - 3][second_coordinate_of_cabin - 1] = 1
        except PlaneDoesntFit:
            raise PlaneDoesntFit
        except ThereIsAlreadyAPlaneThere:
            raise ThereIsAlreadyAPlaneThere

    def is_there_place_for_a_plane_with_left_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        if first_coordinate_of_cabin > 7 or first_coordinate_of_cabin < 2 or second_coordinate_of_cabin < 0 or second_coordinate_of_cabin > 6:
            raise PlaneDoesntFit
        if self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] == 1 or \
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin + 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 2][second_coordinate_of_cabin + 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 2][second_coordinate_of_cabin + 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin + 2] == 1 or \
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin + 3] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 3] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 3] == 1:
            raise ThereIsAlreadyAPlaneThere
        return True

    def left_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        try:
            if self.is_there_place_for_a_plane_with_left_cabin(first_coordinate_of_cabin, second_coordinate_of_cabin) == True:
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] = 1
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin + 1] = 1
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 1] = 1
                self.__board_repository[first_coordinate_of_cabin - 2][second_coordinate_of_cabin + 1] = 1
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 1] = 1
                self.__board_repository[first_coordinate_of_cabin + 2][second_coordinate_of_cabin + 1] = 1
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin + 2] = 1
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin + 3] = 1
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 3] = 1
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 3] = 1
        except PlaneDoesntFit:
            raise PlaneDoesntFit
        except ThereIsAlreadyAPlaneThere:
            raise ThereIsAlreadyAPlaneThere

    def is_there_place_for_a_plane_with_right_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        if first_coordinate_of_cabin > 7 or first_coordinate_of_cabin < 2 or second_coordinate_of_cabin > 9 or second_coordinate_of_cabin < 3:
            raise PlaneDoesntFit
        if self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] == 1 or \
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin - 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 2][second_coordinate_of_cabin - 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 2][second_coordinate_of_cabin - 1] == 1 or \
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin - 2] == 1 or \
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin - 3] == 1 or \
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 3] == 1 or \
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 3] == 1:
            raise ThereIsAlreadyAPlaneThere
        return True

    def right_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        try:
            if self.is_there_place_for_a_plane_with_right_cabin(first_coordinate_of_cabin, second_coordinate_of_cabin) == True:
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] = 1
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin - 1] = 1
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 1] = 1
                self.__board_repository[first_coordinate_of_cabin - 2][second_coordinate_of_cabin - 1] = 1
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 1] = 1
                self.__board_repository[first_coordinate_of_cabin + 2][second_coordinate_of_cabin - 1] = 1
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin - 2] = 1
                self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin - 3] = 1
                self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 3] = 1
                self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 3] = 1
        except PlaneDoesntFit:
            raise PlaneDoesntFit
        except ThereIsAlreadyAPlaneThere:
            raise ThereIsAlreadyAPlaneThere

    def plane_found_right_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] = 'x'
        self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin - 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 2][second_coordinate_of_cabin - 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 2][second_coordinate_of_cabin - 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin - 2] = 'x'
        self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin - 3] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 3] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 3] = 'x'

    def plane_found_left_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] = 'x'
        self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin + 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 2][second_coordinate_of_cabin + 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 2][second_coordinate_of_cabin + 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin + 2] = 'x'
        self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin + 3] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 3] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 3] = 'x'

    def plane_found_up_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin - 2] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 1][second_coordinate_of_cabin + 2] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 2][second_coordinate_of_cabin] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 3][second_coordinate_of_cabin] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 3][second_coordinate_of_cabin + 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin + 3][second_coordinate_of_cabin - 1] = 'x'

    def plane_found_down_cabin(self, first_coordinate_of_cabin, second_coordinate_of_cabin):
        self.__board_repository[first_coordinate_of_cabin][second_coordinate_of_cabin] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin - 2] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 1][second_coordinate_of_cabin + 2] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 2][second_coordinate_of_cabin] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 3][second_coordinate_of_cabin] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 3][second_coordinate_of_cabin + 1] = 'x'
        self.__board_repository[first_coordinate_of_cabin - 3][second_coordinate_of_cabin - 1] = 'x'

    def guess_the_plane(self, first_coordinate, second_coordinate):

        if self.__board_repository[first_coordinate][second_coordinate] == 1:
            self.__board_repository[first_coordinate][second_coordinate] = 'y'
            return True
        return False

    def get_all(self):
        return self.__board_repository

    def get_element(self, row, column):
        return self.__board_repository[row][column]

    def get_row(self, row):
        return self.__board_repository[row]

