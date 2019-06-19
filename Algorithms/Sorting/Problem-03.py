def insertionSort1(n, arr):
    
    target = arr[-1]
    hole = n-2

    while (target < arr[hole]) and (hole >= 0):
        arr[hole+1] = arr[hole]
        print(*arr)
        hole -= 1

    arr[hole+1] = target
    
    print(*arr, sep = " ")

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
