"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14470630
"""

n = int(input())
digits = [n]
while n != 0:
    n = int(input())
    digits.append(n)
print(sum(digits))

