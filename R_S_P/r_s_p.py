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

N=100
id_generator(N)

a = id_generator(N)
seq = [a[x] for x in range(0, N)]    
seq = [int(seq[i]) for i in range(0, len(seq))]  


#### Direct distribution
f_r = seq.count('r')
f_s = seq.count('s')
f_p = seq.count('p')
chisquare([f_r, f_s, f_p], f_exp=[len(seq)/3, len(seq)/3, len(seq)/3])


### Acumulate randomness

Acumulate_randomness = []



### formula

#m**n (m is 3: 'p, r, s', and n is the group (2, 3.... (n-1)))
m=3

#### All Consecutive pairs

n=2

all_pairs=[]

for i in range(0, n):
    all_pairs.append( [seq[a]+ seq[a+1] for a in range(i,len(seq)-n,2) ] )



#### Once you have the list of all the data
all_p_list = list(itertools.chain.from_iterable(all_pairs))
all_p = pd.DataFrame(all_p_list)

unique = all_p[0].unique()
f_obs=np.zeros(m**n)

for idx,i in enumerate(unique):
    f_obs[idx] = all_p_list.count(i)

f_obs = list(f_obs)

f_exp = [ len(all_p_list)/m**n for i in range(0, len(f_obs))]

if chisquare(f_obs, f_exp)[1]<0.05:
    Acumulate_randomness.append(m**n)





### trios
all_trios=[]

n=3
for i in range(0, n):
    all_trios.append( [seq[a]+ seq[a+1] + seq[a+2] for a in range(i,len(seq)-((n+1)-i)) ] )


list(itertools.chain.from_iterable(all_trios))



