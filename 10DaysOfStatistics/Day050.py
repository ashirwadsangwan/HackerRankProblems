import math

lam = float(input())
k = int(input())

def fact(n): return 1 if n==0 else n*fact(n-1)

prob = math.exp(-lam)*(lam**k)/fact(k)

print(round(prob, 3))
