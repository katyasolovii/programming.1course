"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15168443
"""

unique_a = set(input())
unique_b = set(input() )
letters = []
for i in unique_b:
    if i in unique_a:
        letters.append(i)
if len(letters) == len(unique_b):
        print("Ok")
else:
    print("No")