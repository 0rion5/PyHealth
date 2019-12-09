
# -*- coding: utf-8 -*-
"""

@author: 0rion

"""

low= range(1,72)
medium= range(72,83)
high= range(83,91)

intensity_dict= {
        low    : "low"   ,
        medium : "medium",
        high   : "high"
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
    def karvonen(age, restingHR, percent):
        
        """
        This function uses the Karvonen method of determining the optimal target heart rate.
        As compared to HRmax, for which the range is 55% to 90%, when using 
        this method to dtermine intensity, targetHRs during cardiorespiratory 
        training should fall between 50% to 85% of HRR.
        this is to Ensure the target HR is not overestimated
        """
       
        # define heart rate maximum
        HRmax = 220 - age
        
        # return the target heart rate
        return ((HRmax - restingHR)*percent//100) + restingHR 
    
    
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


    def target_high(age, restingHR):
        
        return TargetHeartRate.karvonen(age, restingHR, 90)
    def target_low(age, restingHR):
        return TargetHeartRate.karvonen(age, restingHR, 55)
    
    target_avg = lambda num_1, num_2 : (num_1 + num_2)/2
        
        

# Program Starts Here
if __name__ == "__main__":
    
    restingHR= int(input("Resting heart rate: "))
    age= int(input("Age : "))
    target_high= TargetHeartRate.target_high(age, restingHR)
    target_low= TargetHeartRate.target_low(age, restingHR)
    intensity= int(input("Target intensity 55-90%: "))
    
    for keys in intensity_dict.keys():
        if intensity in keys:
            intensity_rating= intensity_dict[keys][::]
            
    targetBPM= TargetHeartRate.karvonen(age, restingHR, intensity)    
    vo2max= TargetHeartRate.vo2_max(age, restingHR)    
    target_high= TargetHeartRate.target_high(age, restingHR)
    target_low= TargetHeartRate.target_low(age, restingHR)
    target_avg = int(TargetHeartRate.target_avg(target_high,target_low))
    
    print("""Your target heart rate is : {}bpm
Intensity: {}
Target High (90% of HRmax): {}bpm
Target Low  (55% of HRmax): {}bpm 
Target Average            : {}bpm""".format(targetBPM, intensity_rating, target_high, target_low, target_avg))
    