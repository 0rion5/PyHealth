# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:58:43 2019

@author: 0rion
"""
#%%
class PyHealth:
    
    """This class initializes 5 methods used for calculating health and fitness metrics"""
    
    def __init__(self):
        self.data= []
    
    def basal_metabolic_rate():
        import BasalMetabolicRate
        BasalMetabolicRate.setup()
        BasalMetabolicRate.main()
        main_menu= setup()
        return main_menu
    
    
    def body_mass_index():
        import BodyMassIndex
        BMI= BodyMassIndex.main()
        return round(BMI, 2)
        
    
    def one_rep_max():
        import OneRepMax
        upper_rm= OneRepMax.OneRepMax.upper(int(input("Upper Body 4-6 Rep Max in kg: ")))
        lower_rm= OneRepMax.OneRepMax.lower(int(input("Lower Body 4-6 Rep Max in kg: ")))
        print("\nYour recommended upper is: {}\nYour recommended lower is: {}\n".format(round(upper_rm),round(lower_rm)))
        return [upper_rm, lower_rm]

    
    def target_heart_rate():
        import TargetHeartRate
        return TargetHeartRate.main()
    
    
    def vo2max():
        """Gets vo2 max class from module and returns estimated vo2max """
        import Vo2Max
        age= int(input("Enter Age: "))
        gender = input("Gender m/f: ")
        if gender[0::].lower() == 'm':
            gender= 1
        elif gender[0::].lower() == 'f':
            gender = 0
        weight = float(input("weight in lbs: "))
        walk_time_mins = int(input("Enter walk time in mins: "))
        heart_rate = int(input("Heart rate: "))
        VO2max= Vo2Max.Vo2Max.vo2max(age, gender,weight,walk_time_mins, heart_rate)
        return  VO2max
#%%
#%%
def menu(): 
   while True:       
       PyHealth_dict= {
                1 : "Basal Metabolic Rate" ,
                2 : "Body Mass Index"      ,
                3 : "One Rep Max"          ,
                4 : "Target Heart Rate"    ,
                5 : "Vo2 Max"             
                }
       print("\nPyHealth Menu Options:               ") 
       print("(1) Basal Metabolic Rate\n(2) Body Mass Index\n(3) One Rep Max\n(4) Target Heart Rate\n(5) VO2 Max")
       option= int(input("Choose an option 1 to 5: "))
       for key in list(PyHealth_dict):
           if key == option:
                result= PyHealth_dict[key]
                return result
                print(result)
       else:
           return menu()
#%%
#%%
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
#%%
#%%
def main():
    return setup()
#%%
#%%
def setup():
    menu_option= menu()
    print("\nYou've chosen "+str(menu_option))
    if yes_no(input("Would you like to continue? y/n: "))=="yes":
        
        runProgram = True
        while runProgram:
                try:
                    if menu_option == "Basal Metabolic Rate":
                        return PyHealth.basal_metabolic_rate()
                
                    elif menu_option == "Body Mass Index":
                        bmi= PyHealth.body_mass_index()
                        return bmi
                        
                    elif menu_option == "One Rep Max":
                        return PyHealth.one_rep_max()
                        
                    elif menu_option == "Target Heart Rate":
                        return PyHealth.target_heart_rate()
                        
                    elif menu_option == "Vo2 Max":
                        return PyHealth.vo2max()
                                   
                            
                except KeyboardInterrupt:
                    PyHealth.setup()
    else:setup()
#%%
#%%
def destroy():
    import sys
    sys.exit()
#%%
#%%
def initialize():
    import time
    time.sleep(0.1)
    print("          _                                       _                   ")
    time.sleep(0.1)
    print("    _  _ | |                                     | | _  _             ")
    time.sleep(0.1)
    print("   | || || |                                     | || || |            ")
    time.sleep(0.1)
    print(" =H| || || |========nnnn=============nnnn========| || || |H=          ")
    time.sleep(0.1)
    print("   |_||_|| |        |  |             |  |        | ||_||_|            ")
    time.sleep(0.1)
    print("         |_|        /  |             |  \        |_|                  ")
    time.sleep(0.1)
    print("                   |   |             |   |                            ")
    time.sleep(0.1)
    print("                   \   (_   /~~~\   _)   /                            ")
    time.sleep(0.1)
    print("                    \    \ ( '_' ) /    /                             ")
    time.sleep(0.1)
    print("                     \    )\  =  /(    /                              ")
    time.sleep(0.1)
    print("                      \   (_)   (_)   /                               ")
    time.sleep(0.1)
    print("                       \ /   ~~~   \ /                                ")
    time.sleep(0.1)
    print("                       (             )                                ")
    time.sleep(0.1)
    print("                        \           /                                 ")
    time.sleep(0.1)
    print("                         \         /                                  ")
    time.sleep(0.1)
    print("                          )==(O)==(                                   ")
    time.sleep(0.1)
    print("                         /         \                                 /")
    time.sleep(0.1)
    print("                        /____/ \____\                                /")
    time.sleep(0.1)
    print("                        /   /   \   \                                /")
    time.sleep(0.1)
    print("                       /   /     \   \                               /")
    time.sleep(0.1)
    print("                      (   )       (   )                               ")
    time.sleep(0.1)
    print("                      |   |       |   |                               ")
    time.sleep(0.1)
    print("                      |   |       |   |                               ")
    time.sleep(0.1)
    print("                      |___|       |___|                               ")
    time.sleep(0.1)
    print("                      (___)       (___)                               ")
    time.sleep(0.1)
    print("======================================================================")       
    time.sleep(0.1)
    print("         _____       _    _            _ _   _     ")
    time.sleep(0.1)
    print("        |  __ \     | |  | |          | | | | |    ")
    time.sleep(0.1)
    print("        | |__) |   _| |__| | ___  __ _| | |_| |__  ")
    time.sleep(0.1)
    print("        |  ___/ | | |  __  |/ _ \/ _` | | __| '_ \ ")
    time.sleep(0.1)
    print("        | |   | |_| | |  | |  __/ (_| | | |_| | | |")
    time.sleep(0.1)
    print("        |_|    \__, |_|  |_|\___|\__,_|_|\__|_| |_|")
    time.sleep(0.1)
    print("                __/ |                              ")
    time.sleep(0.1)
    print("                |___/                               ")
    time.sleep(0.1)
    print("The programs included are free software;")
    time.sleep(0.3)
    print("the exact license terms for each program are described in the")
    time.sleep(0.3)
    print("individual files in /PyHealth/license.\n")
    time.sleep(0.3)
    print("Calculate your target heart rate with python.\n")
    time.sleep(0.3)
    print("This program uses the different methods of determining the health related calculatoins.\n")
    time.sleep(0.3)
    print("Acheive Goals Faster and increase performace with data you can use.")
    time.sleep(0.3)
#%%
# Program Starts Here
try:
    if __name__ == "__main__":
        initialize()
        main()
except KeyboardInterrupt:
    
    
    destroy()