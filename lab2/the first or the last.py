x = int(input())

x1 = x // 100
x3 = x % 10

if x1 > x3: 
    print (x1)
else:
    if x1 < x3:
        print(x3)
    else:
        print("=")
