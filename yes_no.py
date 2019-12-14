# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 23:31:35 2019

@author: 0rion
"""

def yes_no(user_input):   
    option= lambda x: x[0:1].lower()   
    while True:
        choice= option(user_input)        
        if choice=='y':
            # Return yes
            return True
        elif choice=='n':
            # Return no
            return False
        else:
            # Return function
            return yes_no()
        
# Start Program
if __name__ == "__main__":
    yes_no()    