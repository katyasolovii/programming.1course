"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14996593
"""
#gcd - НСД
#lcm - НСК; НСК(a;b) = a * b // НСД(a,b)
import math

def lcm(n):
    a = 1
    for b in range(1, n + 1):
        a = a * b // math.gcd(a, b)
    return a
n = int(input())
print(lcm(n))