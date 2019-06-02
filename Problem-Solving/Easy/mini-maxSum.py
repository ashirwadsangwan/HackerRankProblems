'''
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the
five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
'''
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
