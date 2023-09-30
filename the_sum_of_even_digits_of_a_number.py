"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14474468
"""
digits = input()
summ = 0 
for n in digits:
    if int(n) % 2 == 0:
        summ += int(n)
if summ > 0 or int(n) == 0:
    print(summ)
else:
    print(-1)
