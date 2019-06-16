# <center>Day 1 of 10 Days of Statistics</center>
This post is about the problems I solved in a tutorial from HackerRank and I have stated my approches to all the problems. 

### [Day 0: Mean, Median, and Mode](https://www.hackerrank.com/challenges/s10-basic-statistics/problem)
#### Task: 
Given an array,`X` , of `N` integers, calculate and print the respective mean, median, and mode on separate lines. If your array contains more than one modal value, choose the numerically smallest one.

```python

import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))

```

### [Day 0: Weighted Mean](https://www.hackerrank.com/challenges/s10-weighted-mean/problem)
#### Task:
Given an array, `X`, of `N` integers and an array, `W`, representing the respective weights of `X`'s elements, calculate and print the weighted mean of `X`'s elements. 

```python


N = map(int,input().split())
X = list(map(int, input().strip().split(' ')))
W = list(map(int, input().strip().split(' ')))
sum_X = sum([a*b for a,b in zip(X,W)])
print(round((sum_X/sum(W)),1))

```


