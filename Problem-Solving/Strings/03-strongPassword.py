def minimumNumber(n, password):
    

    num = 0
    if any(i.isdigit() for i in password)==False:
        num+=1
    if any(i.islower() for i in password)==False:
        num+=1
    if any(i.isupper() for i in password)==False:
        num+=1
    if any(i in "!@#$%^&*()-+" for i in password)==False:
        num+=1
    
    return (max(num, 6-n))



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
