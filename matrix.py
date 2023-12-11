import modul

def upper_triangular_matrix():
    # спочатку, віднімемо перший рядок помножений на такий множник, щоб у другому рядку перший стовпик став 0 від другого
    # далі, те саме робимо тільки відмнімаємо від третього рядка
    # потім, переходимо до другого рядка і від нього помноженого на такий множник, щоб у третьому рядку другий стовпик став 0  від третього
    # всьо, + треба кожен раз шукати спеціальний множик +++ треба ще визначити знак
    # 4 12 8    + *(-2)   4 12 8          + *(-1/2)    4 12 8                      4 12 8 
    # 8 7 1               0 -17 -15                    0 -17 -15      + *3/17      0 -17 -15
    # 2 9 5               2 9 5                        0 3 1                       0 0 -28/17
    matrix = modul.input_matrix() 
    cols_m = len(matrix[0])
    rows_m = len(matrix)
    # перевірка чи взагалі можна перетворити матрицю на верхню квадратну матрицю 
    if rows_m != cols_m: 
        return "Цю матрицю не можна перетворити на верхню квадратну матрицю, оскільки кількість стовпчиків != кількості рядків"
    for i in range(rows_m):
        for j in range(i + 1, rows_m):
            # знайшли потрібний множник, але врахувавши знак
            num = - (matrix[j][i] / matrix[i][i])  
            # потім домножили його на весь рядок даного рядка
            mat_cur = modul.multiplication_of_a_vector_by_a_number(matrix[i], num)
            # далі від цього рядка віднімаємо рядок інший і оновлюємо матрицю
            matrix[j] = modul.adding_a_vector_from_a_vector(matrix[j], mat_cur)
    return modul.print_matrix(matrix)


try:
    res = upper_triangular_matrix()
    print(res)
except ValueError as e:
    print(f"Помилка: {e}")


def rank():
    # робимо те саме, тільки + рахуємо кількість ненульових рядків
    matrix = modul.input_matrix() 
    cols_m = len(matrix[0])
    rows_m = len(matrix)
    r = 0
    # перевірка чи взагалі можна перетворити матрицю на верхню квадратну матрицю 
    if rows_m != cols_m: 
        return "Цю матрицю не можна перетворити на верхню квадратну матрицю, оскільки кількість стовпчиків != кількості рядків"
    for i in range(rows_m):
        for j in range(i + 1, rows_m):
            # знайшли потрібний множник, але врахувавши знак
            num = - (matrix[j][i] / matrix[i][i])  
            # потім домножили його на весь рядок даного рядка
            mat_cur = modul.multiplication_of_a_vector_by_a_number(matrix[i], num)
            # далі від цього рядка віднімаємо рядок інший і оновлюємо матрицю
            matrix[j] = modul.adding_a_vector_from_a_vector(matrix[j], mat_cur)
    for i in range(rows_m):
        check = []
        for j in range(cols_m):
            if matrix[i][j] == 0:
                check.append(matrix[i][j])
        if len(check) == rows_m:
            r -= 1
        else:
            r += 1
    return r


res = rank()
print(f"Ранг матриці: {res}")


def determinant():
    # використовуємо цей код, бо так тоді визначник == добутку діагоналі матриці
    matrix = modul.input_matrix() 
    cols_m = len(matrix[0])
    rows_m = len(matrix)
    determinant = 1
    # перевірка чи взагалі можна перетворити матрицю на верхню квадратну матрицю 
    if rows_m != cols_m: 
        return "Цю матрицю не можна перетворити на верхню квадратну матрицю, оскільки кількість стовпчиків != кількості рядків"
    for i in range(rows_m):
        for j in range(i + 1, rows_m):
            # знайшли потрібний множник, але врахувавши знак
            num = - (matrix[j][i] / matrix[i][i]) 
            # потім домножили його на весь рядок даного рядка
            mat_cur = modul.multiplication_of_a_vector_by_a_number(matrix[i], num)
            # далі від цього рядка віднімаємо рядок інший і оновлюємо матрицю
            matrix[j] = modul.adding_a_vector_from_a_vector(matrix[j], mat_cur)
    for i in range(rows_m):
        determinant *= matrix[i][i]
    return determinant


res = determinant()
print(f"Визначник матриці: {res:.1f}")