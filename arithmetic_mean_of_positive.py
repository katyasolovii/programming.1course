"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14954020
"""
n = int(input())
lst = [float(el) for el in input().split()]
lst_of_positives = [el for el in lst if el > 0]
if len(lst_of_positives) > 0:
    print(f"{(sum(lst_of_positives) / len(lst_of_positives)):.2f}")
else:
    print("Not Found")
    
