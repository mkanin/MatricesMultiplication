"""
Main class of matrix.
"""
class Matrix(object):
    
    """
    :param matrix: matrix
    :type matrix: numpy.array
    :param name: name of matrix
    :type name: str
    """
    def __init__(self, matrix, name = "Matrix"):
        self.matrix = matrix
        self.name = name
    
    """
    Test size of matrix.
    The matrix should be square. If the size of matrix is incorrect,
    this method throws an exception ValueError.
    """
    def test_size(self):
        size = self.matrix.shape
        if size[0] == 0 or size[1] == 0:
            raise ValueError("Matrix " + self.name + "has empty rows or columns")
        if size[0] != size[1]:
            raise ValueError("Number of rows of matrix " + self.name + " does not equal number of columns")
            
