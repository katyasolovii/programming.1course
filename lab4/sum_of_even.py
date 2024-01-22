"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14571390
"""

n = int(input())
digits = [n]
summ = 0 
while n != 0:
    if n % 2 == 0:
        summ += n
    n = int(input())
    digits.append(n)
print(summ)
