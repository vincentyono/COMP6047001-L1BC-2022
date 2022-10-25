# Exercise 08 - Matrix Transposition

# NOTE: If you are confuse try to use the debugging feature in your pycharm or you can also use python tutor https://pythontutor.com/

matrix = eval(input("Please enter a matrix: "))

# check the size of the matrix
#               row          column
ROW, COL = (len(matrix), len(matrix[0]))

# create COL amount of array inside results
results = [[] for i in range(COL)]

# Because the nature of loops, the outer loop usually iterates horizontally, while the inner loop usually iterates vertically
for col in range(COL):
    for row in range(ROW):
        #                   reverse matrix row and column
        #                              |
        #                              V
        results[col].append(matrix[row][col])

print(f"Result: {results}")
