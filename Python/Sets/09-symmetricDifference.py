english = int(input())
eng_roll = input().split()
french = int(input())
fr_roll = input().split()

print(len(set(eng_roll)^(set(fr_roll))))
