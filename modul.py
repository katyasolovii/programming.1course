def errors(matrix, rows, cols):
    for row in matrix:
        if len(row) != cols:
            return False
    return True


def input_matrix():
    while True:
        print("Введіть матрицю:")
        rows, cols = [int(el) for el in input().split()]
        matrix = []
        for i in range(rows):
            count_el = [int(el) for el in input().split()]
            matrix.append(count_el)
    
        if errors(matrix, rows, cols):
            return matrix
        else:
            print("Неправильно ввели матрицю! :( Почніть спочатку! :)")


def print_matrix(matrix):
    mat = []
    for row in matrix:
        line = " ".join(map(str, row))  
        mat.append(line)
    result = "\n".join(mat) 
    print("---------\n" + result + "\n---------")


def input_vector():
    while True:
        print("Введіть вектор:")
        rows, cols = [int(el) for el in input().split()]
        vector = []
        for i in range(rows):
            count_el = [int(el) for el in input().split()]
            vector.append(count_el)

        if errors(vector, rows, cols):
            return vector
        else:
            print("Неправильно ввели вектор! :( Почніть спочатку! :)")


def convert_vec(vector):
    # конвертуємо рядок вертора у стовпчик == матриця з одним стовпчиком
    rows = len(vector)
    cols = len(vector[0])
    col = []
    for i in range(cols):
        col_el = []
        for j in range(rows):
            col_el.append(vector[j][i])
        col.append(col_el)
    return col


def multiply_matrices(matrix_1, matrix_2):
    # множемо рядок rows першої матриці на стовпчик cols другої матриці
    cols_1 = len(matrix_1[0]) # кількість елементів у ствопчику [0] - у першому рядку 
    rows_1 = len(matrix_1)
    rows_2 = len(matrix_2)
    cols_2 = len(matrix_2[0])
    print(cols_1 , cols_2, rows_1, rows_2)
    if cols_1 != rows_2:
        raise ValueError("Матриці не можна помножити! :( Оскільки, стовпці rows першої мариці != рядкам cols дургої матриці.")
    res = []
    for _ in range(rows_1):
        row = [0] * cols_2
        res.append(row)
    for i in range(rows_1):
        for j in range(cols_2):  
            for k in range(rows_2): 
                res[i][j] += matrix_1[i][k] * matrix_2[k][j]
    return res


def multiplication_of_a_vector_by_a_matrix(matrix, vector):
    result = multiply_matrices(vector, matrix)
    return result


def multiplication_of_a_matrix_by_a_vector(matrix, vector):
    vector = convert_vec(vector)
    result = multiply_matrices(matrix, vector)
    return result


def to_standard(user_coords):
    standard_coords = user_coords - 1
    return standard_coords


def data_for_row_permutation(matrix):
    print("Початкова матриця:")
    print_matrix(matrix)
    i = to_standard(int(input("row_1 = ")))
    j = to_standard(int(input("row_2 = ")))
    swap_rows(matrix, i, j)


def swap_rows(matrix, i, j):
    rows_m = len(matrix)
    if 0 <= i <= rows_m and 0 <= j <= rows_m:
        matrix[i], matrix[j] = matrix[j], matrix[i] 
    else:
        print("Індекси рядків неправильні! :(")
    print("Матриця після перестановки рядків:")
    print_matrix(matrix)
    return matrix


def data_for_col_permutation(matrix):
    print("Початкова матриця:")
    print_matrix(matrix)
    i = to_standard(int(input("col_1 = ")))
    j = to_standard(int(input("col_2 = ")))
    swap_cols(matrix, i, j)
    

def swap_cols(matrix, i , j):
    col_m = len(matrix[0])
    row_m =len(matrix)
    # проходимось по рядку змінючи елементи стовпчиків
    if 0 <= i <= col_m and 0 <= j <= col_m:
        for k in range(row_m):
            matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
    else:
        print("Індекси стовпчиків неправильні! :(")
    print("Матриця після перестановки стовпчиків:")
    print_matrix(matrix)
    return matrix


def getting_row(matrix, i):
    rows_m = len(matrix)
    needed_row = to_standard(int(input("Введіть бажаний рядок матриці, який ви хочете отримати: ")))
    if 0 <= needed_row <= rows_m:
        return matrix[needed_row]
    else:
        print("Індекс рядка неправильний! :(")


def multiplication(vector, n):
    v = []
    for i in vector:
        v.append(i * n)
    return v


def subtraction(matrix, vector):
    cols_m = len(matrix[0])
    rows_m = len(matrix)   
    rows_v = len(vector) 
    cols_v = len(vector[0])
    if rows_m != cols_v:
        raise ValueError("Кількість елементів в стовпчику матриці != кількості елементів вектора")
    res_mat = []
    # проходимось по кожному одному рядку, віднімаючи відповідний елемент матриці від відповідного елементу вектора
    for rows_m in matrix:
        res_vec = []
        for i in range(len(rows_m)):
            res_row = rows_m[i] - vector[0][i]
            res_vec.append(res_row)
        res_mat.append(res_vec)
    return res_mat


# додала одну додаткову функцію, щоб написати тільки модулями в matrix.py
def add(vector1, vector2):
    cols_v1 = len(vector1)
    cols_v2 = len(vector2)
    # Перевірка, чи вектори мають однакову довжину
    if cols_v1 != cols_v2:
        raise ValueError("Не можна додавати вектори, у яких різна кількість елементів!")
    res = []
    for i in range(cols_v1):
        res.append(vector1[i] + vector2[i])
    return res
