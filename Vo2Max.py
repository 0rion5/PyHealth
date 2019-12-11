# -*- coding: utf-8 -*-
"""
@author: 0rion
"""

# Create function inside class object
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
    return VO2MAX


# Program Starts here
if __name__ == "__main__":
   VO2MAX =  main()
    
