def breakingRecords(scores):
    best_score = scores[0]
    worst_score = scores[0]
    best_increased = 0
    worse_decreased = 0

    for i in scores:
        if i>best_score:
            best_score = i
            best_increased += 1
        if i<worst_score:
            worst_score=i
            worse_decreased+=1
    return best_increased, worse_decreased
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
