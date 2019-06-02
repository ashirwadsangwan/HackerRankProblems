def timeConversion(s):
    
    if s[-2:] == "AM" and s[:2] == "12": 
        return "00" + s[2:-2] 
          
    # remove the AM     
    elif s[-2:] == "AM": 
        return s[:-2] 
      
    # Checking if last two elements of time 
    # is PM and first two elements are 12    
    elif s[-2:] == "PM" and s[:2] == "12": 
        return s[:-2] 
          
    else: 
          
        # add 12 to hours and remove PM 
        return str(int(s[:2]) + 12) + s[2:8] 
