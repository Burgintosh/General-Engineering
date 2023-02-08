# Activity Homework 14.1: Python Repetition Task 1
# File: HW_14p1_Task2_doanbs.py 
# Date:    29 November 2022
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
# Guesses user inputed code and output the correct number of digit guesses after 1000 attempts
# 

import random

D1 = int(input("Enter the first integer digit of your code:"))
D2 = int(input("Enter the second integer digit of your code:"))
D3 = int(input("Enter the third integer digit of your code:"))
D4 = int(input("Enter the fourth integer digit of your code:"))

guess = 0
count0 = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0

while(guess < 1000):

    G1 = random.randint(0,9)
    G2 = random.randint(0,9)
    G3 = random.randint(0,9)
    G4 = random.randint(0,9)

    C1 = bool(G1 == D1)
    C2 = bool(G2 == D2)
    C3 = bool(G3 == D3)
    C4 = bool(G4 == D4)
    Ct = int(C1) + int(C2) + int(C3) + int(C4)

    if(Ct == 0):
        count0 +=1
    elif(Ct == 1):
        count1 +=1
    elif(Ct == 2):
        count2 +=1
    elif(Ct == 3):
        count3 +=1
    elif(Ct == 4):
        count4 +=1
    #else:          For Debug Purposes
    #    print(Ct)
    guess += 1

    countarr = [count0, count1, count2, count3, count4]
for idx, i in enumerate(countarr):
    print("Number of Attempts with " + str(idx) + " Correct Guesses = " + str(i))