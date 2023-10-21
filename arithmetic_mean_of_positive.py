"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14825417
"""

n = int(input())
lst = [float(el) for el in input().split()]
lst_of_positives = [el for el in lst if el > 0]
lst_of_neg = [el for el in lst if el < 0]
if len(lst_of_neg) == len(lst):
    print("Not Found")
else:
    print(f"{(sum(lst_of_positives) / len(lst_of_positives)):.2f}")