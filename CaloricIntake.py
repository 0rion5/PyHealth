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

# Figure out Calorie needs

# MEN calories/day = 10 x Weight(kg) + 6.25 x height(cm) - 5 x age(y) + 5
def menBmr(x,y,z):
    BMR= 10*x + 6.25*y - 5*z + 5
    return BMR
men_bmr = lambda x,y,z : 10*x + 6.25*y - 5*z + 5


# WOMEN calories/day = 10 x Weight(kg) + 6.25 x height(cm) - 5 x age(y) + 161
def womenBmr(x,y,z):
    BMR= 10*x + 6.25*y -5*z + 161
    return BMR
women_bmr = lambda x,y,z : 10*x + 6.25*y -5*z + 161


# Make a Function for calculating Body Mass Index
# BMI = (Weight in Kilograms / (Height in Meters x Height in Meters))
def BMI(weight, height): return weight//(height/100)**2
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
    act_lvl_dict= {1 : {'Sedentary'        : 1.2  }, # (limited exercise)
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
            print("\nYou have chosen: "+ str(act_lvl_num))
            act_lvl_num= list(act_lvl_dict[act_lvl_num].items())[0][1]
            break
        else: 
            print("You Chosen Wrong! ")
            continue
    return act_lvl_num


def main():
    gender= lambda x : x[0:1].lower()
    print('\nstep 1: Set Goal')
    goal= get_goal()
    print('\nstep 2: Determine Activity Level')
    act_lvl_num= get_act_lvl()
    print('\nEnter Weight, Height, Age and Gender to calculate Basal Metabolic Rate')
    weight = int(input("Enter weight in kg: "))
    height = int(input("Enter height in cm: "))
    age = int(input("Enter age: "))
    bmi= int(BMI(weight, height))
    while True:
        choice= gender(input("Gender M/F: "))
        if choice == 'm':
            # Make return bmr_men function if male
            calorie_intake= men_bmr(weight, height, age) *act_lvl_num + goal
            break
        elif choice == 'f':
            # Make return bmr_women function if female
            calorie_intake= women_bmr(weight, height, age)*act_lvl_num + goal
            break
        else:
            print("You've chosen wrong\n")
            continue
    
    print("\nCaloric intake: {}".format(int(calorie_intake)))
    
    
    for key in list(bmi_cat_dict):
        if bmi in key:
            print("Your Body Mass Index is: {}\nYour Category is: {}".format(bmi, bmi_cat_dict[key]))
    
    return [int(calorie_intake), BMI]

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


def standard_lose_split(daily_calorie_intake):
    carb   = int(daily_calorie_intake*.25)//4
    protein= int(daily_calorie_intake*.50)//4
    fat    = int(daily_calorie_intake*.25)//9
    print("""

Macro Split
Lean Gain 
25/50/25 split
MACRO             grams
Carbs:            {}g
Protein:          {}g
Fat:              {}g 
    """.format(carb, protein, fat))
    return [carb,protein,fat]


# Start of Program
if __name__ == '__main__':
    calorie_intake= main()
#    maintain= standard_maintain_split(calorie_intake[0])
#    lose= standard_lose_split(calorie_intake[0])