k = int(input())
list_  = input().split()
dict_ = {}
for i in list_:
    if i not in dict_:
        dict_[i]=1
    else:
        dict_[i]+=1
for i, j in dict_.items():
    if j==1:
        print((i))
