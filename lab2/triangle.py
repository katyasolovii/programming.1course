a,b,c = map(int, input().split())

if a == b == c:
    print(1)
else:
    if a == b or a == c or b == c:
        print(2)
    else:
        if a != b and a != c and b != c:
            print(3)


"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/14267677
