"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15111916
"""


def convert(n, m):
    res_con = ""
    alphabet = "01"
    while n > 0:
        index = n % m
        res_con += alphabet[index]
        n //= m
    return res_con[::-1]


def exponentiation(n):
    new_symbols = ""
    for i in convert(n, m):
        if i == "1":
            new_symbols += "SX"
        else:
            new_symbols += "S"
    symbols = new_symbols[2:]
    return symbols


m = 2
n = int(input())
print(exponentiation(n))