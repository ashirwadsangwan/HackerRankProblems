import os
import sys

#
# Complete the gradingStudents function below.
#
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

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grades = []

    for _ in range(n):
        grades_item = int(input())
        grades.append(grades_item)

    result = gradingStudents(grades)

    f.write('\n'.join(map(str, result)))
    f.write('\n')

    f.close()
