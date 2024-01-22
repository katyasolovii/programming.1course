"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15076500
"""


def convert(n, k):
    res_con = ""
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n == 0:
        res_con = "0"
    while n > 0:
        index = n % k
        res_con += alphabet[index]
        n //= k
    return res_con[::-1]


m, k = [int(i) for i in input().split()]
n_str = input().strip() #видаляє space напочатку і вкінці 
n = int(n_str, m) #конвертація рядка в ціле число(m означає систему числення, у нашому випадку десяткова)
print(convert(n, k))
