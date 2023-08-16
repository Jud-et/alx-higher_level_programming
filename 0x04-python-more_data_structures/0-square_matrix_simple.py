#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store squared values
    squared_matrix = []

    # Iterate over each row in the input matrix
    for row in matrix:
        # Create a new row to store squared values
        squared_row = []

        # Iterate over each element in the row and compute the square
        for num in row:
            squared_row.append(num ** 2)

        # Add the squared row to the squared matrix
        squared_matrix.append(squared_row)

    return squared_matrix
