import sys
sys.path.append('/home/user/Desktop/Mack/BridgeLabz/Week1')         # helps in importing function from utility

# importing find_leap_year from utility
from Utility.utility import find_leap_year                          

if __name__ == '__main__':                                          
    
    while True:                                                     
        try:
            # taking year from user input                                                        
            year = int(input("Enter year : "))                      
            
            # passing year as argument in find_leap_year
            find_leap_year(year)                                    
            break                                                   
        
        except:
            print("Enter Valid Input")                              