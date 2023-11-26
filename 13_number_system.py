"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15112188
"""


def convert(n):
    res_con = ""
    alphabet = "0123456789ABC"
    if n == 0:
        return "0"
    while n > 0:
        index = n % 13
        res_con += alphabet[index]
        n //= 13
    return res_con[::-1]



n = int(input())
print(convert(n))