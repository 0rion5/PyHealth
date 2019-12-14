# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:21:22 2019

@author: 0rion

What Are Macronutrients?
In order to successfully count macronutrients, it’s important to know what they 
are and why some people need different macronutrient ratios than others.

###############################################################################
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###############################################################################

Carbohydrates
Carbohydrates include sugars, starches and fibers.

Most types of carbs get broken down into glucose, or blood sugar, which your 
body either uses for immediate energy or stores as glycogen — the storage form 
of glucose — in your liver and muscles.

Carbs provide 4 calories per gram and typically make up the largest portion of 
people’s calorie intake.

Carb intake is among the most hotly debated of all macronutrient 
recommendations, but major health organizations suggest consuming 45–65% of 
your daily calories from carbs.

Carbohydrates are found in foods like grains, starchy vegetables, beans, dairy 
products and fruits.

###############################################################################
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###############################################################################

Fats

Fats have the most calories of all macronutrients, providing 9 calories per 
gram.

Your body needs fat for energy and critical functions, such as hormone 
production, nutrient absorption and body temperature maintenance.

Though typical macronutrient recommendations for fats range from 20–35% of 
total calories, many people find success following a diet higher in fat.

Fats are found in foods like oils, butter, avocado, nuts, meat and fatty fish.

###############################################################################
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
###############################################################################

Proteins
Like carbs, proteins provide 4 calories per gram.

Proteins are vital for processes like cell signaling, immune function and the 
building of tissues, hormones and enzymes.

It’s recommended that proteins comprise 10–35% of your total calorie intake.

However, protein recommendations vary depending on body composition goals, 
age, health and more.

Examples of protein-rich foods include eggs, poultry, fish, tofu and lentils.

"""
from time import sleep as s
import sys

women_bmr = lambda x,y,z : 10*x + 6.25*y -5*z + 161
men_bmr = lambda x,y,z : 10*x + 6.25*y - 5*z + 5
# Figure out Calorie needs
# Mifflin ST Jeor Equation
# MEN calories/day = 10 x Weight(kg) + 6.25 x height(cm) - 5 x age(y) + 5
def menBmr(x,y,z):
    BMR= 10*x + 6.25*y - 5*z + 5
    return BMR


# WOMEN calories/day = 10 x Weight(kg) + 6.25 x height(cm) - 5 x age(y) + 161
def womenBmr(x,y,z):
    BMR= 10*x + 6.25*y -5*z + 161
    return BMR



# Make a Function for calculating Body Mass Index
# BMI = (Weight in Kilograms / (Height in Meters x Height in Meters))
def BMI(weight, height): 
    return weight/(height/100)**2
bmi= lambda x,y: x//(y/100)**2
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


# Set Goal Function
def get_goal():
    
    print("""
1 lose weight
2 maintain weight
3 Gain Weight      
    """)
    
    goal= int(input("Enter Goal Number: "))
    goal_dict= {1 : {'lose weight'     : -500},
                2 : {'maintain weight' : 0   },
                3 : {'gain weight'     : 500 },
        }
    
    try:
        while True:
            if goal in goal_dict.keys():
                goal= int([i[1] for i in goal_dict[goal].items()][0])
                break
            else:
                print('You chosen wrong! ')
                get_goal()
                break
    except Exception:
        print("You Didn't choose a goal between 1-3. ")

    return goal


# Get Activity Level
def get_act_lvl():
    
    
    act_lvl_dict= {1 : {'Sedentary'        : 1.2  }, #(limited exercise)
                   2 : {'Lightly active'   : 1.375}, #(light exercise less than three days per week)
                   3 : {'Moderately active': 1.55 }, #(moderate exercise most days of the week)
                   4 : {'Very active'      : 1.725}, #(hard exercise everyday)
                   5 : {'Extra active'     : 1.9  }  #(strenous exercise two or more times per day)
            }    
    print("Activity list: ")
    print("""
1 limited exercise
2 light exercise less than three days per week
3 moderate exercise most days of the week
4 hard exercise everyday
5 strenous exercise two or more times per day
    """)

    
    while True:
        act_lvl_num= int(input("Select activity level by number: "))
        if act_lvl_num in act_lvl_dict.keys():
            act_lvl_desc= str(list(act_lvl_dict[act_lvl_num].keys())[0])
            print("\nYou have chosen a {} activity level.\n".format(act_lvl_desc ))
            act_lvl_num= list(act_lvl_dict[act_lvl_num].items())[0][1]
            break
        else: 
            print("You Chosen Wrong! ")
            continue
    return act_lvl_num


def standard_maintain_split(daily_calorie_intake):
    carb   = int(daily_calorie_intake*.4)//4
    protein= int(daily_calorie_intake*.4)//4
    fat    = int(daily_calorie_intake*.2)//9
    print("""
Macro Split
Standard Maintenance 
40/40/20 split
MACRO             grams   
Carbs:            {}g
Protein:          {}g
Fat:              {}g
    """.format(carb, protein, fat))
    return [carb,protein,fat]


def yes_no(user_input):   
    option= lambda x: x[0:1].lower()   
    while True:
        choice= option(user_input)        
        if choice=='y':
            # Return yes
            return 'yes'
        elif choice=='n':
            # Return no
            return 'no'
        else:
            # Return yes_no() function
            return yes_no(input("Continue? Y/n: "))
def setup():
    print("BBBBBBBBBBBBBBBBB   MMMMMMMM               MMMMMMMMRRRRRRRRRRRRRRRRR   ")
    s(.1)
    print("B::::::::::::::::B  M:::::::M             M:::::::MR::::::::::::::::R  ")
    s(.1)
    print("B::::::BBBBBB:::::B M::::::::M           M::::::::MR::::::RRRRRR:::::R ")
    s(.1)
    print("BB:::::B     B:::::BM:::::::::M         M:::::::::MRR:::::R     R:::::R")
    s(.1)
    print("  B::::B     B:::::BM::::::::::M       M::::::::::M  R::::R     R:::::R")
    s(.1)
    print("  B::::B     B:::::BM:::::::::::M     M:::::::::::M  R::::R     R:::::R")
    s(.1)
    print("  B::::BBBBBB:::::B M:::::::M::::M   M::::M:::::::M  R::::RRRRRR:::::R ")
    s(.1)
    print("  B:::::::::::::BB  M::::::M M::::M M::::M M::::::M  R:::::::::::::RR  ")
    s(.1)
    print("  B::::BBBBBB:::::B M::::::M  M::::M::::M  M::::::M  R::::RRRRRR:::::R ")
    s(.1)
    print("  B::::B     B:::::BM::::::M   M:::::::M   M::::::M  R::::R     R:::::R")
    s(.1)
    print("  B::::B     B:::::BM::::::M    M:::::M    M::::::M  R::::R     R:::::R")
    s(.1)
    print("  B::::B     B:::::BM::::::M     MMMMM     M::::::M  R::::R     R:::::R")
    s(.1)
    print("BB:::::BBBBBB::::::BM::::::M               M::::::MRR:::::R     R:::::R")
    s(.1)
    print("B:::::::::::::::::B M::::::M               M::::::MR::::::R     R:::::R")
    s(.1)
    print("B::::::::::::::::B  M::::::M               M::::::MR::::::R     R:::::R")
    s(.1)
    print("BBBBBBBBBBBBBBBBB   MMMMMMMM               MMMMMMMMRRRRRRRR     RRRRRRR")
    s(.1)
    print("              .__               .__          __                ")
    s(.1)
    print("  ____ _____  |  |   ____  __ __|  | _____ _/  |_  ___________ ")
    s(.1)
    print('_/ ___\\__  \ |  | _/ ___\|  |  \  | \__  \\   __\/  _ \_  __ \\')
    s(.1)
    print("\  \___ / __ \|  |_\  \___|  |  /  |__/ __ \|  | (  <_> )  | \/")
    s(.1)
    print(" \___  >____  /____/\___  >____/|____(____  /__|  \____/|__|   ")
    s(.1)
    print("     \/     \/          \/                \/                   ")
    s(.1)
    print(' ' )
    s(.1)


def main():
    gender= lambda x : x[0:1].lower()
    weight = float(input("Enter weight in kg: "))
    height = int(input("Enter height in cm: "))
    age = int(input("Enter age: "))
    while True:
        choice= gender(input("Gender M/F: "))
        if choice == 'm':
            # Make return bmr_men function if male
            bmr= men_bmr(weight, height, age)
            
            break
        elif choice == 'f':
            # Make return bmr_women function if female
            bmr= women_bmr(weight, height, age)
            break
        else:
            print("You've chosen wrong\n")
            continue
    
    print("\nBasal Metabolic Rate   : {}".format(int(bmr)))
    
    if yes_no(input("Continue to set goals? Y/n:")) == "yes":
        pass
    else: return bmr
    
    goal= get_goal()
    act_lvl_num= get_act_lvl()
    target_calorie_intake= round(bmr *act_lvl_num + goal)
    print("Goal and Activity based caloric intake is {}".format(target_calorie_intake))
    return int(bmr)


def destroy(): return sys.exit()


# Start of Program
if __name__ == '__main__':    
    setup()
    bmr= main()