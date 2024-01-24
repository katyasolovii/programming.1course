"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14455202
""" 

n = int(input())

for x in range(n):    
    x1 = int(input()) 
    if x1 % 2 == 0:
        print(f'{x1} is even')
    else:
        print(f'{x1} is odd')
