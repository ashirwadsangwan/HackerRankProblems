def diagonalDifference(arr):
    main_diag = 0
    alt_diag = 0
    for i in range(0,n):
        main_diag += arr[i][i]
        alt_diag += arr[i][n-1-i]

    return abs(main_diag-alt_diag)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
