# Copyright (c) 2018 Mikhail Kanin
import numpy as np

ntype = np.int64

class Matrix:

    def __init__(self, label, n = 1):
        self._label = label
        matrix = np.zeros((n, n))
        self._matrix = matrix.astype(ntype)

    def create(self, matrix_list):
        self._matrix = np.array(matrix_list)

    def shape(self):
        return self._matrix.shape

    def __repr__(self):
        output_res = list()
        for row in self._matrix:
            str_row = " ".join(str(num) for num in row)
            output_res.append(str_row)
        output_str = "\n".join(output_res)
        return output_str
