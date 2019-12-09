
# -*- coding: utf-8 -*-
"""

@author: 0rion

"""

def target_heart_rate_program_init():
    import time
    print("________¶¶                                                            ") 
    time.sleep(0.1)
    print("____¶___¶¶¶                                                           ") 
    time.sleep(0.1)
    print("____¶¶¶_¶_¶¶¶                                                         ")
    time.sleep(0.1)
    print("_____¶¶¶¶¶__¶¶                                                        ") 
    time.sleep(0.1)
    print("¶¶¶____¶¶¶¶__¶¶                                                       ") 
    time.sleep(0.1)
    print("_¶¶¶¶¶¶¶¶¶¶¶__¶¶                                                      ")
    time.sleep(0.1)
    print("__¶¶¶_¶¶¶¶¶¶¶__¶¶                                                     ")
    time.sleep(0.1)
    print("____¶¶_¶¶¶¶¶¶¶_¶¶                                                     ")
    time.sleep(0.1)
    print("_____¶¶_¶¶¶¶¶¶¶¶¶___________¶¶¶¶¶                                     ")
    time.sleep(0.1)
    print("_______¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶_¶¶¶¶                                   ")
    time.sleep(0.1)
    print("________¶¶¶¶¶¶¶¶¶_______¶¶¶_______¶¶                                  ")
    time.sleep(0.1)
    print("_____________¶¶¶¶¶_____¶¶¶___¶¶____¶¶                                 ")
    time.sleep(0.1)
    print("_______________¶¶¶¶___¶¶¶__¶¶¶¶¶____¶¶                                ")
    time.sleep(0.1)
    print("_________________¶¶¶_¶¶¶__¶¶___¶¶___¶¶¶                               ")
    time.sleep(0.1)
    print("__________________¶¶¶¶___¶¶_____¶____¶¶                               ")
    time.sleep(0.1)
    print("___________________¶¶¶¶_¶¶______¶¶___¶¶                               ")
    time.sleep(0.1)
    print("___________________¶¶¶¶¶¶___¶¶__¶¶___¶¶                               ")
    time.sleep(0.1)
    print("___________________¶_¶¶¶¶__¶¶¶__¶¶___¶¶                               ")
    time.sleep(0.1)
    print("__________________¶¶__¶¶¶¶¶__¶__¶¶___¶¶                               ")
    time.sleep(0.1)
    print("__________________¶¶__¶_¶¶¶¶_¶__¶¶__¶¶¶                               ")
    time.sleep(0.1)
    print("__________________¶__¶¶_¶¶¶¶¶¶__¶¶__¶¶¶                               ")
    time.sleep(0.1)
    print("_________________¶¶__¶¶_¶¶__¶¶__¶¶__¶¶¶                               ")
    time.sleep(0.1)
    print("_________________¶¶__¶¶_¶¶__¶¶__¶¶__¶¶¶                               ")
    time.sleep(0.1)
    print("_________________¶¶__¶¶_¶¶_¶¶__¶¶___¶¶¶                               ")
    time.sleep(0.1)
    print("_________________¶¶__¶¶__¶_¶___¶¶__¶¶¶                                ")
    time.sleep(0.1)
    print("_________________¶¶__¶¶__¶¶___¶¶___¶¶¶                                ")
    time.sleep(0.1)
    print("_________________¶¶__¶_______¶¶___¶¶¶                                 ")
    time.sleep(0.1)
    print("_________________¶¶__¶¶_____¶¶____¶¶¶                                 ")
    time.sleep(0.1)
    print("__________________¶__¶¶____¶¶____¶¶¶                                  ")
    time.sleep(0.1)
    print("__________________¶¶__¶¶¶¶¶____¶¶¶¶                                   ")
    time.sleep(0.1)
    print("__________________¶¶_________¶¶¶¶¶                                    ")
    time.sleep(0.1)
    print("___________________¶¶______¶¶¶¶¶                                      ")
    time.sleep(0.1)
    print("____________________¶¶¶¶¶¶¶¶¶¶                                        ")
    time.sleep(0.1)
    print("______________________¶¶¶¶¶¶                                          ")
    time.sleep(0.1)
    print("""    
___________                           __      ___ ___                        __   

 _______                   _     _    _                 _   
|__   __|                 | |   | |  | |               | |  
   | | __ _ _ __ __ _  ___| |_  | |__| | ___  __ _ _ __| |_ 
   | |/ _` | '__/ _` |/ _ \ __| |  __  |/ _ \/ _` | '__| __|
   | | (_| | | | (_| |  __/ |_  | |  | |  __/ (_| | |  | |_ 
 __|_|\__,_|_|  \__, |\___|\__| |_|  |_|\___|\__,_|_|   \__|
|  __ \     | |  __/ |                                      
| |__) |__ _| |_|___/                                       
|  _  // _` | __/ _ \                                       
| | \ \ (_| | ||  __/                                       
|_|  \_\__,_|\__\___|                                                            

The programs included are free software;
the exact license terms for each program are described in the
individual files in /PyHealth/license.

Calculate your target heart rate with python.

This program uses the Karvonen method of determining the optimal target heart rate.
As compared to HRmax method, for which the range is 55% to 90%, when using 
this method to determine intensity, targetHRs during cardiorespiratory 
training should fall between 50% to 85% of HRR.
this is to Ensure the target HR is not overestimated
 
Acheive Goals Faster and increase performace with data you can use.

            """ )                                                 

    time.sleep(0.2)
low    = range(1,  62)
medium = range(62, 75)
high   = range(75, 101)

intensity_dict= {
        low    : "low intensity"   ,
        medium : "medium intensity",
        high   : "high intensity"
        }

class TargetHeartRate:
    
    """
    This Class Calculates the target heart rate using two different methods
    """
   
    # Class methods to call from other programs when importing
    hr_max= lambda age,percent: (220-age)*percent//100
    karvonen_hr= lambda age, restingHR, percentage: (((220-age) - restingHR)*percentage//100) + restingHR
    
    
    # HRmax Method
    def hrmax(age, percent):
        
        """
        Using HRmax to determine Exercise intensity provides an estimation
        of how hard the end user should exercise. In general, research shows 
        that an appropriate range of recommended exercise intensity falls 
        between 55% and 90% of HRmax 
        """
        
        # define heart rate maximum
        HRmax= 220-age
        # return the target heart rate
        return HRmax*percent//100
            
    
    # Karvonen method
    def karvonen(age, HRresting, percent):
        
        """
        This function uses the Karvonen method of determining the optimal target heart rate.
        As compared to HRmax, for which the range is 55% to 90%, when using 
        this method to determine intensity, targetHRs during cardiorespiratory 
        training should fall between 50% to 85% of HRR.
        this is to Ensure the target HR is not overestimated
        """
       
        # define heart rate maximum
        HRmax =  207-(0.7*age)
        global HRreserve
        HRreserve = HRmax - HRresting
        

        # return the target heart rate
        return round(((HRmax - HRresting)*percent//100) + HRresting)
    
    def heart_rate_reserve(age, HRresting):
        HRmax = 220-age
        return HRmax - HRresting
    
    
    # Get VO2 Max
    def vo2_max(age,resting_hr ):
        
        """
        Vo2 Max = 15.3 x (MHR/RHR)

        MHR = Maximum heart rate. This number is actually the number of beats 
        over the number of minutes, or the number of beats in 20 seconds multiplied by 3. 

        RHR = Resting heart rate. The number is also found by dividing beats 
        by minute or number of beats in 20 seconds multiplied by three. 
        """
        # Return VO2 Max
        return round(15.3*((220-age)/resting_hr),2)


    def target_high(age, HRresting):
        return TargetHeartRate.karvonen(age, HRresting, 85)

    def target_low(age, HRresting):
        return TargetHeartRate.karvonen(age, HRresting, 50)

    def target_min(HRreserve,RHR):
        return HRreserve*0.5 +RHR
    
    target_avg = lambda x, y : (x+y)/2
        
    def zoladz(age):
        """
        An alternative to the Karvonen method is the Zoladz method, 
        which derives exercise zones by subtracting values from HRmax:
        
        THR = HRmax − Adjuster ± 5 bpm
            Zone 1 Adjuster = 50 bpm
            Zone 2 Adjuster = 40 bpm
            Zone 3 Adjuster = 30 bpm
            Zone 4 Adjuster = 20 bpm
            Zone 5 Adjuster = 10 bpm
        """
        adjuster= {
                1 : 50, # Easy
                2 : 40, # Easy but less
                3 : 30, # Medium
                4 : 20, # Medium but less
                5 : 10  # Hard
                   }
        # Heart Rate Max
        HRmax = 220 -int(age)
        # Get user input to select a zone
        selected_zone= int(input("Select Training Zone: "))
        # Use List comprehension to check if selected zone is in the adjuster dict
        for key in adjuster: 
            if key == selected_zone:
                THR= HRmax - int(adjuster[key])
        return THR
               
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
            # Return function
            return yes_no()
        
# Program Starts Here
if __name__ == "__main__":
    target_heart_rate_program_init()
    if yes_no(input("Continue to target heart rate? y/n: "))=="yes":
        restingHR= int(input("What is your resting heart rate? "))
        age= int(input("How old are you? "))
        target_high= TargetHeartRate.target_high(age, restingHR)
        target_low= TargetHeartRate.target_low(age, restingHR)
        intensity= int(input("What is your target intensity 50-85%? "))
        
        for keys in intensity_dict.keys():
            if intensity in keys:
                intensity_rating= intensity_dict[keys][::]
                
        targetBPM= TargetHeartRate.karvonen(age, restingHR, intensity)    
        vo2max= TargetHeartRate.vo2_max(age, restingHR)    
        target_high= TargetHeartRate.target_high(age, restingHR)
        target_low= TargetHeartRate.target_low(age, restingHR)
        
        print("""\nYour target heart rate is : {} bpm
Intensity Level           : {}
Target High (85% of HRR): {} bpm
Target Low  (50% of HRR): {} bpm
Vo2Max                    : {} ml/kg/min""".format(targetBPM, intensity_rating, target_high, target_low,vo2max))
