## Solution 1

from functools import reduce
from operator import xor

def lonely_integer(a):
    return reduce(xor, a)
    
## Solution 2 It's basically same as 1 without importing anything.

def lonelyinteger(a):
    lonely_int = 0
    for i in a:
        lonely_int^=i
    
    return lonely_int
    
## Solution 3

def lonelyinteger(a):
    dict_ = {}
    for i in a:
        if i not in dict_:
            dict_[i]=1
        else:
            dict_[i]+=1
    
    lonely_int = 0
    for key in dict_.keys():
        if dict_[key]==1:
            lonely_int = key
    
    return lonely_int
