


# [Problem Solving](https://www.hackerrank.com/domains/algorithms?filters%5Bstatus%5D%5B%5D=unsolved&badge_type=problem-solving)



#### [Problem 4 : Staircase](https://www.hackerrank.com/challenges/staircase/problem)
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


 
#### [Problem 6 - Birthday Cake Candles](https://www.hackerrank.com/challenges/birthday-cake-candles/problem)

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



#### [Problem 9 : Apple and Orange](https://www.hackerrank.com/challenges/apple-and-orange/problem)

![alt text](https://s3.amazonaws.com/hr-challenge-images/25220/1474218925-f2a791d52c-Appleandorange2.png)
```python
def countApplesAndOranges(s, t, a, b, apples, oranges):

    app = 0
    org = 0

    app_list = []
    org_list = []

    for i in apples:
        app_list.append(a+i)
    for j in oranges:
        org_list.append(b+j)

    for k in app_list:
        if k>=s and k<=t:
            app+=1
    for m in org_list:
        if m>=s and m<=t:
            org+=1

    print(app)
    print(org) 
```    

#### [Problem 10 : Kangaroo](https://www.hackerrank.com/challenges/kangaroo/problem)
![alt text](https://s3.amazonaws.com/hr-assets/0/1516005283-e74e76ff0c-kangaroo.png)


```python
def kangaroo(x1, v1, x2, v2):

    if v1 == v2 and x1 == x2:
        return 'YES'
    elif v1 == v2:
        return 'NO'
     
    x = (x2-x1) / (v1-v2)    
    if (x == round(x) and x > 0):
        return 'YES'
    else:
        return 'NO'
```
