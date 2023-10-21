"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14826474
"""

n = int(input())
array_n = [int(el) for el in input().split()]
m = int(input())
array_m = [int(el) for el in input().split()]
array = [el for el in array_n if el not in array_m]
print(len(array))
print(*array)