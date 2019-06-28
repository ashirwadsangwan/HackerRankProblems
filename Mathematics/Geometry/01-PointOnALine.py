if __name__ == '__main__':
    n = int(input())
    odd = []
    even = []
        
    for n_itr in range(n):
        xy = input().split()
        
        x = int(xy[0])

        y = int(xy[1])

       
        odd.append(x)
    
        even.append(y)

        odd = sorted(odd)
        even = sorted(even)

    if odd[0]==odd[-1]:
        
        print("YES")
    elif even[0]==even[-1]:
        print("YES")
    else:
        print("NO")
