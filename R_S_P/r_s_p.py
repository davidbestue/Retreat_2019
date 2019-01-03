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



#### Generate a sequence of rsq
def id_generator(size=6, chars=['r', 's', 'p']): #'r', 's', 'p'
    return ''.join(random.choice(chars) for _ in range(size))

id_generator()

N=1000
id_generator(N)

a = id_generator(N)
seq = [a[x] for x in range(0, N)]    

### Acumulate randomness
Acumulate_randomness = []

### formula to now all the possible combinations
#m**n (m is 3: 'p, r, s', and n is the group (2, 3.... (n-1)))
m=3


for n in [2,3]: ##length of grouping
    
    ### All possible combinations   
    s=""
    all_poss_comb = [s.join(seq[i: i+n ]) for i in range(0, len(seq) - (n-1)) ]
    all_p = pd.DataFrame(all_poss_comb)
    unique = all_p[0].unique()
    
    ### start checking for repeted sequences
    f_obs_filt_rep=[]
    for i in unique:
        f_obs_filt_rep.append(all_poss_comb.count(i))
        
    #no repeted subsequences
    if len(pd.DataFrame(f_obs_filt_rep)[0].unique()) == 1:  
        print( 'No rep freq for ' + str(n))
    
    #there are repeted subsequences
    else: 
        
        if n<15:
            
            f_obs=np.zeros(m**n)
            
            for idx,i in enumerate(unique):
                f_obs[idx] = all_poss_comb.count(i)
            
            f_obs = list(f_obs)
            
            f_exp = [ len(all_poss_comb)/m**n for i in range(0, len(f_obs))]
            
            print(chisquare(f_obs, f_exp))
            if chisquare(f_obs, f_exp)[1]<0.05:
                Acumulate_randomness.append(m**n)
        
        else: ## memory error
            print( 'Rep of ' + str(n))
            Acumulate_randomness.append(m**n)



    
    
    
    

