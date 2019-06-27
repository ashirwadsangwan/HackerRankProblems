import math

def isPrime(n):
    if n==2 or n==3: return "Prime"
    if n%2==0 or n<2: return "Not prime"
    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return "Not prime"   

    return "Prime"



n = int(input())
for i in range(n):
    print(isPrime(int(input())))
