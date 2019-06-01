# Complete the sockMerchant function below.

def sockMerchant(n, ar):
    num = {}
    for i in ar:
        if i not in num:
            num[i]=1
        else:
            num[i]+=1

    duplets = 0
    for i in num.values():
        duplets+=(i//2)
    return duplets               


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
