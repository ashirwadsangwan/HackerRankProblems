from statistics import median

n = int(input())
X = input().split()
F = input().split()

array = []

for i in range(n):
    array+=([X[i]] * int(F[i]))

array = [int(x) for x in array]
array = sorted(array)

t=int(len(array)/2)
if len(array)%2==0:
    L=array[:t]
    U=array[t:]
else:
    L=array[:t]
    U=array[t+1:]
    
print("{:.1f}".format((int(median(U))-int(median(L)))))

