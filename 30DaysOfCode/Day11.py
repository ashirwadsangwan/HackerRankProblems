if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    my_hourglasses = list()

    for i in range(0,4):
        for j in range(0,4):
            hourglass = list()
            hourglass += arr[i][j:j+3]
            hourglass.append(arr[i+1][j+1])
            hourglass += arr[i+2][j:j+3]
            my_hourglasses.append(hourglass)

    hourglasses_sums = [sum(item) for item in my_hourglasses]

    print(max(hourglasses_sums))
