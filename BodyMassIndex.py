# -*- coding: utf-8 -*-
"""
@author: 0rion
"""


# BMI METRIC
# BMI = (Weight in Kilograms / (Height in Centimeters x Height in Centimeters)/100)
bmi_metric= lambda x,y: x/(y/100)**2


# BMI IMPERIAL
# BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
bmi_imperial= lambda x,y: (x/y**2)*703


# Make a body mass index object
class BodyMassIndex:

    # Initialize to be stored to multiple instances
    def __init__(self,weight, height ):
        self.weight= weight
        self.height= height

    # Make a Doc String
    def __doc__ ():
        """
        This Class Calculates Body Mass Index in metric[weight(kg),height(cm)] 
        and in imperial[weight(lbs) height(ft)].
        """
    # BMI = (Weight in Kilograms / (Height in Centimeters x Height in Centimeters)/100)        
    metric   = lambda weight, height : weight/(height/100)**2
    # BMI = (Weight in Pounds / (Height in inches x Height in inches)) x 703
    imperial = lambda weight, height : weight/height**2*703


def main():
    
    weight= float(input("Enter weight in kg: "))
    height= int(input("Height in cm: "))
    bmi= BodyMassIndex.metric(weight,height)
    
    # Define the ranges for bmi category index
    Severe_thinness= range(0, 16)
    Moderate_thinness= range(16, 17)
    Mild_thinness= range(17, 18)
    Normal= range(18, 25)
    Overweight= range(25, 30)
    Obese_class_one= range(30, 35)
    Obese_class_two= range(35, 40)
    Obese_class_thr= range(40, 99)
    
    # Define a dictionary of the range of categories for body mass index rating
    bmi_cat_dict= {Severe_thinness   : 'Severe Thinness' , 
                   Moderate_thinness : 'Moderate Thinness',
                   Mild_thinness     : 'Mild Thinness',
                   Normal            : 'Normal',
                   Overweight        : 'Overweight',
                   Obese_class_one   : 'Obese Class I',
                   Obese_class_two   : 'Obese Class II', 
                   Obese_class_thr   : 'Obese Class III', 
              }

    for key in list(bmi_cat_dict):
        if int(bmi) in key:
            print("\nBody Mass Index {} is {}".format(round(bmi,2), bmi_cat_dict[key]))
            
    return bmi


def setup():

                                                             
    from time import sleep as s                                                             
    print("BBBBBBBBBBBBBBBBB   MMMMMMMM               MMMMMMMMIIIIIIIIII")
    s(0.1)
    print("B::::::::::::::::B  M:::::::M             M:::::::MI::::::::I")
    s(0.1)
    print("B::::::BBBBBB:::::B M::::::::M           M::::::::MI::::::::I")
    s(0.1)
    print("BB:::::B     B:::::BM:::::::::M         M:::::::::MII::::::II")
    s(0.1)
    print("  B::::B     B:::::BM::::::::::M       M::::::::::M  I::::I  ")
    s(0.1)
    print("  B::::B     B:::::BM:::::::::::M     M:::::::::::M  I::::I  ")
    s(0.1)
    print("  B::::BBBBBB:::::B M:::::::M::::M   M::::M:::::::M  I::::I  ")
    s(0.1)
    print("  B:::::::::::::BB  M::::::M M::::M M::::M M::::::M  I::::I  ")
    s(0.1)
    print("  B::::BBBBBB:::::B M::::::M  M::::M::::M  M::::::M  I::::I  ")
    s(0.1)
    print("  B::::B     B:::::BM::::::M   M:::::::M   M::::::M  I::::I  ")
    s(0.1)
    print("  B::::B     B:::::BM::::::M    M:::::M    M::::::M  I::::I  ")
    s(0.1)
    print("  B::::B     B:::::BM::::::M     MMMMM     M::::::M  I::::I  ")
    s(0.1)
    print("BB:::::BBBBBB::::::BM::::::M               M::::::MII::::::II")
    s(0.1)
    print("B:::::::::::::::::B M::::::M               M::::::MI::::::::I")
    s(0.1)
    print("B::::::::::::::::B  M::::::M               M::::::MI::::::::I")
    s(0.1)
    print("BBBBBBBBBBBBBBBBB   MMMMMMMM               MMMMMMMMIIIIIIIIII")
    s(0.1)
    
    s(0.1)
    print("              .__               .__          __                ")
    s(0.1)
    print("  ____ _____  |  |   ____  __ __|  | _____ _/  |_  ___________ ")
    s(0.1)
    print('_/ ___\\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ \\')
    s(0.1)
    print("\  \___ / __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/")
    s(0.1)
    print(" \___  >____  /____/\___  >____/|____(____  /__|  \____/|__|   ")
    s(0.1)
    print("     \/     \/          \/                \/                   ")
    s(0.1)
    print(' ' )
    s(0.1)
            

# Program Starts here
if __name__ == '__main__':
    setup()
    bmi = main()       