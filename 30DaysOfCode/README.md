# [30 Days of Code]()

## Day 4

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
