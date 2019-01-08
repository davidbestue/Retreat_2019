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
#from psychopy import gui  ### the gui makes competence with easygui! you do not need it!
from psychopy import visual, core, event
import pandas as pd
import os
import glob

import easygui
from easygui import multenterbox


#Dialogue box for subject name
screen_dim =[1600, 900]
min_bet_perc=1
max_bet_perc=30


root_imgs = os.getcwd() + '\\images\\' 

msg = 'Names '
title = "Subjects information"
fieldNames = ["Player1", "Player2"]
fieldValues = multenterbox(msg,title, fieldNames)
player1 = fieldValues[0]
player2 = fieldValues[1]


win = psychopy.visual.Window(size=screen_dim, units="pix", pos=(0, 0), fullscr=False, allowGUI=True)



for trial in range(0, len(stims)):
    
    #Trial number
    trial_number=visual.TextStim(win=win, text= str(trial) + '/' +str(len(stims)) , pos=[screen_dim[0]/3, screen_dim[1]/2.3], wrapWidth=screen_dim[0]/2, color=[1,1,1], units='pix', height=screen_dim[1]/25) 
    trial_number.draw()
    
    #Select the images
    card1 = path + '/Vector-Playing-Cards-master/cards-png/' + stims.iloc[trial].card1
    card2 = path + '/Vector-Playing-Cards-master/cards-png/' + stims.iloc[trial].card2
    
    image1 = psychopy.visual.ImageStim(win=win, image=card1 , units='pix',size=(250,350), ori=0, pos=(150, 100))                                                                                                                                                   
    image2 = psychopy.visual.ImageStim(win=win, image=card2 , units='pix',size=(250,350), ori=0, pos=(-150, 100))                                                     
    
    #Draww and display
    image1.draw()                                                                                                                                                 
    image2.draw()
    win.flip()
    
    core.wait(1)
