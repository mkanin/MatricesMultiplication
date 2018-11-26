from matrix.matrix import Matrix

class MatrixFileReader:

    def __init__(self, file_name):
        self._file_name = file_name.strip()
        
    def read(self, label):
        self._fhandle = open(self._file_name, "r")
        matrix_list = list()
        for row in self._fhandle:
            row = row.strip()
            if row.startswith('#'):
                continue
            columns = list()
            cols = row.split()
            for column in cols:
                column = int(column)
                columns.append(column)
            matrix_list.append(columns)
        self._fhandle.close()
        matrix = Matrix(label)
        matrix.create(matrix_list)
        return matrix        

class OutputFileWriter:
    
    def __init__(self, file_name):
        self._file_name = file_name.strip()
        self._fhandle = open(self._file_name, "w")
    
    def write(self, output_str):
        self._fhandle.write(output_str)

    def close(self):
        self._fhandle.close()
