import numpy as np

ntype = np.int64

def read_matrix(fhandle):
    matrix = []
    for row in fhandle:
        row = row.rstrip()
        columns = []
        cols = row.split()
        for column in cols:
            column = int(column)
            columns.append(column)
        matrix.append(columns)
    return np.array(matrix)

def test_matrix_size(matrix, name_of_matrix):
    size = matrix.shape
    if size[0] == 0 or size[1] == 0:
        print("Matrix " + name_of_matrix + " has empty rows or colums")
        return 1
    if size[0] != size[1]:
        print("Number of rows of matrix " + name_of_matrix + " does not equal number of columns")
        return 1
    return 0

def test_matrices_size(matrix_a, matrix_b):
    name_a = "A"
    name_b = "B"
    size_a = matrix_a.shape
    size_b = matrix_b.shape
    result_of_matrix_test_a = test_matrix_size(matrix_a, name_a)
    result_of_matrix_test_b = test_matrix_size(matrix_b, name_b)
    if result_of_matrix_test_a == 1 or result_of_matrix_test_b == 1:
        return 1
    if size_a != size_b:
        print("Size of matrix " + name_a + " does not equal size of matrix " + name_b)
        return 1
    return 0

def square_matrix_multiply(matrix_a, matrix_b):    
    n = matrix_a.shape[0]
    matrix_c = np.zeros((n, n))
    matrix_c = matrix_c.astype(ntype)
    for i in range(n):
        for j in range(n):
            matrix_c[i, j] = 0
            for k in range(n):
                matrix_c[i, j] += matrix_a[i, k] * matrix_b[k, j]
    return matrix_c

def square_matrix_multiply_recursive(matrix_a, matrix_b):
    n = matrix_a.shape[0]
    matrix_c = np.zeros((n, n))
    matrix_c = matrix_c.astype(ntype)
    if n == 1:
        matrix_c[0, 0] = matrix_a[0, 0] * matrix_b[0, 0]
    else:
        half_n = int(n / 2)
        matrix_c[0 : half_n, 0 : half_n] = square_matrix_multiply_recursive(matrix_a[0 : half_n, 0 : half_n], matrix_b[0 : half_n, 0 : half_n]) + square_matrix_multiply_recursive(matrix_a[0 : half_n, half_n : n], matrix_b[half_n : n, 0 : half_n])
        matrix_c[0 : half_n, half_n : n] = square_matrix_multiply_recursive(matrix_a[0 : half_n, 0 : half_n], matrix_b[0 : half_n, half_n : n]) + square_matrix_multiply_recursive(matrix_a[0 : half_n, half_n : n], matrix_b[half_n : n, half_n : n])
        matrix_c[half_n : n, 0 : half_n] = square_matrix_multiply_recursive(matrix_a[half_n : n, 0 : half_n], matrix_b[0 : half_n, 0 : half_n]) + square_matrix_multiply_recursive(matrix_a[half_n : n, half_n : n], matrix_b[half_n : n, 0 : half_n])
        matrix_c[half_n : n, half_n : n] = square_matrix_multiply_recursive(matrix_a[half_n : n, 0 : half_n], matrix_b[0 : half_n, half_n : n]) + square_matrix_multiply_recursive(matrix_a[half_n : n, half_n : n], matrix_b[half_n : n, half_n : n])
    return matrix_c

def square_matrix_multiply_recursive_strassen(matrix_a, matrix_b):
    n = matrix_a.shape[0]
    matrix_c = np.zeros((n, n))
    matrix_c = matrix_c.astype(ntype)
    if n == 1:
        matrix_c[0, 0] = matrix_a[0, 0] * matrix_b[0, 0]
    else:
        half_n = int(n / 2)
        # Sums
        s0 = matrix_b[0 : half_n, half_n : n] - matrix_b[half_n : n, half_n : n]
        s1 = matrix_a[0 : half_n, 0 : half_n] + matrix_a[0 : half_n, half_n : n]
        s2 = matrix_a[half_n : n, 0 : half_n] + matrix_a[half_n : n, half_n : n]
        s3 = matrix_b[half_n : n, 0 : half_n] - matrix_b[0 : half_n, 0 : half_n]
        s4 = matrix_a[0 : half_n, 0 : half_n] + matrix_a[half_n : n, half_n : n]
        s5 = matrix_b[0 : half_n, 0 : half_n] + matrix_b[half_n : n, half_n : n]
        s6 = matrix_a[0 : half_n, half_n : n] - matrix_a[half_n : n, half_n : n]
        s7 = matrix_b[half_n : n, 0 : half_n] + matrix_b[half_n : n, half_n : n]
        s8 = matrix_a[0 : half_n, 0 : half_n] - matrix_a[half_n : n, 0 : half_n]
        s9 = matrix_b[0 : half_n, 0 : half_n] + matrix_b[0 : half_n, half_n : n]
        # Product of numbers
        p0 = square_matrix_multiply_recursive_strassen(matrix_a[0 : half_n, 0 : half_n], s0)
        p1 = square_matrix_multiply_recursive_strassen(s1, matrix_b[half_n : n, half_n : n])
        p2 = square_matrix_multiply_recursive_strassen(s2, matrix_b[0 : half_n, 0 : half_n])
        p3 = square_matrix_multiply_recursive_strassen(matrix_a[half_n : n, half_n : n], s3)
        p4 = square_matrix_multiply_recursive_strassen(s4, s5)
        p5 = square_matrix_multiply_recursive_strassen(s6, s7)
        p6 = square_matrix_multiply_recursive_strassen(s8, s9)
        # Parts of the new matrix equal summatrices
        matrix_c[0 : half_n, 0 : half_n] = p4 + p3 - p1 + p5
        matrix_c[0 : half_n, half_n : n] = p0 + p1
        matrix_c[half_n : n, 0 : half_n] = p2 + p3
        matrix_c[half_n : n, half_n : n] = p4 + p0 - p2 - p6
    return matrix_c            

def string_matrix(matrix):
    output_str = ""
    for row in matrix:
        str_row = " ".join(str(num) for num in row) + "\n"
        output_str += str_row
    return output_str

def string_matrix_format(matrix, name, message):
    output_str = "{_message} \"{_name}\":\n{_matrix}".format(_message = message, _name = name, _matrix = string_matrix(matrix))
    return output_str

def string_output_format_for_all_matrices(matrix_a, matrix_b, matrix_c, matrix_cr, matrix_crs):
    str_input_matrix = "Input matrix"
    str_output_matrix = "Output matrix"
    name_a = "A"
    name_b = "B"
    name_c = "Classical approach"
    name_cr = "Recursive approach"
    name_crs = "Recursive Strassen\'s algorithm"
    str_a = string_matrix_format(matrix_a, name_a, str_input_matrix)
    str_b = string_matrix_format(matrix_b, name_b, str_input_matrix)
    str_c = string_matrix_format(matrix_c, name_c, str_output_matrix)
    str_cr = string_matrix_format(matrix_cr, name_cr, str_output_matrix)
    str_crs = string_matrix_format(matrix_crs, name_crs, str_output_matrix)
    output_str = "{_str_a}\n{_str_b}\n{_str_c}\n{_str_cr}\n{_str_crs}".format(_str_a = str_a, _str_b = str_b, _str_c = str_c, _str_cr = str_cr, _str_crs = str_crs)
    return output_str
        
def print_output(output_str):
    print("")
    print(output_str)

def write_output(fhandle, output_str):
    fhandle.write(output_str)
    
fname_read_a = input("Enter input file name: ")
if len(fname_read_a) < 1: fname_read_a = "input/inputA.txt"

fname_read_b = input("Enter input file name: ")
if len(fname_read_b) < 1: fname_read_b = "input/inputB.txt"

fname_write = input("Enter output file name: ")
if len(fname_write) < 1: fname_write = "output/output.txt"

fhandle_read_a = open(fname_read_a, "r")
fhandle_read_b = open(fname_read_b, "r")
fhandle_write = open(fname_write, "w")

matrix_a = read_matrix(fhandle_read_a)
matrix_b = read_matrix(fhandle_read_b)

result_of_test_matrices_size = test_matrices_size(matrix_a, matrix_b)
if result_of_test_matrices_size:
    exit(1)

matrix_c = square_matrix_multiply(matrix_a, matrix_b)
matrix_cr = square_matrix_multiply_recursive(matrix_a, matrix_b)
matrix_crs = square_matrix_multiply_recursive_strassen(matrix_a, matrix_b)

output_str = string_output_format_for_all_matrices(matrix_a, matrix_b, matrix_c, matrix_cr, matrix_crs)

print_output(output_str)
write_output(fhandle_write, output_str)
