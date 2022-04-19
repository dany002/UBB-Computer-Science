import random

class BotMoves:
    def __init__(self, board_service_for_player):
        self.__player_service = board_service_for_player

        self.__list_of_moves = {'first coordinate': [], 'second coordinate': []}
        self.__number_of_neighbours = 0
        self.__status = {}

    def check_duplicate_move(self, first_coordinate, second_coordinate):
        for index in range(len(self.__list_of_moves['first coordinate'])):
            if first_coordinate == self.__list_of_moves['first coordinate'][index] and second_coordinate == self.__list_of_moves['second coordinate'][index]:
                return True
        return False

    def make_move(self, player_cabin):
        list_of_possible_moves = []
        for index in range(len(self.__list_of_moves['first coordinate'])):
            if self.__status[(self.__list_of_moves['first coordinate'][index], self.__list_of_moves['second coordinate'][index])] == 1:

                if self.check_duplicate_move(self.__list_of_moves['first coordinate'][index], self.__list_of_moves['second coordinate'][index] + 1) == False:
                    list_of_possible_moves.append((self.__list_of_moves['first coordinate'][index], self.__list_of_moves['second coordinate'][index] + 1))

                if self.check_duplicate_move(self.__list_of_moves['first coordinate'][index], self.__list_of_moves['second coordinate'][index] - 1) == False:
                    list_of_possible_moves.append((self.__list_of_moves['first coordinate'][index], self.__list_of_moves['second coordinate'][index] - 1))

                if self.check_duplicate_move(self.__list_of_moves['first coordinate'][index] + 1, self.__list_of_moves['second coordinate'][index]) == False:
                    list_of_possible_moves.append((self.__list_of_moves['first coordinate'][index] + 1, self.__list_of_moves['second coordinate'][index]))

                if self.check_duplicate_move(self.__list_of_moves['first coordinate'][index] - 1, self.__list_of_moves['second coordinate'][index]) == False:
                    list_of_possible_moves.append((self.__list_of_moves['first coordinate'][index] - 1, self.__list_of_moves['second coordinate'][index]))
        list_of_possible_moves = list(filter(lambda move: 0 <= move[0] <= 9 and 0 <= move[1] <= 9, list_of_possible_moves))
        if len(list_of_possible_moves) == 0:
            first_coordinate = random.randint(0, 9)
            second_coordinate = random.randint(0, 9)
            while self.check_duplicate_move(first_coordinate, second_coordinate) == True:
                first_coordinate = random.randint(0, 9)
                second_coordinate = random.randint(0, 9)
            list_of_possible_moves.append((first_coordinate, second_coordinate))


        move = list_of_possible_moves[random.randrange(0, len(list_of_possible_moves))]
        self.__status[move] = self.__player_service.guess_the_plane_bot(move[0], move[1], player_cabin)

        self.__list_of_moves['first coordinate'].append(move[0])
        self.__list_of_moves['second coordinate'].append(move[1])