def introTutorial(V, arr):

    low = 0
    high  = len(arr)-1
    while(low<=high):
        mid = (low+high)//2

        if V == arr[mid]:
            return mid
        elif V >= arr[mid]:
            low = mid+1
        else:
            high = mid-1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
