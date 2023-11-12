"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15098183
"""

a, b = [int(i) for i in input().split()]
uniq_digits = []
for num in range(a, b + 1):
    digits = str(num)
    if len(set(digits)) == len(digits):
        uniq_digits.append(digits)
print(*uniq_digits)
