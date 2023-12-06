# Creating a 2D array (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in the 2D array
print(matrix[0][0])  # Access the element at the first row and first column (1)
print(matrix[1][2])  # Access the element at the second row and third column (6)

# Modifying elements in the 2D array
matrix[1][1] = 10  # Change the value at the second row and second column to 10

# Looping through the 2D array
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()

# Adding a new row to the matrix
new_row = [11, 12, 13]
matrix.append(new_row)

# Adding a new column to the matrix
new_column = [14, 15, 16]
for i in range(len(matrix)):
    matrix[i].append(new_column[i])

# Displaying the updated matrix
for row in matrix:
    for element in row:
        print(element, end=' ')
    print()
