# Activity Homework 13.1: Python Conditional Task 1
# File: HW_13p1_Task1_doanbs.py 
# Date:    23 November 2022
# By:      Burgess Doan III
# Section: 005
# Team:    Team 072
# 
# ELECTRONIC SIGNATURE
# Burgess Doan III
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# A BRIEF DESCRIPTION OF WHAT THE SCRIPT OR FUNCTION DOES
# This script is a header template that will be used for 
# all your python files the rest of the semester.

import math

pres = float(input("Enter the Pressure, P (in atm): "))
tempC = float(input("Enter the Temperature, T (in Celsius): "))

# Conversions
tempK = float(tempC + 273.15) # Celsius to Kelvin

#Calculations
pres1 = 0.006 * (math.exp((6293*((1/273.15)-(1/float(tempK))))-(0.56*math.log(float(tempK)/273.15))))
pres2 = 0.006 * (math.exp((6808*((1/273.15)-(1/float(tempK))))-(5.09*math.log(float(tempK)/273.15))))
print(pres1)
print(pres2)

if(tempK > 647 and pres > 218):
    print("Super Critical Liquid")
elif(tempK < 273.15):
    if(pres > pres1):
        print("Solid")
    else:
        print("Gas")
elif(pres > pres2):
    print("Liquid")
else:
    print("Gas")