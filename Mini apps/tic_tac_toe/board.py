# Custom class to serve as tic tac toe board
class Board:
    def __init__(self):
        self.__board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def print(self) -> None:
        print(f" {self.__board[0]} | {self.__board[1]} | {self.__board[2]} ")
        print("---+---+---")
        print(f" {self.__board[3]} | {self.__board[4]} | {self.__board[5]} ")
        print("---+---+---")
        print(f" {self.__board[6]} | {self.__board[7]} | {self.__board[8]} ")

    def mark_board(self, tile_number: int, player: str) -> bool:
        # Check if tile_number is in range of self.__board list
        if tile_number >= 1 and tile_number <= 9:
            # Check if the tile chosen is an int (if it is an int, it means it is empty)
            if isinstance(self.__board[tile_number - 1], int):
                self.__board[tile_number - 1] = player
                return False

        return True

    def is_win(self, player: str) -> bool:
        # Check horizontal
        is_horizontal = (((self.__board[0] == player) and (self.__board[1] == player) and (self.__board[2] == player)) or
                         ((self.__board[3] == player) and (self.__board[4] == player) and (self.__board[5] == player)) or
                         ((self.__board[6] == player) and (self.__board[7] == player) and (self.__board[8] == player)))

        # Check vertical
        is_vertical = (((self.__board[0] == player) and (self.__board[3] == player) and (self.__board[6] == player)) or
                       ((self.__board[1] == player) and (self.__board[4] == player) and (self.__board[7] == player)) or
                       ((self.__board[2] == player) and (self.__board[5] == player) and (self.__board[8] == player)))

        # Check diagonal
        is_diagonal = (((self.__board[0] == player) and (self.__board[4] == player) and (self.__board[8] == player)) or
                       ((self.__board[2] == player) and (self.__board[4] == player) and (self.__board[6] == player)))

        if is_horizontal or is_vertical or is_diagonal:
            return True

        return False

    def available_tile(self) -> list:
        result = []
        for tile in self.__board:
            if isinstance(tile, int):  # if tile is an int append to result
                result.append(tile)

        return result
