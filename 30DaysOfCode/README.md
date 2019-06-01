# [30 Days of Code](https://www.hackerrank.com/domains/tutorials/30-days-of-code?filters%5Bsubdomains%5D%5B%5D=30-days-of-code&badge_type=30-days-of-code)

## Day 1
### Data Types
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
