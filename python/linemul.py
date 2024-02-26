import numpy as np
import time

def generate_matrices(number_of_lines):
    # Matrix with all 1's of size (number_of_lines, number_of_lines)
    matrix_all_ones = np.ones((number_of_lines, number_of_lines))

    # Matrix with values 1 to number_of_lines according to row
    matrix_incremental = np.array([np.full(number_of_lines, i+1) for i in range(number_of_lines)])

    return matrix_all_ones, matrix_incremental

def line_multiplication(matrix_all_ones, matrix_incremental, number_of_lines):
    
    result = np.zeros((number_of_lines, number_of_lines))

    for i in range(number_of_lines):
        for j in range(number_of_lines):
            result[i, j] = matrix_all_ones[i, 0] * matrix_incremental[i, j]

    return result

# Example
number_of_lines = int(input("Enter the number of lines: "))

start_time = time.time()

matrix_all_ones, matrix_incremental = generate_matrices(number_of_lines)

result = line_multiplication(matrix_all_ones, matrix_incremental, number_of_lines)

end_time = time.time()
execution_time = round(end_time - start_time, 3)
print(execution_time)

print("\nResult of multiplication:")
print(result)