def maximumToys(prices, k):
    
    prices = sorted(prices)
    
    toys = []
    for i in range(len(prices)):
        while (k-prices[i])>=0:
            toys.append(i)
            k -= prices[i]  
            break
            
    return len(toys)
     
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
