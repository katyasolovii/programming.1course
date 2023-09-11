x,y  = map(float, input().split())

first_part = (x**2-2*x*y+4*y**2)/(x+5)
second_part = (3*x**2 - y**2)/(y-7)
print (f"{first_part + second_part:.3f}")