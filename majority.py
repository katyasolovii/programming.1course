"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15169423
"""

n = int(input())
res = []

for _ in range(n):
    count_voices = int(input())
    count_digits = {} # власний словник кожного набору цифр
    for _ in range(count_voices):
        digits = int(input())
        count_digits[digits] = count_digits.get(digits, 0) + 1
    max_count = max(count_digits.values())
    max_digits = [key for key, value in count_digits.items() 
                  if value == max_count] # додає пари (ключ-значення) у список ,якщо значення == max_count
    if len(max_digits) == 1:
        res.append(max_digits[0])
    else:
        res.append(min(max_digits))
print(*res, sep='\n')