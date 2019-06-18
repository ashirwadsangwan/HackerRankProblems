def countSwaps(a):

    n = len(a)
    swaps = 0
    for i in range(n):
        for j in range(n-1):
            if a[j] > a[j+1]:
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
                swaps += 1
    return swaps

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    print("Array is sorted in {} swaps.".format(countSwaps(a)))
    print("First Element:", a[0])
    print("Last Element:",a[-1])
