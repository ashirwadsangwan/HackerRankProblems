# [30 Days of Code](https://www.hackerrank.com/domains/tutorials/30-days-of-code?filters%5Bsubdomains%5D%5B%5D=30-days-of-code&badge_type=30-days-of-code)

## Day 1
### Data Types

The variables `i`, `d`, and `s` are already declared and initialized for you. You must:

1. Declare `3` variables: one of type int, one of type double, and one of type String.
2. Read `3` lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your    `3` variables.
3. Use the  operator to perform the following operations: 

    ```
    1. Print the sum of `i` plus your int variable on a new line.
    2. Print the sum of `d` plus your double variable to a scale of one decimal place on a new line.
    3. Concatenate `s` with the string you read as input and print the result on a new line.
    ```

```python
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.

int2 = int(input())
double = float(input())
string = str(input())

# Read and save an integer, double, and String to your variables.

# Print the sum of both integer variables on a new line.

print(i + int2)

# Print the sum of the double variables on a new line.

print(d + double)

# Concatenate and print the String variables on a new line

print(s + string)
```


## Day 4 
### Class vs Instance

Write a Person class with an instance variable, `age`, and a constructor that takes an integer, `initialAge`, as a parameter. 
The constructor must assign `initialAge` to `age` after confirming the argument passed as `initialAge` is not negative; if a negative argument is
passed as `initialAge`, the constructor should set `age` to `0` and print `Age is not valid, setting age to 0.`. In addition, you must write
the following instance methods:

1. `yearPasses()` should increase the `age` instance variable by 1.
2. `amIOld()` should perform the following conditional actions:

    ```
    If age < 13, print You are young..
    If age >= 13 and age < 18 , print You are a teenager..
    Otherwise, print You are old..
    ```
    
```python    

class Person:

    def __init__(self,initialAge):
        if initialAge > 0 :
            self.initialAge = initialAge
        else:
            print('Age is not valid, setting age to 0.')
            self.initialAge = 0
        
    def amIOld(self):
        if self.initialAge < 13:
            print('You are young.')
        elif self.initialAge >=13 and self.initialAge < 18:
            print('You are a teenager.')
        else:
            print('You are old.')
        
    def yearPasses(self):
        # Increment the age of the person in here
        self.initialAge+=1
        
        
```        


## Day 7
### Arrays

Given an array, `A`, of `N` integers, print `A`'s elements in reverse order as a single line of space-separated numbers.


```python

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    des_n = n-1
    reverse_array = []
    
    while des_n >= 0:
        reverse_array.append(arr[des_n])
        des_n -= 1
   
    for i in reverse_array:
        print(i, end=' ')
        
```
