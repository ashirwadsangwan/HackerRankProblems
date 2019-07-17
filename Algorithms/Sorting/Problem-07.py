#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr = sorted(arr)
    minAbsDiff = min([abs(i-j) for i, j in zip(arr, arr[1:])])
    new_arr = []
    for x, y in zip(arr, arr[1:]):
        if abs(x-y)==minAbsDiff:
            if x<y:
                new_arr.append(x)
                new_arr.append(y)
            else:
                new_arr.append(y)
                new_arr.append(x)
    return new_arr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
