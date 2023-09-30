"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14378723
"""

n = int(input())
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(len(str(factorial)))