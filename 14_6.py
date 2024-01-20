#Р озв’язати квадратне рівняння ax^2+bx+c=0. Оформити перевірку вхідних даних (що рівняння є квадратним і 
# має розв’язок на множині дійсних чисел) за допомогою оператора assert.


def solution(a, b, c):
    assert a != 0, "AssertionError: рівняння не має розв'язків"
    discriminant = pow(b, 2) - 4 * a * c
    assert discriminant >= 0, "AssertionError: рівняння не має розв'язків на множині дійсних чисел"
    if discriminant == 0:
        x1 = -b / 2 * a
        return x1
    else:
        x1 = (-b + pow(discriminant, 2)) / 2 * a
        x2 = (-b - pow(discriminant, 2)) / 2 * a
        return x1, x2
    
a, b, c = [float(el) for el in input().split()]
try:
    print(solution(a, b, c))
except AssertionError as e:
    print(e)