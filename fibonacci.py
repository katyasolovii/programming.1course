"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15276755
"""


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def fibonacci(n, mod):
    k, l = 0, 1
    for _ in range(n):
        k, l = l, (k + l) % mod
    return k


modul = pow(10, 8)
while True:
    n, m = [int(el) for el in input().split()]
    res_gcd = gcd(n, m)
    print(fibonacci(res_gcd, modul))
    break
