def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zero+=1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zero/len(arr)) 
