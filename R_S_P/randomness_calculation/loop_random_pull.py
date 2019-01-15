# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 15:53:01 2018

@author: David
"""

import string
import random
from scipy.stats import chisquare
import itertools
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as sns
import matplotlib.pyplot as plt



#### Generate a sequence of rsq
def id_generator(size=6, chars=['r', 's', 'p']): #'r', 's', 'p'
    return ''.join(random.choice(chars) for _ in range(size))

id_generator()



sums=[]
for s in range(0,10000):
    N=50
    id_generator(N)
    
    a = id_generator(N)
    seq = [a[x] for x in range(0, N)]    
    
    #a=[['r', 's', 'p', 'p', 'p'] for i in range(0,2)]
    #a=list(itertools.chain.from_iterable(a))
    #b = id_generator(90)
    #b = [b[x] for x in range(0, 90)]  
    #seq=a+b
      
    ### Acumulate randomness
    Acumulate_randomness = []
    control_randomness =[]
    ### formula to now all the possible combinations
    #m**n (m is 3: 'p, r, s', and n is the group (2, 3.... (n-1)))
    m=3
    
    ### groups as Lluis said
    
    likelihood_ratios = []
    for n in range(1, int(N/2)): ##length of grouping   1,   int(N/2)
        
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
            n_exp = 1/m**n 
            for x in f_obs_filt_rep:
                summatory.append( x * np.log(n_exp/ (x/N_s )))
            
            likelihood_ratio = -2*sum(summatory)
            likelihood_ratios.append(likelihood_ratio)
    
            
    
            
    sums_lk_ch = sum(likelihood_ratios)
    sums.append(sums_lk_ch)





sums_random = sums
sns.distplot(sums_random)
stats.shapiro(sums_random)

np.save('random_val_50.npy', np.array(sums_random))
radnom_dist = np.load('random_val_50.npy')
sns.distplot(radnom_dist)
plt.show()







    

