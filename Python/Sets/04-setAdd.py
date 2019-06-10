N = int(input())

array = []
for i in range(N):
    array.append(input())
print(len(set(array)))

## alternate

print(len(set([str(input()) for x in range(int(input()))])))
