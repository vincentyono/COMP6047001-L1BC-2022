from board import Board
from os import system  # os is a built-in Python module, for more information: https://docs.python.org/3/library/os.html # nopep8
from random import choice  # random is a built-in Python module, for more information: https://docs.python.org/3/library/random.html # nopep8


class Game:
    def __init__(self):
        self.__board = Board()
        self.__PLAYER = "O"
        self.__CPU = "X"
        self.__running = True
        self.__WINNER = None

    def __is_gameover(self) -> bool:
        if self.__board.is_win(self.__PLAYER):
            self.__WINNER = "Player"
            return True
        elif self.__board.is_win(self.__CPU):
            self.__WINNER = "CPU"
            return True
        elif len(self.__board.available_tile()) == 0:
            self.__WINNER = "Draw"
            return True
        else:
            return False

    def run_game(self):

        while self.__running:
            system("cls")  # Windows
            # system("clear")  # Mac

            is_invalid = True
            self.__board.print()

            # if player input invalid tile, it will loops and prompt player to input again
            while is_invalid:
                player = input("Please pick a tile: ")

                if player.isdigit():  # if player input a digit
                    is_invalid = self.__board.mark_board(
                        int(player), self.__PLAYER)

                if is_invalid:  # if it is invalid input
                    print("Invalid Input")

            if self.__is_gameover():  # check if it is game over
                self.__running = False
            else:                    # if it is not game over, CPU turns
                self.__board.mark_board(
                    choice(self.__board.available_tile()), self.__CPU)

            if self.__is_gameover():  # check if it is game over again
                self.__running = False

    def gameover(self):
        system("cls")  # Windows
        # system("clear")  # Mac

        self.__board.print()

        print()

        if self.__WINNER == "Player" or self.__WINNER == "CPU":
            print(f"Game Over, {self.__WINNER} Wins!")
        else:
            print(f"Game Over, it's a {self.__WINNER}")
