l, r = list(map(float, input().split(" ")))
k = int(input())
prob = l/r

print(round(prob*((1-prob)**(k-1)),3))
