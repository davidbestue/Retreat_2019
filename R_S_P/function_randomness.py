# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 15:39:10 2019

@author: David
"""

import string
import random
from scipy.stats import chisquare
import itertools
import pandas as pd
import numpy as np
from scipy import stats


def randomness_sequence(seq):
    
    m=3
    N = len(seq)
    likelihood_ratios = []
    for n in range(1, int(N/2)+1): ##length of grouping   1,   int(N/2)
        
        ### All possible combinations   
        s=""
        all_poss_comb = [s.join(seq[i: i+n ]) for i in range(0, len(seq) - (n-1)) ]
        ##
        sublists = []
        for len_n in range(0, n):
            idxs = np.arange(len_n, len(all_poss_comb), n)
            sublists.append( np.take(all_poss_comb, idxs) )
        
        
        #just take the ones with at least 2 inside
        sublists = np.array(sublists)[np.array([len(sublists[i]) for i in range(0, len(sublists))])>1]
        #print(len(sublists))
        
        subl_lik = []
        for n_analysis in range(0, len(sublists)):
            seq_anal = sublists[n_analysis]
            N_s = len(sublists[n_analysis]) ### for the formula
            seq_anal_p = pd.DataFrame(seq_anal)
            unique = seq_anal_p[0].unique()
            
            ## Count the unique
            f_obs_filt_rep=[]
            for i in unique:
                f_obs_filt_rep.append(list(seq_anal).count(i))
            
            
            summatory = []
            n_exp = float(1)/m**n 
            for x in f_obs_filt_rep:
                summatory.append( x * np.log(n_exp/ (float(x)/N_s )))
            
            likelihood_ratio = -2*sum(summatory)
            #https://en.wikipedia.org/wiki/Multinomial_test
            correction = 1 + ( (m**n +1) /  6*N_s   ) + ((m**n)**2 / 6*N_s**2)
            likelihood_ratio_c = likelihood_ratio / correction
            subl_lik.append(likelihood_ratio_c)
        
        ###
        likelihood_ratios.append(np.mean(subl_lik))
    
            
    
            
    sums_lk_ch = sum(likelihood_ratios)
    return sums_lk_ch, likelihood_ratios







    

