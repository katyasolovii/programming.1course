"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15193281
"""


def f(n):
    if n % 10 > 0:
        return n % 10
    elif n == 0:
        return 0
    else:
        return f(n // 10)

def summ(p, q):
    return sum(f(n) for n in range(p, q + 1))

results = [] 

while True:
    p, q = [int(el) for el in input().split()]
    if p < 0 and q < 0:
        break
    results.append(summ(p, q))
for result in results:
    print(result)