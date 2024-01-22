"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15159102
"""

n = int(input())
numebrs = (int(num) for num in input().split())
uniq_num = set(abs(num) for num in numebrs)
print(len(uniq_num))