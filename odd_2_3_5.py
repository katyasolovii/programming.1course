"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14461452
"""

n = int(input())
i = 0
count = 0 #кількість чисел, які не діляться на 2, 3, 5
while count < n:
    i += 1
    if (i % 2 != 0 
        and i % 3 != 0 
        and i % 5 != 0):
        print(i, end=" ")
        count += 1