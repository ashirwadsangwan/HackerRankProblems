if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    des_n = n-1
    reverse_array = []
    
    while des_n >= 0:
        reverse_array.append(arr[des_n])
        des_n -= 1
   
    for i in reverse_array:
        print(i, end=' ')
