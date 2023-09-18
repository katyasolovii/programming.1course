"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14222920
"""

a,b,n = map(int, input().split())

price = (a + (b / 100)) * n

print(int(price), int(round(price % 1 * 100, 2)))

