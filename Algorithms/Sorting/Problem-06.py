def runningTime(arr):
    
    swaps = 0
    
    for i in range(len(arr)):

        target = arr[i]
        hole = i
        
        while (hole>0 and arr[hole-1]>target):

            arr[hole] = arr[hole-1]
            swaps+=1
            hole -=1
        arr[hole] = target
        
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = runningTime(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
