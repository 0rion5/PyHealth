# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:12:04 2019

@author: 0rion
"""


class OneRepMax:
    
    def __init__(self):
        self.data= []
        
    __doc__ = """
        This class calculates one rep max for upper body and lower boddy using the users
        4-6 rep max in kg.
        """
    
    upper= lambda x: x*1.1307  + 0.6998
    lower= lambda x: x*1.09703 + 14.2546
    upper_lbs= lambda x: (x*1.1307  + 0.6998)*2.20462
    lower_lbs= lambda x: (x*1.09703 + 14.2546)*2.20462
    def upper_lbs(lbs): return (lbs*1.1307  + 0.6998)*2.20462
    def lower_lbs(lbs): return (lbs*1.09703 + 14.2546)*2.20462



if __name__ ==  '__main__' :

    rm_upper= round(OneRepMax.upper(int(input("Upper Body 4-6 Rep Max in kg: "))))
    rm_lower= round(OneRepMax.lower(int(input("Lower Body 4-6 Rep Max in kg: "))))
    print("""Recommended upper 1RM: {}\n\nRecommended lower 1RM: {}\n""".format(rm_upper,rm_lower))