"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14475682
"""

n = int(input())
i = 2
while i < n:
    if n // i != 1:
        n = n // i
        i += 1
print(n)

    

    