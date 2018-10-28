import numpy

"""
This class checks size of two matrices and comapres its shape.
"""
class MatrixChecker(object):
    
    """
    :param matrix_a: the first matrix
    :type matrix_a: numpy.array
    :param matrix_b: the second matrix
    :type matrix_b: numpy.array
    """
    def __init__(self, matrix_a, matrix_b):
        self.matrix_a = matrix_a
        self.matrix_b = matrix_b

    def test_sizes(self):
        try:
            self.matrix_a.test_size()
            self.matrix_b.test_size()
        except ValueError as inst:
            raise ValueError(str(inst))
        else:
            size_a = self.matrix_a.shape
            size_b = self.matrix_b.shape
            if size_a != size_b:
                raise ValueError("Size of matrix " + self.matrix_a.name + " does not equal size of matrix " + self.matrix_b.name)
