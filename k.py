"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14825905
"""

n, k = map(int, input().split())
array = [int(el) for el in input().split()]
sort_array = sorted(array)
result = sort_array[k - 1]
print(result)
