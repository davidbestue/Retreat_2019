# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:02:54 2019

@author: David Bestue
"""

##### Tasks 2 players Rock _ paper _ sicssors
from random import choice
import numpy
from numpy import array, unique
import numpy as np
from itertools import chain
import psychopy.visual
import psychopy.event
from psychopy import visual, core, event
import pandas as pd
import os
import glob
import easygui
from easygui import multenterbox
from function_randomness import randomness_sequence

# https://www.iconfinder.com/icons/2088376/game_gesture_hand_right_rock_win_icon

#Dialogue box for subject name
screen_dim =[1280, 720]
rounds=50

black=[-1,-1,-1]

root_imgs = os.getcwd() + '\\images\\' 
root_save = os.getcwd() + '\\results\\' 


msg = 'Names '
title = "Subjects information"
fieldNames = ["Player_left", "beers P_left", "Player_right", "beers P_right", "repetition"]
fieldValues = multenterbox(msg,title, fieldNames)
player1 = fieldValues[0]
b_pl1 = fieldValues[1]

player2 = fieldValues[2]
b_pl2 = fieldValues[3]

b_n = fieldValues[4]



win = psychopy.visual.Window(size=screen_dim, units="pix", pos=(0, 0), fullscr=True, allowGUI=True)

responses=[]



for trial in range(0, rounds):
    
    #Trial number
    trial_number=visual.TextStim(win=win, text= str(trial) + '/' +str(rounds) , pos=[screen_dim[0]/3, screen_dim[1]/2.3], wrapWidth=screen_dim[0]/2, color=[1,1,1], units='pix', height=screen_dim[1]/25) 
    #Names players
    pl1=visual.TextStim(win=win, text=player1, pos=[ -0.25* screen_dim[0],  0.35* screen_dim[1]], wrapWidth=screen_dim[0]/2, color=[1,1,1], units='pix', height=screen_dim[1]/15) 
    pl2=visual.TextStim(win=win, text=player2, pos=[ +0.25* screen_dim[0],  0.35* screen_dim[1]], wrapWidth=screen_dim[0]/2, color=[1,1,1], units='pix', height=screen_dim[1]/15) 
    
    #play instruction
    play_txt=visual.TextStim(win=win, text='Play!', pos=[0, -0.1* screen_dim[1]], wrapWidth=screen_dim[0]/2, color=black, units='pix', height=screen_dim[1]/10) 
    
    ## Start
    trial_number.draw()
    pl1.draw()
    pl2.draw()
    play_txt.draw()
    
    win.flip()
    decisions = []
    list_options = ["left", "right", "down", "a", "s", "d"]
    
    while len(decisions)<2:
        keys_pressed= psychopy.event.waitKeys(keyList=list_options)
        #print(keys_pressed)
        decisions.append(keys_pressed[0])
        if keys_pressed[0] in ["left", "right", "down"]:
            list_options = ["a", "s", "d"]
        else:
            list_options = ["left", "right", "down"]
    
    
    ##
    #print(decisions)
    #print('Done!')
    if decisions[0] in ['a', 's', 'd']:
        pl1_resp = decisions[0]
        pl2_resp = decisions[1]
    else:
        pl1_resp = decisions[1]
        pl2_resp = decisions[0] 
    
    ## convert to rock, paper, scissor
    if pl1_resp =='a':
        pl1_resp = 'rock'
    elif pl1_resp =='s':
        pl1_resp = 'paper'
    elif pl1_resp =='d':
        pl1_resp = 'scissor'
    
    #
    if pl2_resp =='left':
        pl2_resp = 'rock'
    elif pl2_resp =='down':
        pl2_resp = 'paper'
    elif pl2_resp =='right':
        pl2_resp = 'scissor'
    
    print(decisions)
    print(pl1_resp, pl2_resp)
    #imgs
    resp_img1= root_imgs +  pl1_resp + '.png'
    p1_img = psychopy.visual.ImageStim(win=win, image=resp_img1 , units='pix',size=(screen_dim[1]/2.5,screen_dim[1]/2.5), ori=0, pos=[ -0.25* screen_dim[0],  -0.05* screen_dim[1]]) 
    p1_img.draw()  
    resp_img2 = root_imgs +  pl2_resp + '.png'
    p2_img = psychopy.visual.ImageStim(win=win, image=resp_img2 , units='pix',size=(screen_dim[1]/2.5,screen_dim[1]/2.5), ori=0, pos=[ 0.25* screen_dim[0],  -0.05* screen_dim[1]]) 
    p2_img.draw()  
    trial_number.draw()
    pl1.draw()
    pl2.draw() 
    
    if pl1_resp == pl2_resp:
        winner='draw'
    elif pl1_resp == 'rock':
        if pl2_resp == 'paper':
            winner = player2
        elif pl2_resp == 'scissor':
            winner = player1
    elif pl1_resp == 'paper':
        if pl2_resp == 'rock':
            winner = player1
        elif pl2_resp == 'scissor':
            winner = player2
    elif pl1_resp == 'scissor':
        if pl2_resp == 'rock':
            winner = player2
        elif pl2_resp == 'paper':
            winner = player1
    
    
    print(winner)
    winner_txt=visual.TextStim(win=win, text= winner, pos=[0, -0.1* screen_dim[1]], wrapWidth=screen_dim[0]/2, color=black, units='pix', height=screen_dim[1]/10) 
    winner_txt.draw()
    win.flip()
    core.wait(1)
    responses.append([player1, player2, pl1_resp, pl2_resp, winner])


## Calculate_winner
df = pd.DataFrame(responses)
df.columns = ['player1', 'player2', 'resp1', 'resp2', 'result'] 
wins_p1 = df.loc[df.result == player1, 'result'].count()
wins_p2 = df.loc[df.result == player2, 'result'].count()

if wins_p1>wins_p2:
    Final_result_text =visual.TextStim(win=win, text= player1 + ' wins! ' + str(wins_p1) + '-' + str(wins_p2), pos=[0, -0.1* screen_dim[1]], wrapWidth=screen_dim[0]/2, color=black, units='pix', height=screen_dim[1]/8) 
    winner_subject=player1
elif wins_p2>wins_p1:
    Final_result_text =visual.TextStim(win=win, text= player2 + ' wins! ' + str(wins_p2) + '-' + str(wins_p1), pos=[0, -0.1* screen_dim[1]], wrapWidth=screen_dim[0]/2, color=black, units='pix', height=screen_dim[1]/8) 
    winner_subject=player2
else:
    Final_result_text =visual.TextStim(win=win, text=' Draw! ' + str(wins_p2) + '-' + str(wins_p1), pos=[0, -0.1* screen_dim[1]], wrapWidth=screen_dim[0]/2, color=black, units='pix', height=screen_dim[1]/8) 
    winner_subject='draw'

Final_result_text.draw()
win.flip()
core.wait(10)

win.close()

df['winner_round'] = winner_subject
df['b_p1'] = int(b_pl1)
df['b_p2'] = int(b_pl2)
df['repetition'] = int(b_n)

###
df['resp1']=df['resp1'].replace(['rock', 'scissor', 'paper'], ['r', 's', 'p'])
df['resp2']=df['resp2'].replace(['rock', 'scissor', 'paper'], ['r', 's', 'p'])

###
randomness_p1 =  round(randomness_sequence(list(df['resp1'].values) )[0], 3) 
randomness_p2 =  round(randomness_sequence(list(df['resp2'].values) )[0], 3) 

df['randomness_p1']=randomness_p1
df['randomness_p2']=randomness_p2


lk_r_p1 = randomness_sequence(list(df['resp1'].values) )[1]
lk_r_p2 = randomness_sequence(list(df['resp2'].values) )[1]

for i in range(0, len(lk_r_p1)):
    df['p1_lik_' +str(i+1)] = lk_r_p1[i]
    df['p2_lik_' +str(i+1)] = lk_r_p2[i]

###
name_df = b_n + '_' + player1 + '_' + player2 + '.xlsx'
df.to_excel(root_save + name_df )
 






