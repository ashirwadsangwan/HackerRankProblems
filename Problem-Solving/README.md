


## [Problem 1 : Diagonal Difference](https://www.hackerrank.com/challenges/diagonal-difference/problem)
```python
def diagonalDifference(arr):
    
    '''
    arr is a n x n matrix.
    '''
    main_diag = 0
    alt_diag = 0
    for i in range(0,n):
        main_diag += arr[i][i]
        alt_diag += arr[i][n-1-i]

    return abs(main_diag-alt_diag)
  ```


## [Problem 2 : Comparing Triplets](https://www.hackerrank.com/challenges/compare-the-triplets/problem)

```python

def compareTriplets(a, b):

    '''
    a: Alice's score out of 100
    b: Bob's score out of 100
    '''
    alice, bob = 0, 0
    for i in range(3):
        if a[i]>b[i]:
            alice+=1
        elif a[i]==b[i]:
            pass
        else:
            bob += 1
    return alice, bob    
    
  ```
  
  ## [Problem 3 : Plus Minus](https://www.hackerrank.com/challenges/plus-minus/problem)
Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

```python
def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zero+=1
    print(pos/len(arr))
    print(neg/len(arr))
    print(zero/len(arr))   
```


## [Problem 4 : Staircase](https://www.hackerrank.com/challenges/staircase/problem)
 ```   
       #
      ##
     ###
    ####
```
Observe that its base and height are both equal to `n` , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size `n` .

```python

def staircase(n):
    
    for i in range(1,n+1):
        
        print((n-i)*' '+'#'*i)
```

## [Problem 5 : Mini-Max Sum](https://www.hackerrank.com/challenges/mini-max-sum/problem)

Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

```python

def miniMaxSum(arr):

    min_sum = 0
    max_sum = 0

    for i in arr:
        if i == max(arr):
            pass
        else:
            min_sum+=i
    for i in arr:
        if i == min(arr):
            pass
        else:
            max_sum += i

    if min(arr)==max(arr):
        max_sum = 4*min(arr)
        min_sum  = 4*min(arr)           

    print(min_sum, max_sum)      
```
## [Problem 6 - Birthday Cake Candles](https://www.hackerrank.com/challenges/birthday-cake-candles/problem)

You are in charge of the cake for your niece's birthday and have decided the cake will have one candle for each year of her total age. When she blows out the candles, she’ll only be able to blow out the tallest ones. Your task is to find out how many candles she can successfully blow out.

```python

def birthdayCakeCandles(ar):

    dict_ = {}
    for i in ar:
        if i not in dict_:
            dict_[i]=1
        else:
            dict_[i]+=1
    return max(dict_.values())        
    
```

## [Problem 7 : Time Conversion](https://www.hackerrank.com/challenges/time-conversion/problem)

```python

def timeConversion(s):
    
    if s[-2:] == "AM" and s[:2] == "12": 
        return "00" + s[2:-2] 
          
    # remove the AM     
    elif s[-2:] == "AM": 
        return s[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif s[-2:] == "PM" and s[:2] == "12": 
        return s[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(s[:2]) + 12) + s[2:8] 
```
## [Problem 8 : Grading System](https://www.hackerrank.com/challenges/grading/problem)

```python
def gradingStudents(grades):
    
    rounded_grades = []
    for i in grades:

        if i<38:
            rounded_grades.append(i)

        elif i>=38 and ((i+1)%5==0):
            rounded_grades.append(i+1)

        elif i>=38 and ((i+2)%5==0):
            rounded_grades.append(i+2)
        
        else:
            rounded_grades.append(i)

    return rounded_grades
```
