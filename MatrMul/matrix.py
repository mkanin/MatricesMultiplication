class Matrix(object):
    """Main class of matrix.

    :param matrix: matrix
    :type matrix: numpy.array
    :param name: name of matrix
    :type name: str
    """
    def __init__(self, matrix, name):
        self.matrix = matrix
        self.name = name

    def test_size(self):
        size = self.matrix.shape
        if size[0] == 0 or size[1] == 0:
            raise ValueError("Matrix " + self.name + "has empty rows or columns")
        if size[0] != size[1]:
            raise ValueError("Number of rows of matrix " + self.name + " does not equal number of columns")
            
