"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14267592
"""

x = int(input())

if x >= 0:
    print(pow(x,3) + 2 * pow(x,2) + 4 * x - 6)
else:
    if x < 0:
       print(pow(x, 3) - 7 * x)
