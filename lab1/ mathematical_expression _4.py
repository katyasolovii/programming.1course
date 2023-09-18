import math
x, y  = map(float, input().split())
first_part = (2*x*y)/(math.sqrt(pow(x, 2)+ pow(y, 2)))
second_part = pow(x+y-1, 2) / (x*y)
print (f"{first_part - second_part:.3f}")
