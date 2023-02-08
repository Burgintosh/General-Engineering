# Activity HW 11.1: Python Sequential Task 2
# File: HW_11p1_Task2_doanbs.py
# Date:    16 November 2022
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
# This program uses a mathmatical equation to create
# out puts based off given inputs. It is developed from
# Converting a LabView Program to Python

import math

# Inputs
Vo = float(input("Enter the Initial Speed (Vo, m/s): ")) # m/s
K = float(input("Enter the Constant (K, (Kgm^2)/s): ")) # (Kgm^2)/s
m = float(input("Enter the Mass of the Mobile (m, Kg): ")) # Kg

# Calculation
V = math.sqrt((Vo * 39.4)**2 - ((K * 15477.02) / (m * 0.07)))

# Output
print("The Value of V = " + "{:.2f}".format(V) + " in/s")