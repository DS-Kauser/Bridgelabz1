import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz/Week1')             # helps in importing function from utility

# importing distance_from_origin function from utility
from Utility.utility import distance_from_origin                        

if __name__ == '__main__' :                                             
    
    while True:                                                         
        
        try:
            # taking x and y value from user                                                            
            abcissa = float(input("Enter x-value : "))                  
            ordinate = float(input("Enter y-value: "))                  
            
            # passing the argument in the function to calculate distance
            dist = distance_from_origin(abcissa, ordinate)              
            print(dist)
            break                                                       
        
        except:
            print("Enter a valid input")                                