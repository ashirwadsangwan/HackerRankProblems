# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice, bob = 0, 0
    for i in range(3):
        if a[i]>b[i]:
            alice+=1
        elif a[i]==b[i]:
            pass
        else:
            bob += 1
    return alice, bob                


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
