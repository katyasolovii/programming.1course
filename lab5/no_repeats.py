"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14826448
"""

N = int(input())
array = [int(el) for el in input().split()]
array1 = []
for i in range(len(array)):
    el = array[i]
    if el not in array1: 
        array1.append(el)
print(*array1)