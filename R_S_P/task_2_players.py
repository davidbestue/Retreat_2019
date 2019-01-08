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
import pyglet


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
key=pyglet.window.key
keyboard = key.KeyStateHandler()
win.winHandle.push_handlers(keyboard)



for trial in range(0, rounds):
    
    #Trial number
    trial_number=visual.TextStim(win=win, text= str(trial) + '/' +str(rounds) , pos=[screen_dim[0]/3, screen_dim[1]/2.3], wrapWidth=screen_dim[0]/2, color=[1,1,1], units='pix', height=screen_dim[1]/25) 
    trial_number.draw()
    
    #Names players
    pl1=visual.TextStim(win=win, text=player1, pos=[ -0.25* screen_dim[0],  0.25* screen_dim[1]], wrapWidth=screen_dim[0]/2, color=[1,1,1], units='pix', height=screen_dim[1]/15) 
    pl2=visual.TextStim(win=win, text=player2, pos=[ +0.25* screen_dim[0],  0.25* screen_dim[1]], wrapWidth=screen_dim[0]/2, color=[1,1,1], units='pix', height=screen_dim[1]/15) 
    pl1.draw()
    pl2.draw()
    
    
    #play instruction
    play_txt=visual.TextStim(win=win, text='Play!', pos=[0, -0.1* screen_dim[1]], wrapWidth=screen_dim[0]/2, color=black, units='pix', height=screen_dim[1]/10) 
    play_txt.draw()
    
    p1_dec = 'None'
    p2_dec = 'None'
    
    while p1_dec == 'None' or p2_dec == 'None':
        
        ##      
        print(p1_dec, p2_dec)
        #
        if keyboard[key.A]:
            p1_dec = 'left'
        
        if keyboard[key.L]:
            p2_dec = 'right'      
    
    
    print(p1_dec, p2_dec)
        
        
    
    
    #scape loop
    if keyboard[key.E]:
        win.close()
    
    
    #######
    
    if mouse_click[0]: #keyboard[key.A]:
        mov_ang=1

    
    rock = root_imgs + 'rock.png'
    rock_img = psychopy.visual.ImageStim(win=win, image=rock , units='pix',size=(250,350), ori=0, pos=(150, 100))                                                           
    #Draww and display
    rock_img.draw()                                                                                                                                                 
    win.flip()
    
    core.wait(1)
    
    



rock = root_imgs + 'rock.png'
rock_img = psychopy.visual.ImageStim(win=win, image=rock , units='pix',size=(screen_dim[1]/2.5,screen_dim[1]/2.5), ori=0, pos=(150, 100))                                                           
rock_img.draw()                                                                                                                                                 
win.flip()

scissors = root_imgs + 'scissor.png'
scissors_img = psychopy.visual.ImageStim(win=win, image=scissors , units='pix',size=(screen_dim[1]/2.5,screen_dim[1]/2.5), ori=0, pos=(150, 100))                                                           
scissors_img.draw()                                                                                                                                                 
win.flip()


paper = root_imgs + 'paper.png'
paper_img = psychopy.visual.ImageStim(win=win, image=paper , units='pix',size=(screen_dim[1]/2.5,screen_dim[1]/2.5), ori=0, pos=(150, 100))                                                           
paper_img.draw()                                                                                                                                                 
win.flip()




