"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14825905
"""

n, k = map(int, input().split())
array = [int(el) for el in input().split()]
sort_array = sorted(array)
result = sort_array[k - 1]
print(result)


lst_of_positives = [el for el in lst if el > 0]
if lst_of_positives:
    arithmetic_mean = sum(lst_of_positives) / len(lst_of_positives)
    print(f"{(arithmetic_mean):.2f}")
else: 
    print("Not Found")