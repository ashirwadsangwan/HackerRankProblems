n = int(input())
array = list(map(int, input().split()))

mean = sum(array)/n
variance = sum((i-mean)**2 for i in array)/n
def sqrt(x): return x**(1/2)

print("{:.1f}".format(sqrt(variance)))
