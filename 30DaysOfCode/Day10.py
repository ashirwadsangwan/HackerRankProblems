if __name__ == '__main__':
    
    n = int(input())
    count = 0
   
    # Count the number of iterations to 
    # reach n = 0. 
    while (n!=0): 
      
        # This operation reduces length 
        # of every sequence of 1s by one. 
        n = (n & (n << 1)) 
   
        count += 1
      
    print(count) 
