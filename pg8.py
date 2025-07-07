import numpy as np

rows = int(input("Enter the number of rows for the matrix: "))
cols = int(input("Enter the number of columns for the matrix: "))

if rows != cols:
    print("Error: Only square matrices have inverses. Please enter equal number of rows and columns.")
    exit()
    
matrix_elements = []
print("Enter the matrix elements row by row:")
for i in range(rows):
    row = []
    for j in range(cols):
        element = float(input(f"Enter element at position ({i+1}, {j+1}): "))
        row.append(element)
    matrix_elements.append(row)

matrix = np.array(matrix_elements)
try:
    inverse_matrix = np.linalg.inv(matrix)
    print("\nOriginal Matrix:")
    print(matrix)
    print("\nInverse Matrix:")
    print(inverse_matrix)
except np.linalg.LinAlgError:
    print("\nError: The matrix is singular and does not have an inverse.")
