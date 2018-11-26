from matrix.matrix import Matrix
from matrix.checker import MatrixChecker
from matrix_multiplication.multiplication import MatrixMultiplication
from utils.utils import MatrixFileReader
from utils.utils import OutputFileWriter
import time

def main():

    fname_read_a = input("Enter input file name: ")
    if len(fname_read_a) < 1: fname_read_a = "files/input/input_a.txt"

    fname_read_b = input("Enter input file name: ")
    if len(fname_read_b) < 1: fname_read_b = "files/input/input_b.txt"

    fname_write = input("Enter output file name: ")
    if len(fname_write) < 1: fname_write = "files/output/output.txt"

    matrix_file_reader_1 = MatrixFileReader(fname_read_a)
    matrix_file_reader_2 = MatrixFileReader(fname_read_b)

    label_a = "A"
    matrix_a = matrix_file_reader_1.read(label_a)
    label_b = "B"
    matrix_b = matrix_file_reader_2.read(label_b)

    matrix_checker = MatrixChecker()

    try:
        matrix_checker.test_sizes(matrix_a, matrix_b)
    except ValueError:
        print(arg)
        exit(1)

    matrix_multiplication = MatrixMultiplication()

    matrix_a_arr = matrix_a._matrix
    matrix_b_arr = matrix_b._matrix

    start = time.time()
    matrix_c_arr = matrix_multiplication.square_matrix_multiply(matrix_a_arr, matrix_b_arr)
    end = time.time()
    runtime_c = end - start

    start = time.time()
    matrix_cr_arr = matrix_multiplication.square_matrix_multiply(matrix_a_arr, matrix_b_arr)
    end = time.time()
    runtime_cr = end - start

    start = time.time()
    matrix_crs_arr = matrix_multiplication.square_matrix_multiply_recursive_strassen(matrix_a_arr, matrix_b_arr)
    end = time.time()
    runtime_crs = end - start
    
    matrix_c = Matrix("Classical approach")
    matrix_c._matrix = matrix_c_arr

    matrix_cr = Matrix("Recursive approach")
    matrix_cr._matrix = matrix_cr_arr

    matrix_crs = Matrix("Recursive Strassen\'s algorithm")
    matrix_crs._matrix = matrix_crs_arr

    output_str_a = "Input matrix \"{_matrix_label}\":\n{_matrix}\n".format(
        _matrix_label = matrix_a._label, _matrix = str(matrix_a))
    output_str_b = "Input matrix \"{_matrix_label}\":\n{_matrix}\n".format(
        _matrix_label = matrix_b._label, _matrix = str(matrix_b))
    output_str_c = "Output matrix \"{_matrix_label}\":\n{_matrix}\nRuntime:\n{_runtime}\n".format(
        _matrix_label = matrix_c._label, _matrix = str(matrix_c), _runtime = runtime_c)
    output_str_cr = "Output matrix \"{_matrix_label}\":\n{_matrix}\nRuntime:\n{_runtime}\n".format(
        _matrix_label = matrix_cr._label, _matrix = str(matrix_cr), _runtime = runtime_cr)
    output_str_crs = "Output matrix \"{_matrix_label}\":\n{_matrix}\nRuntime:\n{_runtime}\n".format(
        _matrix_label = matrix_crs._label, _matrix = str(matrix_crs), _runtime = runtime_crs)

    output_file_writer = OutputFileWriter(fname_write)

    output_file_writer.write(output_str_a)
    output_file_writer.write("\n")
    output_file_writer.write(output_str_b)
    output_file_writer.write("\n")
    output_file_writer.write(output_str_c)
    output_file_writer.write("\n")
    output_file_writer.write(output_str_cr)
    output_file_writer.write("\n")
    output_file_writer.write(output_str_crs)
    output_file_writer.write("\n")

    print()
    print(output_str_a)
    print(output_str_b)
    print(output_str_c)
    print(output_str_cr)
    print(output_str_crs)

if __name__ == "__main__":
    main()



