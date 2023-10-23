"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14826223
"""

n = int(input())
lst = [int(el) for el in input().split()]
result = [lst[-1]] + lst[:-1] #останній елемент списка + список від 1 до передостаннього елемента 
print(*result)