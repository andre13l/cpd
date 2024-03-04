import numpy as np
import time

def generate_matrices(number_of_lines):
    # Matrix with all 1's of size (number_of_lines, number_of_lines)
    matrix_all_ones = np.ones((number_of_lines, number_of_lines))

    # Matrix with values 1 to number_of_lines according to row
    matrix_incremental = np.array([np.full(number_of_lines, i+1) for i in range(number_of_lines)])

    return matrix_all_ones, matrix_incremental

def line_multiplication(matrix_all_ones, matrix_incremental, number_of_lines):
    # Broadcast matrix_all_ones to have the same shape as matrix_incremental
    matrix_all_ones_broadcasted = np.broadcast_to(matrix_all_ones[:, 0][:, None], matrix_incremental.shape)

    # Perform element-wise multiplication
    result = matrix_all_ones_broadcasted * matrix_incremental

    return result

if __name__ == "__main__":
    number_of_lines = int(input("Enter the number of lines: "))

    start_time = time.time()

    matrix_all_ones, matrix_incremental = generate_matrices(number_of_lines)

    result = line_multiplication(matrix_all_ones, matrix_incremental, number_of_lines)

    end_time = time.time()
    execution_time = round(end_time - start_time, 3)
    print("Execution Time:", execution_time)

    print("\nResult of multiplication:")
    print(result)
