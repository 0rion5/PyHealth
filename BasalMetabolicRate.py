# -*- coding: utf-8 -*-
"""
Created on Dec 11 11:11:11 2111

@author: 0rion

Desciption: Harris-Benedict Equation for estimating Basal metabolic Rate

"""


class BasalMetabolicRate:
    
    
    def __init__(self, weight, height, age):
        self.weight = weight
        self.height = height
        self.age    = age
        
    
    def __doc__(self):
        """
        Equation to Calculate Your BMR

        The Harris-Benedict Equation is often used to estimate basal metabolic rate.
        
        Men:  BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) - (5.677 x age in years)
        Women: BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) - (4.330 x age in years)

        """
        
    
    WOMEN= lambda x,y,z: round(447.593 + 9.247*x + 3.098*y - 4.330*z, 2)
    
    
    def women(weight, height, age): 
        return round(447.593 + 9.247*weight + 3.098*height - 4.330*age)


    MEN= lambda x,y,z: round(88.362 + 13.397*x + 4.799*y - 5.677*z, 2)
    
    
    def men(weight, height, age): 
        return round(88.362 + 13.397*weight + 4.799*height - 5.677*age)


def get_bmr():

    option= lambda x: x[0:1].lower()
    while True:
        choice= option(input('Gender M/F:'))
        if choice=='f':
            # Return Female
            bmr = BasalMetabolicRate.women(int(input("Weight(kg) : ")),int(input("Height(cm) : ")),int(input("Age(yrs)   : ")))
            print("""    
Women:
BMR = 447.593 + (9.247 x weight in kg) + (3.098 x height in cm) - (4.330 x age in years)

Harris-Benedict Equation Estimates    
Your Basal Metabolic Rate is: {}/calories per day      
                """.format(bmr))
            return bmr

        elif choice=='m':
            # Return Male
            bmr = BasalMetabolicRate.men(int(input("Weight(kg) : ")),int(input("Height(cm) : ")),int(input("Age(yrs)   : ")))
            print("""    
Men:
BMR = 88.362 + (13.397 x weight in kg) + (4.799 x height in cm) - (5.677 x age in years)

Harris-Benedict Estimation    
Basal Metabolic Rate: {} cals/day      
                """.format(bmr))
            return bmr
        else:
            # Return function
            return get_bmr()
    
# Start of Program
if __name__ == "__main__" :
    bmr= get_bmr()