"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14404196
"""

n = int(input())
new_d = 0 
i = 0
while n:
    last = n % 10
    if last % 2 == 0:
        last += 1
    else:
        last -= 1
    new_d += last * pow(10, i)
    n = n // 10
    i += 1
print(new_d)



