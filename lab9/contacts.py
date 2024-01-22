"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15038070
"""

n = int(input())
phone_numbers = [int(el) for el in input().split()]
contacts = set(phone_numbers)
print(len(contacts))