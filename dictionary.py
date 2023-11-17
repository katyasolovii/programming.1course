"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15168406
"""

n = int(input())
d = {}
rev_d = {}

# введення даних
for _ in range(n):
    key, values_str = input().split(" - ")
    values = values_str.split(", ")
    d[key] = values
    for value in values:
        if value not in rev_d:
            rev_d[value] = []
        rev_d[value].append(key)
print(len(rev_d))

for value, words in sorted(rev_d.items()):
    print(f"{value} - {', '.join(words)}")