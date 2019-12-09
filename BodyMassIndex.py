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


# Program Start
if __name__ == '__main__':
    bmi= int(BodyMassIndex.metric(int(input("Enter weight in kg: ")),int(input("Height in cm: "))))
    for key in list(bmi_cat_dict):
        if bmi in key:
            print("\nYour Body Mass Index is: {}\nYour category is: {}".format(bmi, bmi_cat_dict[key]))            