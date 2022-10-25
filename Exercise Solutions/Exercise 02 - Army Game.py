# Exercise 02 - Army Game (hackerrank.com)

import math  # Built-in python module, for more information: https://docs.python.org/3/library/math.html

#    m   |  supply
# -------+----------    looking at the pattern, it looks like (m / 2) but it rounds up
#    1   |    1         if there is a decimal point
#    2   |    1
#    3   |    2
#    4   |    2
#    5   |    3
#    6   |    3
#    7   |    4
#    8   |    4
#    9   |    5


def game_with_cells(m: int, n: int) -> int:
    return math.ceil(m / 2) * math.ceil(n / 2)


print(game_with_cells(2, 2))  # output: 1
print(game_with_cells(9, 9))  # output: 25
print(game_with_cells(10, 1))  # output: 5
print(game_with_cells(6, 4))  # output: 6
