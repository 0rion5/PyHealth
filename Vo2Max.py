# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:21:07 2019

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
        
        VO2 = 132.853 - (0.0769 * weight)\
        -(0.3877 * age)+(6.315 * gender)\
        -(3.2649 * walk_time_mins)\
        -(0.156 * heart_rate)
        print("\nVO2 Max: {} ml/kg/min".format(round(VO2, 2)))
        
        return VO2
    
    def VO2max_basic():
        HRmax= lambda x: 220-x
        HRmax= HRmax(int(input("Your age: ")))
        HRrest= int(input("Your resting heart rate: ")) 
        return round(15*(HRmax/HRrest), 2)

# Start Program
if __name__ == "__main__":
    # age in years
    age= int(input("Enter Age: "))
    
    # Gender M/F
    while True:
        gender= input("Enter Gender: ")
        if gender[0::].lower() == 'f':
            gender= 0
            break
        elif gender == 'm':
            gender= 1
            break
        else: continue
    
    # weight in lbs
    weight= int(input("Weight lbs "))
    
    # walk time in mins
    walk_time_mins= int(input("Walk time in mins: "))
    
    # heart rate
    heart_rate= int(input("heart rate: "))
    
    VO2max= VO2max.VO2max(age,gender,weight,walk_time_mins,heart_rate)