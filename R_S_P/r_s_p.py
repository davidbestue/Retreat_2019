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
#seq = [int(seq[i]) for i in range(0, len(seq))]  


#### Direct distribution
#f_r = seq.count('r')
#f_s = seq.count('s')
#f_p = seq.count('p')
#chisquare([f_r, f_s, f_p], f_exp=[len(seq)/3, len(seq)/3, len(seq)/3])


### Acumulate randomness

Acumulate_randomness = []



### formula

#m**n (m is 3: 'p, r, s', and n is the group (2, 3.... (n-1)))
m=3

#### All Consecutive pairs

s=""
n = 6
all_poss_comb = [s.join(seq[i: i+n ]) for i in range(0, len(seq) - (n-1)) ]

#### Once you have the list of all the data
all_p = pd.DataFrame(all_poss_comb)

unique = all_p[0].unique()

if n<15:
    f_obs=np.zeros(m**n)
    
    for idx,i in enumerate(unique):
        f_obs[idx] = all_poss_comb.count(i)
    
    f_obs = list(f_obs)
    
    f_exp = [ len(all_poss_comb)/m**n for i in range(0, len(f_obs))]
    
    if chisquare(f_obs, f_exp)[1]<0.05:
        Acumulate_randomness.append(m**n)

else: ## memory error
    f_obs=[]
    for i in unique:
        f_obs.append(all_poss_comb.count(i))
    


#####################
        ##################
        ###################




for n in [2,3]:

f_obs_filt_rep=[]
for i in unique:
    f_obs_filt_rep.append(all_poss_comb.count(i))
    

if len(pd.DataFrame(f_obs_filt_rep)[0].unique()) == 1:  #no repeted subsequences
    print( 'No rep freq for ' + str(n))

else: #there are repeted subsequences
    
    
    if n<15:
        
        f_obs=np.zeros(m**n)
        
        for idx,i in enumerate(unique):
            f_obs[idx] = all_poss_comb.count(i)
        
        f_obs = list(f_obs)
        
        f_exp = [ len(all_poss_comb)/m**n for i in range(0, len(f_obs))]
        
        print(chisquare(f_obs, f_exp)[1])
        if chisquare(f_obs, f_exp)[1]<0.05:
            Acumulate_randomness.append(m**n)
    
    else: ## memory error
        print( 'Rep of ' + str(n))
        Acumulate_randomness.append(m**n)



    
    
    
    


### trios
all_trios=[]

n=3
for i in range(0, n):
    all_trios.append( [seq[a]+ seq[a+1] + seq[a+2] for a in range(i,len(seq)-((n+1)-i)) ] )


list(itertools.chain.from_iterable(all_trios))



##########################################
##########################################



s=""

n = 50
all_poss_comb = [s.join(seq[i: i+n ]) for i in range(0, len(seq) - (n-1)) ]



print(combinations[0][-3:])
print(combinations[1][-3:])
print(seq[-6:])


