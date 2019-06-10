A = set(input().split())
n  = int(input())

print(all(A.issuperset(set(input().split()))==True for i in range(n)))
