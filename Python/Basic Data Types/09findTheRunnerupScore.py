if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_array = list(set(sorted(arr)))
    sorted_array.remove(max(sorted_array))
    print(max(sorted_array))
