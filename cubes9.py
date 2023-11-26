"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15037615
"""

n = int(input())
symbols = input()
new_symbols = {}
for letter in symbols:
    if letter in new_symbols:
        new_symbols[letter] += 1
    else:
        new_symbols[letter] = 1
for letter, count in new_symbols.items():
    if count % 2 == 1:
        print(letter)
        break
else:
    print("Ok")   
