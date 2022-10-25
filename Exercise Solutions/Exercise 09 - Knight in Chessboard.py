# Exercise 09 - Knight in Chessboard

# NOTE: If you are confuse try to use the debugging feature in your pycharm or you can also use python tutor https://pythontutor.com/

alphabets = ["A", "B", "C", "D", "E", "F", "G", "H"]
board = []

# width and height of chessboard
WIDTH = 8
HEIGHT = 8

user_input = input("Please select a coordinate: ")

# coordinate as tuple (x, y)
coordinate = (alphabets.index(user_input[0].upper()),
              HEIGHT - int(user_input[1]))

# creating board
for height in range(HEIGHT):
    board.append([])
    for width in range(WIDTH):
        #                this is to reverse the number so (8 - 0) from the top to (8 - 7) at the bottom
        #                use height so number only changes vertically
        #                                                |
        #                                                |   this part
        #                                                V
        board[height].append(f"{alphabets[width]}{HEIGHT - height}")

# mark the selected coordinate
#           y              x
board[coordinate[1]][coordinate[0]] = "KN"

#           these are the possible coordinates that knight can move to from the selected coordinate, the format is (x, y)
#           negative x == to the left and positive x == to the right, negative y == to the top and positive y == to the bottom
for x, y in [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]:

    #   check if the possible coordinates are inside the board
    if (coordinate[0] + x >= 0 and coordinate[0] + x <= 7) and (coordinate[1] + y >= 0 and coordinate[1] + y <= 7):
        # mark the possible moves
        board[coordinate[1] + y][coordinate[0] + x] = "XX"

# print the board
for height in range(HEIGHT):
    for width in range(WIDTH):
        print(board[height][width], end=" ")
    print()  # this is for new lines
