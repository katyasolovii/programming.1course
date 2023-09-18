Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14199030
"""

from math import sqrt

a,b,c,d,f = [float (x) for x in input(). split()]

p1 = (a + b + f) / 2
p2 = (f + d + c) / 2

s1 = sqrt(p1 * (p1 - a) * (p1 - b) * (p1 - f)) 
s2 = sqrt(p2 * (p2 - f) * (p2 - d) * (p2 - c)) 

print(s1 + s2)
