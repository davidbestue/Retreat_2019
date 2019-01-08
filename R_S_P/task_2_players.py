# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:02:54 2019

@author: David
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



#Dialogue box for subject name
screen_dim =[1600, 900]

rounds=2

black=[-1,-1,-1]

root_imgs = os.getcwd() + '\\images\\' 

msg = 'Names '
title = "Subjects information"
fieldNames = ["Player_left", "Player_right"]
fieldValues = multenterbox(msg,title, fieldNames)
player1 = fieldValues[0]
player2 = fieldValues[1]


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
    list_options = ["left", "right", "up", "a", "w", "d"]
    
    while len(decisions)<2:
        keys_pressed= psychopy.event.waitKeys(keyList=list_options)
        #print(keys_pressed)
        decisions.append(keys_pressed[0])
        if keys_pressed[0] in ["left", "right", "up"]:
            list_options = ["a", "w", "d"]
        else:
            list_options = ["left", "right", "up"]
    
    
    ##
    #print(decisions)
    #print('Done!')
    if decisions[0] in ['a', 'w', 'd']:
        pl1_resp = decisions[0]
        pl2_resp = decisions[1]
    else:
        pl1_resp = decisions[1]
        pl2_resp = decisions[0] 
    
    ## convert to rock, paper, scissor
    if pl1_resp =='a':
        pl1_resp = 'rock'
    elif pl1_resp =='w':
        pl1_resp = 'paper'
    elif pl1_resp =='d':
        pl1_resp = 'scissor'
    
    #
    if pl2_resp =='left':
        pl2_resp = 'rock'
    elif pl2_resp =='up':
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
    core.wait(2)
    responses.append([player1, player2, pl1_resp, pl2_resp, winner])
    







