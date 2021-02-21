import math
rows = int(input("How many rows would you like in you 2d array? "))
cols = int(input("How many columns would you like in you 2d array? "))
num_rows, num_cols = rows, cols
matrix = ([0, 0, 0, 0],
          [0, 0, 0, 0])
arr2 = matrix * math.ceil(num_cols)

print(arr2)


arr3 = arr2 * math.ceil(num_rows)
matrix1 = ([1, 1, 1, 1],
           [1, 1, 1, 1])
arr4 = matrix1 * math.ceil(num_cols)
arr5 = arr4 * math.ceil(num_rows)
arr6 = (arr3 + arr5) + arr3