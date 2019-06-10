M = int(input())
set_M = set(input().split())
N = int(input())
set_N = set(input().split())


[print(i) for i in sorted(set_M^set_N, key = int)]
