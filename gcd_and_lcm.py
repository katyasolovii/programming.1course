"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15097681
"""
# 60 * 3 = НСК(P, Q) * НСД(P, Q)
# 180 = P * Q
# (1,180),(2,90),(3,60),(4,45),(5,36),(6,30),(9,20),(10,18),(12,15),
# (15,12),(18,10),(20,9),(30,6),(36,5),(45,4),(60,3),(90,2),(180,1)
# (3,60),(5,36),(6,30),(9,20) задовільняють (4)
# алгоритм Евкліда


def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def find_pairs(a, b):
    gcdPQ_lcmPQ = a * b
    pairs = set()
    for p in range(1, int(gcdPQ_lcmPQ ** 0.5) + 1):
        if gcdPQ_lcmPQ % p == 0:
            q = gcdPQ_lcmPQ // p
            if find_gcd(p, q) == q:
                pairs.add((p, q))
                pairs.add((q, p))
    return len(pairs)


a,b = [int(n) for n in input().split()]
print(find_pairs(a,b))
