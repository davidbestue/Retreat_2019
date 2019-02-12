# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 17:16:55 2019

@author: David
"""

### Randomness old+


import string
import random
from scipy.stats import chisquare
import itertools
import pandas as pd
import numpy as np
from scipy import stats


def randomness_old(seq):
    ### Acumulate randomness
    Acumulate_randomness = []
    control_randomness =[]
    ### formula to now all the possible combinations
    #m**n (m is 3: 'p, r, s', and n is the group (2, 3.... (n-1)))
    m=3
    N=50   
    for n in range(1, int(N/2)):
        ##length of grouping        
        ### All possible combinations   
        s=""
        all_poss_comb = [s.join(seq[i: i+n ]) for i in range(0, len(seq) - (n-1)) ]
        all_p = pd.DataFrame(all_poss_comb)
        unique = all_p[0].unique()
        
        ##control
        #control_randomness.append(m**n * 1/1)
        
        ### start checking for repeted sequences
        f_obs_filt_rep=[]
        for i in unique:
            f_obs_filt_rep.append(all_poss_comb.count(i))
            
        #no repeted subsequences
        if len(pd.DataFrame(f_obs_filt_rep)[0].unique()) == 1:  
            #print( 'No rep freq of ' + str(n))
            #Acumulate_randomness.append(m**n * 1/1)
        
        #there are repeted subsequences
        else: 
            
            if n<15:
                
                f_obs=np.zeros(m**n)
                
                for idx,i in enumerate(unique):
                    f_obs[idx] = all_poss_comb.count(i)
                
                f_obs = list(f_obs)
                
                f_exp = [ len(all_poss_comb)/m**n for i in range(0, len(f_obs))]
                
                #print(chisquare(f_obs, f_exp))
                stat, p_value = chisquare(f_obs, f_exp)
                
                Acumulate_randomness.append(m**n * 1/p_value)
                control_randomness.append(m**n * 1/1)
                #print( 'Rep of ' + str(n) + ', p_value = ' + str(p_value))
                    
                    
            
            else: ## memory error
                #print( 'Rep of ' + str(n))
                Acumulate_randomness.append(m**n * 1/0.05)
                control_randomness.append(m**n * 1/1)
    
    
    
    
    
    control =  sum(control_randomness)
    rand_seq = round( sum(Acumulate_randomness) - control, 3)    
    return rand_seq