## [Problem 1](https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup)

John works at a clothing store. He has a large pile of socks that he must pair by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.

For example, there are `n=7` socks with colors `ar = [1,2,1,2,1,3,2]` . There is one pair of color 1 and one of color 2 . There are three odd socks left, one of each color. The number of pairs is 2Function Description


```
sockMerchant has the following parameter(s):

* n: the number of socks in the pile
* ar: the colors of each sock.
```
#### Input Format

The first line contains `n` an integer , the number of socks represented in `ar` . 
The second line contains `n` space-separated integers describing the colors `ar[i]` of the socks in the pile.


#### Output Format

Return the total number of matching pairs of socks that John can sell.

```python
def sockMerchant(n, ar):

    '''
    Creates a Dictionary of all the number in the array and then accordingly
    return the duplets.
    '''
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
```
