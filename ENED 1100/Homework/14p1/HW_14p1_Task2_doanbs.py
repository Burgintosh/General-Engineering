# Activity Homework 14.1: Python Repetition Task 2
# File: HW_14p1_Task2_doanbs.py 
# Date:    30 November 2022
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
# Dice Game, rolling a 5 changes turns, first to 50 points wins.
# 

import random

def WinCheck(player, score):
    if(score >= 50):
        play = 0
        print('Congrats, ' + player + ', you win with ' + str(score) + ' points!')
        return 1

def PrintWin(P1Score, P2Score, P1Turn):
    player1 = "Player 1"
    player2 = "Player 2"
    if P1Turn == 1:
        if WinCheck(player1, P1Score) == 1:
            print(player1 + " Final Score: " + str(P1Score))
            print(player2 + " Final Score: " + str(P2Score))
            quit()
    elif P1Turn == 0:
        if WinCheck(player2, P2Score) == 1:
            print(player1 + " Final Score: " + str(P1Score))
            print(player2 + " Final Score: " + str(P2Score))
            quit()

def PrintDice(D1, D2):
    print("Dice1 = " + str(D1) + " and Dice2 = " + str(D2))


def CalcScore(oldScore, D1, D2):
    return oldScore + D1 + D2

def PrintScore(player, score):
    print(player + " Score: " + str(score) + "\n")

def ChangeTurn(newPlayer, oldTurn, newTurn):
    oldTurn = 0
    newTurn = 1
    print("\n" + newPlayer + ", it is your turn.\n")
    return oldTurn, newTurn


P1Turn = 1
P1Score = 0

P2Turn = 0
P2Score = 0

start = input("Enter any key to start: ")
play = 1
print("Player 1's turn")
while(play == 1):
    while(P1Turn == 1):
        dice1 = random.randint(0,6)
        dice2 = random.randint(0,6)
        PrintDice(dice1, dice2)
        

        if(dice1 == 5 or dice2 == 5):
            tempTup = ChangeTurn("Player 2", P1Turn, P2Turn)
            P1Turn = tempTup[0]
            P2Turn = tempTup[1]

        else:
            P1Score = CalcScore(P1Score, dice1, dice2)
            PrintScore("Player 1", P1Score)
        PrintWin(P1Score, P2Score, P1Turn)

    while(P2Turn == 1):
        dice1 = random.randint(0,6)
        dice2 = random.randint(0,6)
        PrintDice(dice1, dice2)
        

        if(dice1 == 5 or dice2 == 5):
            tempTup = ChangeTurn("Player 1", P2Turn, P1Turn)
            P2Turn = tempTup[0]
            P1Turn = tempTup[1]
        else:
            P2Score = CalcScore(P2Score, dice1, dice2)
            PrintScore("Player 2", P2Score)
        PrintWin(P1Score, P2Score, P1Turn)