"""
Посилання на розв'язок: https://www.eolymp.com/uk/submissions/15072567
"""
#60 * 3 = НСК(P, Q) * НСД(P, Q)
#180 = P * Q
#(1,180),(2,90),(3,60),(4,45),(5,36),(6,30),(9,20),(10,18),(12,15),
#(15,12),(18,10),(20,9),(30,6),(36,5),(45,4),(60,3),(90,2),(180,1)
#(3,60),(5,36),(6,30),(9,20) задовільняють (4)
#алгоритм Евкліда
import math
def find_gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
def find_pairs(A, B):
    gcdPQ_lcmPQ = A * B
    pairs = set()
    for P in range(1, gcdPQ_lcmPQ + 1):
        if gcdPQ_lcmPQ % P == 0:
            Q = gcdPQ_lcmPQ // P
            if find_gcd(P, Q) == A:
                pairs.add((P, Q))
                pairs.add((Q, P))
    return len(pairs)
A,B = [int(n) for n in input().split()]
print(find_pairs(A,B))