import numpy as np
import time

def generate_matrices(number_of_lines):
    # Matrix with all 1's of size (number_of_lines, number_of_lines)
    matrix_all_ones = np.ones((number_of_lines, number_of_lines))

    # Matrix with values 1 to number_of_lines according to row
    matrix_incremental = np.array([np.full(number_of_lines, i+1) for i in range(number_of_lines)])

    return matrix_all_ones, matrix_incremental

def block_multiplication(matrix_all_ones, matrix_incremental, number_of_lines, block_size):
    result = np.zeros((number_of_lines, number_of_lines))

    for i in range(0, number_of_lines, block_size):
        for j in range(0, number_of_lines, block_size):
            for k in range(0, number_of_lines, block_size):
                for x in range(i, min(i + block_size, number_of_lines)):
                    for y in range(j, min(j + block_size, number_of_lines)):
                        for z in range(k, min(k + block_size, number_of_lines)):
                            result[x, y] += matrix_all_ones[x, z] * matrix_incremental[z, y]

    return result

number_of_lines = int(input("Enter the number of lines: "))

block_size = int(input("Enter the block size: "))

start_time = time.time()

matrix_all_ones, matrix_incremental = generate_matrices(number_of_lines)

result = block_multiplication(matrix_all_ones, matrix_incremental, number_of_lines, block_size)

end_time = time.time()
execution_time = round(end_time - start_time, 3)
print(execution_time)

print("\nResult of multiplication:")
print(result)