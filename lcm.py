"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15098203
"""
# gcd - НСД
# lcm - НСК; НСК(a;b) = a * b // НСД(a,b)


def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def lcm(n):
    a = 1
    for b in range(1, n + 1):
        a = a * b // find_gcd(a, b)
    return a


n = int(input())
print(lcm(n))
