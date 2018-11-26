import numpy as np

ntype = np.int64

class MatrixMultiplication:

    def square_matrix_multiply(self, matrix_a_arr, matrix_b_arr):
        n = matrix_a_arr.shape[0]
        matrix_c_arr = np.zeros((n, n))
        matrix_c_arr = matrix_c_arr.astype(ntype)
        for i in range(n):
            for j in range(n):
                matrix_c_arr[i, j] = 0
                for k in range(n):
                    matrix_c_arr[i, j] += matrix_a_arr[i, k] * matrix_b_arr[k, j]
        return matrix_c_arr

    def square_matrix_multiply_recursive(self, matrix_a_arr, matrix_b_arr):
        n = matrix_a_arr.shape[0]
        matrix_c_arr = np.zeros((n, n))
        matrix_c_arr = matrix_c_arr.astype(ntype)
        if n == 1:
            matrix_c_arr[0, 0] = matrix_a_arr[0, 0] * matrix_b_arr[0, 0]
        else:
            half_n = int(n / 2)
            matrix_c_arr[0 : half_n, 0 : half_n] = self.square_matrix_multiply_recursive(matrix_a_arr[0 : half_n, 0 : half_n], matrix_b_arr[0 : half_n, 0 : half_n]) + self.square_matrix_multiply_recursive(matrix_a_arr[0 : half_n, half_n : n], matrix_b_arr[half_n : n, 0 : half_n])
            matrix_c_arr[0 : half_n, half_n : n] = self.square_matrix_multiply_recursive(matrix_a_arr[0 : half_n, 0 : half_n], matrix_b_arr[0 : half_n, half_n : n]) + self.square_matrix_multiply_recursive(matrix_a_arr[0 : half_n, half_n : n], matrix_b_arr[half_n : n, half_n : n])
            matrix_c_arr[half_n : n, 0 : half_n] = self.square_matrix_multiply_recursive(matrix_a_arr[half_n : n, 0 : half_n], matrix_b_arr[0 : half_n, 0 : half_n]) + self.square_matrix_multiply_recursive(matrix_a_arr[half_n : n, half_n : n], matrix_b_arr[half_n : n, 0 : half_n])
            matrix_c_arr[half_n : n, half_n : n] = self.square_matrix_multiply_recursive(matrix_a_arr[half_n : n, 0 : half_n], matrix_b_arr[0 : half_n, half_n : n]) + self.square_matrix_multiply_recursive(matrix_a_arr[half_n : n, half_n : n], matrix_b_arr[half_n : n, half_n : n])
        return matrix_c_arr

    def square_matrix_multiply_recursive_strassen(self, matrix_a_arr, matrix_b_arr):
        n = matrix_a_arr.shape[0]
        matrix_c_arr = np.zeros((n, n))
        matrix_c_arr = matrix_c_arr.astype(ntype)
        if n == 1:
            matrix_c_arr[0, 0] = matrix_a_arr[0, 0] * matrix_b_arr[0, 0]
        else:
            half_n = int(n / 2)
            # Sums
            s0 = matrix_b_arr[0 : half_n, half_n : n] - matrix_b_arr[half_n : n, half_n : n]
            s1 = matrix_a_arr[0 : half_n, 0 : half_n] + matrix_a_arr[0 : half_n, half_n : n]
            s2 = matrix_a_arr[half_n : n, 0 : half_n] + matrix_a_arr[half_n : n, half_n : n]
            s3 = matrix_b_arr[half_n : n, 0 : half_n] - matrix_b_arr[0 : half_n, 0 : half_n]
            s4 = matrix_a_arr[0 : half_n, 0 : half_n] + matrix_a_arr[half_n : n, half_n : n]
            s5 = matrix_b_arr[0 : half_n, 0 : half_n] + matrix_b_arr[half_n : n, half_n : n]
            s6 = matrix_a_arr[0 : half_n, half_n : n] - matrix_a_arr[half_n : n, half_n : n]
            s7 = matrix_b_arr[half_n : n, 0 : half_n] + matrix_b_arr[half_n : n, half_n : n]
            s8 = matrix_a_arr[0 : half_n, 0 : half_n] - matrix_a_arr[half_n : n, 0 : half_n]
            s9 = matrix_b_arr[0 : half_n, 0 : half_n] + matrix_b_arr[0 : half_n, half_n : n]
            # Product of numbers
            p0 = self.square_matrix_multiply_recursive_strassen(matrix_a_arr[0 : half_n, 0 : half_n], s0)
            p1 = self.square_matrix_multiply_recursive_strassen(s1, matrix_b_arr[half_n : n, half_n : n])
            p2 = self.square_matrix_multiply_recursive_strassen(s2, matrix_b_arr[0 : half_n, 0 : half_n])
            p3 = self.square_matrix_multiply_recursive_strassen(matrix_a_arr[half_n : n, half_n : n], s3)
            p4 = self.square_matrix_multiply_recursive_strassen(s4, s5)
            p5 = self.square_matrix_multiply_recursive_strassen(s6, s7)
            p6 = self.square_matrix_multiply_recursive_strassen(s8, s9)
            # Parts of the new matrix equal summatrices
            matrix_c_arr[0 : half_n, 0 : half_n] = p4 + p3 - p1 + p5
            matrix_c_arr[0 : half_n, half_n : n] = p0 + p1
            matrix_c_arr[half_n : n, 0 : half_n] = p2 + p3
            matrix_c_arr[half_n : n, half_n : n] = p4 + p0 - p2 - p6
        return matrix_c_arr 
