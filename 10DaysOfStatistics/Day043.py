l, r = list(map(float, input().split(" ")))
k = int(input())
prob = l/r


print(round(sum(prob*(1-prob)**(i-1) for i in range(1,k+1)),3))
