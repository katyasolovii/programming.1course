"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14930316
"""

word = input()
new_word = ""
for letter in word:
    if letter.isalnum():
        new_word += letter * 2
    else:
        new_word += letter
print(new_word)