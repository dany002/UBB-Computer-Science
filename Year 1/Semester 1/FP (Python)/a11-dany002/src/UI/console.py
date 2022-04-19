

from domain.Validators import PlaneDoesntFit, ThereIsAlreadyAPlaneThere, NotInTheRange, NotNumber, NotInTheRangeAJ, IsNumber


class Console:
    def __init__(self, board_service_for_player, board_service_for_bot, bot_moves, bot_moves_for_ai = None):
        self.__bot_moves = bot_moves
        self.__bot_moves_for_ai = bot_moves_for_ai # I use it only for ai_vs_ai game
        self.__player_board = board_service_for_player
        self.__bot_board = board_service_for_bot
        self.__player_cabin = {'first coordinate': [], 'second coordinate': [], 'position' : []}

    def _help(self):
        print("So the board looks like this:"
              "   1  2  3  4  5  6  7  8  9  10"
              "A  0  0  0  0  0  0  0  0  0  0"
              "B  0  0  x  0  0  0  0  0  0  0"
              "C  x  x  x  x  x  0  0  0  0  0"
              "D  0  0  x  0  0  0  0  0  0  0"
              "E  0  x  x  x  0  0  x  0  0  0"
              "F  0  0  0  0  0  0  x  0  x  0"
              "G  0  0  0  0  0  x  x  x  x  0"
              "H  0  0  0  0  0  0  x  0  x  0"
              "I  0  0  0  0  0  0  x  0  0  0"
              "J  0  0  0  0  0  0  0  0  0  0"
              "with x is denoted the place where is a plane."
              "You have to type the following command to guess the place where it can be:"
              "C3 that means that you think that C3 is a part of the plane. If you've guessed we'll tell you :D"
              "You win if you got all the opponent's cabins. In this example cabins are: B3, G6. If you've guessed all the cabins ( there"
              "are 3 cabins ) you won and you have my respect for at least 5 seconds.")

    def create_board(self):
        while self.__player_board.how_many_planes_are_on_board() != 3:
            position = input("How do you want to be the plane positioned? Right/Left/Up/Down?")
            position = position.lower()
            if position == "up":
                first_coordinate = input("What do you want to be the x axis ? Choose a number between 1-10")
                second_coordinate = input("What do you want to be the y axis ? Choose a letter between A-J")
                try:
                    self.__player_board.up_cabin(first_coordinate, second_coordinate)
                    self.__player_cabin["first coordinate"].append(int(first_coordinate) - 1)
                    second_coordinate = second_coordinate.upper()
                    second_coordinate = ord(second_coordinate) - 64
                    self.__player_cabin["second coordinate"].append(int(second_coordinate) - 1)
                    self.__player_cabin["position"].append("up")
                    self._list_player_board()
                except ThereIsAlreadyAPlaneThere:
                    print("There is already a plane there!")
                except PlaneDoesntFit:
                    print("The plane doesn't fit")
                except NotNumber:
                    print("The first coordinate, the one on the x axis has to be an integer!")
                except NotInTheRange:
                    print("The first coordinate, the one on the x axis has to be between 1-10")
                except NotInTheRangeAJ:
                    print("The second coordinate, the one on the y axis has to be a letter between A-J")
                except IsNumber:
                    print("The second coordinate, the one on the y axis has to be a letter not a number.")

            if position == "down":
                first_coordinate = input("What do you want to be the x axis ? Choose a number between 1-10")
                second_coordinate = input("What do you want to be the y axis ? Choose a letter between A-J")
                try:
                    self.__player_board.down_cabin(first_coordinate, second_coordinate)
                    self.__player_cabin["first coordinate"].append(int(first_coordinate) - 1)
                    second_coordinate = second_coordinate.upper()
                    second_coordinate = ord(second_coordinate) - 64
                    self.__player_cabin["second coordinate"].append(int(second_coordinate) - 1)
                    self.__player_cabin["position"].append("down")
                    self._list_player_board()
                except ThereIsAlreadyAPlaneThere:
                    print("There is already a plane there!")
                except PlaneDoesntFit:
                    print("The plane doesn't fit")
                except NotNumber:
                    print("The first coordinate, the one on the x axis has to be an integer!")
                except NotInTheRange:
                    print("The first coordinate, the one on the x axis has to be between 1-10")
                except NotInTheRangeAJ:
                    print("The second coordinate, the one on the y axis has to be a letter between A-J")
                except IsNumber:
                    print("The second coordinate, the one on the y axis has to be a letter not a number.")

            if position == "left":
                first_coordinate = input("What do you want to be the x axis ? Choose a number between 1-10")
                second_coordinate = input("What do you want to be the y axis ? Choose a letter between A-J")
                try:
                    self.__player_board.left_cabin(first_coordinate, second_coordinate)
                    self.__player_cabin["first coordinate"].append(int(first_coordinate) - 1)
                    second_coordinate = second_coordinate.upper()
                    second_coordinate = ord(second_coordinate) - 64
                    self.__player_cabin["second coordinate"].append(int(second_coordinate) - 1)
                    self.__player_cabin["position"].append("left")
                    self._list_player_board()
                except ThereIsAlreadyAPlaneThere:
                    print("There is already a plane there!")
                except PlaneDoesntFit:
                    print("The plane doesn't fit")
                except NotNumber:
                    print("The first coordinate, the one on the x axis has to be an integer!")
                except NotInTheRange:
                    print("The first coordinate, the one on the x axis has to be between 1-10")
                except NotInTheRangeAJ:
                    print("The second coordinate, the one on the y axis has to be a letter between A-J")
                except IsNumber:
                    print("The second coordinate, the one on the y axis has to be a letter not a number.")

            if position == "right":
                first_coordinate = input("What do you want to be the x axis ? Choose a number between 1-10")
                second_coordinate = input("What do you want to be the y axis ? Choose a letter between A-J")
                try:
                    self.__player_board.right_cabin(first_coordinate, second_coordinate)
                    self.__player_cabin["first coordinate"].append(int(first_coordinate) - 1)
                    second_coordinate = second_coordinate.upper()
                    second_coordinate = ord(second_coordinate) - 64
                    self.__player_cabin["second coordinate"].append(int(second_coordinate) - 1)
                    self.__player_cabin["position"].append("right")
                    self._list_player_board()
                except ThereIsAlreadyAPlaneThere:
                    print("There is already a plane there!")
                except PlaneDoesntFit:
                    print("The plane doesn't fit")
                except NotNumber:
                    print("The first coordinate, the one on the x axis has to be an integer!")
                except NotInTheRange:
                    print("The first coordinate, the one on the x axis has to be between 1-10")
                except NotInTheRangeAJ:
                    print("The second coordinate, the one on the y axis has to be a letter between A-J")
                except IsNumber:
                    print("The second coordinate, the one on the y axis has to be a letter not a number.")

    def _print_menu(self):
        print("<list> to see your board")
        print("<guess> to guess the enemy plane.")
        print("<exit> to give up")

    def guess_the_plane(self):
        first_coordinate = input("What do you think that is the first coordinate of the enemy plane? X axis ( Choose between 1-10 )")
        second_coordinate = input("What do you think that is the second coordinate of the enemy plane? Y axis ( Choose between A-J )")
        try:
            valid = self.__bot_board.guess_the_plane(first_coordinate, second_coordinate)
            if valid == 2:
                print("You guessed the cabin! Good job!")
            elif valid == 1:
                print("You guessed a part of the plane!")
            else:
                print("Unlucky shot :)")
        except NotNumber:
            print("The first coordinate, the one on the x axis has to be an integer!")
        except NotInTheRange:
            print("The first coordinate, the one on the x axis has to be between 1-10")
        except NotInTheRangeAJ:
            print("The second coordinate, the one on the y axis has to be a letter between A-J")
        except IsNumber:
            print("The second coordinate, the one on the y axis has to be a letter not a number.")


    def _list_player_board(self):
        board_string = ""

        for index in range(10):
            board_string += self.format_row_to_be_printed(self.__player_board.get_all()[index]) + "\n"
        print(board_string)

    def format_row_to_be_printed(self, battle_row):
        battle_string = str(battle_row).replace("'", "")
        battle_string = battle_string.replace("[", "")
        battle_string = battle_string.replace("]", "")
        battle_string = battle_string.replace(",", "")
        return battle_string

    def bot_action(self):
        self.__bot_moves.make_move(self.__player_cabin)

    def run_command_player_vs_bot(self):
        print("Good luck! You play versus a bot :)")
        print("First let's create your board!")
        self._list_player_board()
        self.create_board()
        self.__bot_board.create_board_for_bot()
        print('\n')
        hacks_on = input("Do you want to play with hacks? Yes or no?")
        hacks_on = hacks_on.lower()

        while self.__player_board.is_game_won() == False and self.__bot_board.is_game_won() == False:
            if hacks_on == "yes":
                print("Bot board is:")
                self._list_bot_board()
            self._print_menu()
            command = input("What do you want to do?")
            if command == "list":
                self._list_player_board()
                continue
            elif command == "guess":
                try:
                    self.guess_the_plane()
                except Exception:
                    continue
            elif command == "exit":
                print("Wow! You give up! I'm so sorry for you dude!")
                break
            self.bot_action()
        print('\n')
        self._list_player_board()
        if self.__player_board.is_game_won() == False:
            print("You won! Ez!")
        else:
            print("You lost!")


    ######################################################## AI VS AI #####################################################
    def _list_bot_board(self):
        """
        I use it only for ai_vs_ai
        :return:
        """
        board_string = ""

        for index in range(10):
            board_string += self.format_row_to_be_printed(self.__bot_board.get_all()[index]) + "\n"
        print(board_string)

    def _count_number_of_x_for_the_first_bot(self):
        """
        To see when the bot lose ( I use it only for ai_vs_ai )
        :return:
        """
        number_of_x = 0
        for index in range(10):
            for index2 in range(10):
                if self.__bot_board.get_element(index, index2) == "x":
                    number_of_x += 1
        return number_of_x

    def _count_number_of_x_for_the_second_bot(self):
        """
        To see when the bot lose ( I use it only for ai_vs_ai )
        :return:
        """
        number_of_x = 0
        for index in range(10):
            for index2 in range(10):
                if self.__player_board.get_element(index, index2) == "x":
                    number_of_x += 1
        return number_of_x


    def run_command_ai_vs_ai(self):
        """
        AI_vs_AI, I consider that self.__player_board is the 1st bot and self.__bot_board is the 2nd bot.
        :return:
        """
        print("This is going to be a hard battle!")
        print("Bot number 1: please create your board:")
        self.__player_board.create_board_for_bot()
        print("Bot number 1: Sure, here you are: ")
        self._list_player_board()

        print("Bot number 2: please create your board:")
        self.__bot_board.create_board_for_bot()
        print("Bot number 2: Sure, here you are: ")
        self._list_bot_board()

        while self._count_number_of_x_for_the_second_bot() != 30 and self._count_number_of_x_for_the_first_bot() != 30:
            self.__bot_moves.make_move(self.__player_board.get_the_list_of_bot_cabin())
            self.__bot_moves_for_ai.make_move(self.__bot_board.get_the_list_of_bot_cabin())
            print("Bot number 1 board:")
            self._list_player_board()
            print("Bot number 2 board:")
            self._list_bot_board()

        print('\n')
        if self._count_number_of_x_for_the_first_bot() == 30:
            print("The winner is Bot 1:")
            self._list_player_board()
            print("Also here is the board for Bot 2")
            self._list_bot_board()
        else:
            print("The winner is Bot 2:")
            self._list_bot_board()
            print("Also here is the board for Bot 1")
            self._list_player_board()