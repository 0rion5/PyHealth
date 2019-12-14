# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:21:07 2019

@author: 0rion

"""
class Vo2Max:
    

    def vo2max(age,gender,weight,walk_time_mins,heart_rate):
        
        """
        Calculate your VO2 max using the following equation: 
        
            VO2 = 
        132.853 - (0.0769 x weight in lb) - (0.3877 x age)
        + (6.315 x gender) - (3.2649 x walk time in minutes)
        - (0.156 x heart rate) 
        
        If you are male, use the number 1, 
        if you are female, use the number 0 for the calculation.
        """
        
        VO2 = 132.853 - (0.0769 * float(weight))\
        -(0.3877 * age)+(6.315 * gender)\
        -(3.2649 * walk_time_mins)\
        -(0.156 * heart_rate)
        print("\nVO2 Max: {} ml/kg/min".format(round(VO2, 2)))
        
        return VO2


    def Vo2Max():
        HRmax= lambda x: 220-x
        HRmax= HRmax(int(input("Your age: ")))
        HRrest= int(input("Your resting heart rate: "))
        VO2max= round(15*(HRmax/HRrest), 2)
        print("\n{} ml/kg/min".format(VO2max))
        return VO2max


def main():
 
    VO2max= Vo2Max.vo2max(33,1,192,15,134)
    
    return VO2max


def setup():

    
    pass


def destroy():
    import sys
    sys.exit()
    
    pass


try:    
    # Start Program
    if __name__ == "__main__":    
        runProgram = main()
except KeyboardInterrupt:
    setup()
    