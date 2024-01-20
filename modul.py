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


def multiplication_of_a_vector_by_a_matrix(matrix, vector):
    result = multiply_matrices(vector, matrix)
    return result


def multiplication_of_a_matrix_by_a_vector(matrix, vector):
    vector = convert_vec(vector)
    result = multiply_matrices(matrix, vector)
    return result


def matrix_row_permutation(matrix):
    print("Початкова матриця:")
    print_matrix(matrix)
    row_1 = int(input("row_1 = "))
    row_2 = int(input("row_2 = "))
    rows_m = len(matrix)
    # починаю з 1 не з 0, зручніше
    if 1 <= row_1 <= rows_m and 1 <= row_2 <= rows_m:
        matrix[row_1 - 1], matrix[row_2 - 1] = matrix[row_2 - 1], matrix[row_1 - 1] 
    else:
        print("Індекси рядків неправильні! :(")
    print("Матриця після перестановки рядків:")
    print_matrix(matrix)


def matrix_col_permutation(matrix):
    print_matrix(matrix)
    col_1 = int(input("col_1 = "))
    col_2 = int(input("col_2 = "))
    col_m = len(matrix[0])
    row_m =len(matrix)
    # проходимось по рядку змінючи елементи стовпчиків
    if 1 <= col_1 <= col_m and 1 <= col_2 <= col_m:
        for i in range(row_m):
            # print(matrix[i])
            matrix[i][col_1 - 1], matrix[i][col_2 - 1] = matrix[i][col_2 - 1], matrix[i][col_1 - 1]
    else:
        print("Індекси стовпчиків неправильні! :(")
    print("Матриця після перестановки стовпчиків:")
    print_matrix(matrix)


def getting_a_matrix_row(matrix):
    rows_m = len(matrix)
    needed_row = int(input("Введіть бажаний рядок матриці, який ви хочете отримати: "))
    if 1 <= needed_row <= rows_m:
        return matrix[needed_row - 1]
    else:
        print("Індекс рядка неправильний! :(")


def multiplication_of_a_vector_by_a_number(vector, n):
    res= []
    for el in vector:
        el *= n
        res.append(el)
    return res


def subtraction_of_the_vector_from_all_rows_of_the_matrix(matrix, vector):
    cols_m = len(matrix[0])
    rows_m = len(matrix)   
    rows_v = len(vector) 
    if cols_m != rows_v:
        raise ValueError("Кількість елементів в стовпчику матриці != кількості елементів вектора")
    res = []
    # проходимось по кожному одному рядку, віднімаючи відповідний елемент матриці від відповідного елементу вектора
    for row_m in matrix:
        res_mat = []
        for i in range(len(row_m)):
            res_row = row_m[i] - vector[i]
            res_mat.append(res_row)
        res.append(res_mat)
    return res
# try:
#     res = subtraction_of_the_vector_from_all_rows_of_the_matrix()
#     print(res)
# except ValueError as e:
#     print(f"Помилка: {e}")

# додала одну додаткову функцію, щоб написати тільки модулями в matrix.py
def adding_a_vector_from_a_vector(vector1, vector2):
    # Перевірка, чи вектори мають однакову довжину
    if len(vector1) != len(vector2):
        raise ValueError("Не можна додавати вектори, у яких різна кількість елементів!")
    res = []
    for i in range(len(vector1)):
        res.append(vector1[i] + vector2[i])
    return res
# try:
#     result = adding_a_vector_from_a_vector(vector1, vector2)
#     print(result)
# except ValueError as e:
#     print(f"Помилка: {e}")
