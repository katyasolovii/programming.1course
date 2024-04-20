import modul


def upper_triangular(matrix):
    # спочатку, віднімемо перший рядок помножений на такий множник, щоб у другому рядку перший стовпик став 0 від другого
    # далі, те саме робимо тільки відмнімаємо від третього рядка
    # потім, переходимо до другого рядка і від нього помноженого на такий множник, щоб у третьому рядку другий стовпик став 0  від третього
    # всьо, + треба кожен раз шукати спеціальний множик +++ треба ще визначити знак
    # 4 12 8    + *(-2)   4 12 8          + *(-1/2)    4 12 8                      4 12 8 
    # 8 7 1               0 -17 -15                    0 -17 -15      + *3/17      0 -17 -15
    # 2 9 5               2 9 5                        0 3 1                       0 0 -28/17 
    cols_m = len(matrix[0])
    rows_m = len(matrix)
    for i in range(rows_m):
        if matrix[i][i] == 0:
            for k in range(i + 1, rows_m):
                if matrix[k][i] != 0:
                    modul.swap_rows(matrix, i, k)
                else:   
                    continue
        for j in range(i + 1, rows_m):
            # знайшли потрібний множник, але врахувавши знак
            num =  - (matrix[j][i] / matrix[i][i])
            # потім домножили його на весь рядок даного рядка
            mat_cur = modul.multiplication(matrix[i], num)
            # далі від цього рядка віднімаємо рядок інший і оновлюємо матрицю
            matrix[j] = modul.add(matrix[j], mat_cur)
    return modul.print_matrix(matrix)


matrix = modul.input_matrix()
res = upper_triangular(matrix)
print(res)


def rank(matrix):
    upper_triangular(matrix) 
    rows_m = len(matrix)
    r = 0
    for row in matrix:
        if all(el == 0 for el in row):
            r += 1
    res_r = rows_m - r
    return res_r


matrix = modul.input_matrix()
res = rank(matrix)
print(f"Ранг матриці: {res}")


def determinant():
    # використовуємо цей код, бо так тоді визначник == добутку діагоналі матриці
    upper_triangular(matrix) 
    rows_m = len(matrix)
    determinant = 1
    for i in range(rows_m):
        determinant *= matrix[i][i]
    return determinant


matrix = modul.input_matrix()
res = determinant()
print(f"Визначник матриці: {res:.1f}")
