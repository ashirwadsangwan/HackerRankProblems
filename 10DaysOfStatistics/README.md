# <center>10 Days of Statistics</center>
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
### [Day 1: Quartiles](https://www.hackerrank.com/challenges/s10-quartiles/problem)
#### Task:
Given an array,`X` , of `n` integers, calculate the respective first quartile (`Q1`), second quartile (`Q2`), and third quartile (`Q3`). It is guaranteed that `Q1`, `Q2`, and `Q3` are integers.

```python

from statistics import median
n=int(input())
arr=[int(x) for x in input().split()]
arr.sort()
t=int(len(arr)/2)
if len(arr)%2==0:
    L=arr[:t]
    U=arr[t:]
else:
    L=arr[:t]
    U=arr[t+1:]
    
print(int(median(L)))
print(int(median(arr)))
print(int(median(U)))

```

### [Day 1: Interquartile Range](https://www.hackerrank.com/challenges/s10-interquartile-range/problem)

```python

from statistics import median

n = int(input())
X = input().split()
F = input().split()

array = []

for i in range(n):
    array+=([X[i]] * int(F[i]))

array = [int(x) for x in array]
array = sorted(array)

t=int(len(array)/2)
if len(array)%2==0:
    L=array[:t]
    U=array[t:]
else:
    L=array[:t]
    U=array[t+1:]
    
print("{:.1f}".format((int(median(U))-int(median(L)))))



```

### [Day 1: Standard Deviation](https://www.hackerrank.com/challenges/s10-standard-deviation/problem)

```python

n = int(input())
array = list(map(int, input().split()))

mean = sum(array)/n
variance = sum((i-mean)**2 for i in array)/n
def sqrt(x): return x**(1/2)

print("{:.1f}".format(sqrt(variance)))

```

### [Day 2: Basic Probability](https://www.hackerrank.com/challenges/s10-mcq-1/problem)
#### Task:
In a single toss of `2` fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most `9`.

```
There are only 6 options when the sum could be more than 9 i.e. (4,6),(5,5),(5,6),(6,4),(6,5),(6,6).
So, in 30 of 36 cases the sum is maximum 9. 

=> Prob = 30/36 = 5/6

```

### [Day 2: More Dice](https://www.hackerrank.com/challenges/s10-mcq-2/problem)
#### Task:
In a single toss of `2` fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be different and the two dice have a sum of `6`.

```
The cases when the sum of two dice is 6 and when the numbers on both dice is different are: (1,5),(2,4),(4,2),(5,1)
And we have a total of 36 cases.
=> Prob = 4/36 = 1/9

```

### [Day 2: Compound Event Probability](https://www.hackerrank.com/challenges/s10-mcq-3/problem)
#### Task:
There are `3` urns labeled `X`, `Y`, and `Z`. 


Urn `X` contains `4` red balls and `3` black balls.
Urn `Y` contains `5` red balls and `4` black balls.
Urn `Z` contains `4` red balls and `4` black balls. 

One ball is drawn from each of the `3` urns. What is the probability that, of the `3` balls drawn, `2` are red and `1` is black?

```
Urn X has a 4/7 probability of giving a red ball
Urn Y has a 5/9 probability of giving a red ball
Urn Z has a 1/2 probability of giving a red ball

Urn X has a 3/7 probability of giving a black ball
Urn Y has a 4/9 probability of giving a black ball
Urn Z has a 1/2 probability of giving a black ball

=> P(2 red, 1 black) 
=> P(Red Red Black) + P(Red Black Red) + P(Black Red Red)
=> (4/7)*(5/9)*(1/2) + (4/7)*(4/9)*(1/2) + (3/7)*(5/9)*(1/2)
=> 20/126 + 16/126 + 15/126 
=> 51/126 
=> 17/42

```




