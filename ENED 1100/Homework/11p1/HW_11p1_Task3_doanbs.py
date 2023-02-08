# Activity HW 11.1: Python Sequential Task 3
# File: HW_11p1_Task3_doanbs.py
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

E_i = int(input("Enter the amplitude of the incident wave: "))
n1 = float(input("Enter the intrinsic impedance of medium 1: "))
n2 = float(input("Enter the intrinsic impeance of medium 2: "))
th_i = int(input("Enter the angle of the incident wave (in Degrees): "))
th_t = int(input("Enter the angle of the transmitted wave (in Degrees): "))

E_t = float(((2 * n2 * math.cos(math.radians(th_i))) / ((n2 * math.cos(math.radians(th_t)) + n1 + math.cos(math.radians(th_i))))) * E_i)
E_r = float(((n2 * math.cos(math.radians(th_i)) - n1 * math.cos(math.radians(th_t))) / (n2 * math.cos(math.radians(th_i)) + n1 * math.cos(math.radians(th_t)))) * E_i)

print("The amplitude of the transmitted wave is E_t = " + "{:.2f}".format(E_t) + "V/m")
print("The amplitude of the reflected wave E_r = " + "{:.2f}".format(E_r) + "V/m")