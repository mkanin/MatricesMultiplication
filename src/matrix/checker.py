# Copyright (c) 2018 Mikhail Kanin
import math

class MatrixChecker:       
    
    def test_size(self, matrix):
        n_rows = matrix.shape()[0]
        n_columns = matrix.shape()[1]
        if n_rows == 0 or n_columns == 0:
            raise ValueError("Matrix %s has empty rows or columns." % (matrix._label,))
        if n_rows != n_columns:
            raise ValueError("The number of rows of matrix %s does not equal the number of columns." % (matrix._label,))
        size_log_2 = math.log(n_rows, 2)
        if not size_log_2.is_integer():
            raise ValueError("The shape of matrix must be pow of 2." % (matrix._label,))
        return n_rows

    def test_sizes(self, matrix_a, matrix_b):
        size_a = self.test_size(matrix_a)
        size_b = self.test_size(matrix_b)
        if size_a != size_b:
            raise ValueError("The size of matrix %s does not equal size of matrix %s." % (matrix_a._label, matrix_b._label,))
        
