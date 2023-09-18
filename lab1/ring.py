import math
s, R = map(float, input().split())
r = math.sqrt(pow(R, 2) - (s / math.pi))
print (f"{r:.2f}")
