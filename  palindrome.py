"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14930398
"""

word = input()
word_without_gap = word.replace(" ", "")
rev_word = word_without_gap[::-1]
if rev_word == word_without_gap:
    print("YES")
else: 
    print("NO")