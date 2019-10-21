# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:10:29 2019

@author: chamiotk
"""

import random

def shuffle():
    play = True
    J1_turn = True
    J1_score = 0
    J1_score_turn = 0
    bot_score = 0
    bot_score_turn = 0
    while(play):
        if J1_turn:
            launch = random.randrange(1,7)
            print("J1 - dice : ", launch)
            if launch == 1:
                # Dice at 1, turn score is removed + bot turn
                J1_score_turn = 0
                J1_turn = False
                print("J1 - Dice = 1, turn to bot")
            else: 
                J1_score_turn += launch
                if J1_score_turn + J1_score >= 100:
                    # Turn score + global >= 100 => End of game
                    print("J1 - WINNER")
                    play = False
                    break
                print("J1 in progress : ", J1_score_turn)
                print("J1 - global if exit", J1_score_turn + J1_score)
                ask_for_continue = input("Continue ? y or n")
                if ask_for_continue == 'n':
                    J1_score += J1_score_turn # Add turn score to global score when user decides to quit his turn
                    J1_score_turn = 0
                    print("J1 - Global Score : ", J1_score)
                    J1_turn = False # -> Turn to bot
                elif ask_for_continue == 'q':
                    play = False
        else:
            launch = random.randrange(1,7)
            if launch == 1:
                bot_score_turn = 0
                J1_turn = True
                print("BOT - Dice = 1, turn to J1, score : ", bot_score)
            else: 
                bot_score_turn += launch
                if bot_score_turn + bot_score >= 100:
                    print("BOT - WINNER")
                    play = False
                    break
                bot_decision = random.randrange(1,3) # Bot has 1 chance on 3 to decide to quit his turn
                if bot_decision == 1:
                    bot_score += bot_score_turn
                    bot_score_turn = 0
                    print("BOT - Global Score : ", bot_score)
                    J1_turn = True
            

shuffle()