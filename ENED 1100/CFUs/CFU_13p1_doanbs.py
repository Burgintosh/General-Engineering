# Activity CFU 13.1 Python Conditional
# File: CFU_13p1_doanbs.py
# Date:    31 October 2022
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
# THis program takes an input of an orthographic view
# and outputs the dimensions used to show that view.

run = 1
while run == 1:
    view = str(input("Enter an Orthographic View (Front, Top, or Right): "))
    if(view.lower() == "front"):
        print("Height and Width")
        run = 0
    elif(view.lower() == "top"):
        print("Width and Depth")
        run = 0
    elif(view.lower() == "right"):
        print("Depth and Height")
        run = 0
    else:
        print("The view is invalid, please try again.")