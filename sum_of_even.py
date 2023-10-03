"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14530963
"""

n = int(input())
digits = [n]
summ = 0 
while n != 0:
    n = int(input())
    digits.append(n)
for n in digits:
    if n % 2 == 0:
        summ += n
print(summ)