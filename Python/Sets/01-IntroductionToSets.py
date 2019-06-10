def average(array):
    
    arr = list(set(array))
    return (sum(arr)/len(arr))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
