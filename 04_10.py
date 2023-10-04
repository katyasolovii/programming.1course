n = int(input())
d = 1
for i in range(1, n + 1):
    if i % 8 == 0:
        d *= i
print(d)