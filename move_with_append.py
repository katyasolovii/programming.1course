"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14826184
"""

n = int(input())
lst = [int(el) for el in input().split()]
lst1 = []
for i in range(len(lst)):
    el = lst[i]
    el1 = lst[i - 1]
    lst1.append(el1)
print(*lst1)