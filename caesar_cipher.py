"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14925777
"""

word = input()
n = int(input())
new_word = ""
for i in word:
    if ord(i) - n < 65:
        new_i = chr(ord(i) - n + 26)
        new_word += new_i
    else:
        new_i = chr(ord(i) - n)
        new_word += new_i
print(new_word)