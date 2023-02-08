# Activity HW 11.1: Python Sequential Task 1
# File: HW_11p1_Task1_doanbs.py
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
# Converting a flow chart diagram to Python

import math

# Inputs
c = float(3e+9) # Speed of Light, m/s
v = float(1.2e+9) # Speed of the Movile, m/s
m = int(150000) # Mass of the Mobile, kg

# Equations
gam = float(1/(math.sqrt(1-(v/c)**2)))
p = float(m*v)
q = float(m*v*gam)

# Outputs
print("Gam = " + "{:.2e}".format(gam))
print("p = " + "{:.2e}".format(p) + " kg*m/s")
print("q = " + "{:.2e}".format(q) + " kg*m/s")

