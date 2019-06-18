def insertionSort2(n, arr):
    for i in range(1, n):
            value = arr[i]
            hole = i

            while (hole>0 and arr[hole-1]>value):
            
                arr[hole] = arr[hole-1]
                hole = hole-1
            arr[hole] = value
            print(*arr, sep = " ")
            

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
