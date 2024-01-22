"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15076431
"""


def convert(n, m):
    res_con = ""
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0: 
        res_con = "0"
    while n > 0:
        index = n % m
        res_con += alphabet[index]
        n //= m
    return res_con


def palindrome(s):
    return s == s[::-1]


n_str = input().strip() 
n = int(n_str, 10) 
bases = []
for i in range(2, 37):
    convert_n = convert(n, i)
    if palindrome(convert_n):
        bases.append(i)
if not bases:
    print("none")
elif len(bases) == 1:
    print("unique")
    print(bases[0])
else:
    print("multiple")
    print(" ".join(map(str, bases)))
