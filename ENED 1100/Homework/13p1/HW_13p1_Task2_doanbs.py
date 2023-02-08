# Activity Homework 13.1: Python Conditional Task 2
# File: HW_13p1_Task2_doanbs.py 
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

name = str(input("Enter the name of the metal (Al, Co, or Cr): "))
structure = str(input("Enter the crystal structure (FCC, BCC, or HCP): "))
avogadoConstant = 6.022E23

#Determine Metal
if(name.lower() == "al"):
    nameFull = "Aluminum"
    mM = 26.98 # g/mol
    rad = 0.1431 * 10**-7 # nm
    densAct = 2.7 # g/cm^3
elif(name.lower() == "co"):
    nameFull = "Cobalt"
    mM = 58.93 # g/mol
    rad = 0.1253 * 10**-7 # cm
    densAct = 8.9 # g/cm^3
elif(name.lower() == "cr"):
    nameFull = "Chromium"
    mM = 52.00 # g/mol
    rad = 0.1249 * 10**-7 # nm
    densAct = 7.2 # g/cm^3

#Determine Structure 
if(structure.upper() == "FCC"):
    length = (4 * rad) / (math.sqrt(2))
    vol = length**3
    atomNum = 4
elif(structure.upper() == "BCC"):
    length = (4 * rad) / (math.sqrt(3))
    vol = length**3
    atomNum = 2
elif(structure.upper() == "HCP"):
    length = 2 * rad
    height = 1.63 * length
    vol = (3 * math.sqrt(3) * height * length**2) / 2
    atomNum = 6

atomMass = mM / avogadoConstant


densCalc = atomMass * atomNum / vol

percDiff = abs(densAct - densCalc) / (densAct) * 100

print("The percent difference is " + "{:.2f}".format(percDiff))

if(percDiff > 5):
    print("Warning: Inputted Crystal Structure May Be Incorrect.")
elif(percDiff <= 5):
    print("The Inputted Crystal Structure is Correct.")