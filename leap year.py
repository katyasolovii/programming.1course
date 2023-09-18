x = int(input())
if x % 4 == 0 and x % 100 != 0:
    print("YES")
else:
    if x % 400 == 0:
        print("YES")
    else: 
        print("NO")