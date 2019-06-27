def minimumAbsoluteDifference(arr):
    arr = sorted(arr)
    return min(abs(x-y) for x,y in zip(arr, arr[1:]))
