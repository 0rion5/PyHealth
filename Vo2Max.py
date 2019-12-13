# -*- coding: utf-8 -*-
"""
@author: 0rion
"""

class VO2max:
    
    def __init__(self,age,gender,weight,walk_time_mins,heart_rate):
        self.age= age
        self.gender= gender
        self.weight= weight
        self.walk_time_mins= walk_time_mins
        self.heart_rate= heart_rate
    
    vo2max= lambda a,g,w,wtm,hr : 132.853-(0.0769 * w)-(0.3877 * a)+(6.315 * g)\
    -(3.2649 * wtm)-(0.156 * hr)    
    
    def VO2max(age,gender,weight,walk_time_mins,heart_rate):
        
        """
        Calculate your VO2 max using the following equation: 
        
            VO2 = 
        132.853 - (0.0769 x weight in lb) - (0.3877 x age)
        + (6.315 x gender) - (3.2649 x walk time in minutes)
        - (0.156 x heart rate) 
        
        If you are male, use the number 1, 
        if you are female, use the number 0 for the calculation.
        """
        
        VO2 = (132.853 - (0.0769 * weight)\
        -(0.3877 * age)+(6.315 * gender)\
        -(3.2649 * walk_time_mins)\
        -(0.156 * heart_rate))*-1
        print("\nVO2 Max: {} ml/kg/min".format(round(VO2, 2)))
        
        return VO2

# Define Vo2 max
def vo2max(age, HRrest):
    """Calculates vo2max"""
    HRmax= lambda x: 220-x 
    return round(15*(HRmax(age)/HRrest), 2)

# Main function gets user inputs and passes it to the class object method.
def main():
    """Collects user inputs to pass to Vo2Max.vo2max(age, HRrest) method."""
    # age in years
    age= int(input("How old are you? "))
    # Resting heart rate
    HRrest= int(input("Resting heart rate? "))
    VO2MAX= vo2max(age,HRrest)
    print("{VO2MAX} ml/kg/min")
    return VO2MAX


# Program Starts here
if __name__ == "__main__":
   VO2MAX =  main()
    
