# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 16:20:29 2019

@author: David
"""



import string
import random
from scipy.stats import chisquare
import itertools
import pandas as pd
import numpy as np



#### Generate a sequence of rsq
def id_generator(size=6, chars=['r', 's', 'p']): #'r', 's', 'p'
    return ''.join(random.choice(chars) for _ in range(size))

id_generator()

N=50
id_generator(N)

a = id_generator(N)
seq = [a[x] for x in range(0, N)]    



m=3
N = len(seq)
likelihood_ratios = []
for n in range(1, 5): ##length of grouping   1,   int(N/2)
    print(n)
    ### All possible combinations   
    s=""
    all_poss_comb = [s.join(seq[i: i+n ]) for i in range(0, len(seq) - (n-1)) ]
    ##
    partitions = []
    for len_n in range(0, n):
        idxs = np.arange(len_n, len(all_poss_comb), n)
        partitions.append( np.take(all_poss_comb, idxs) )
        
    
    partitions = np.array(partitions)[np.array([len(partitions[i]) for i in range(0, len(partitions))])>1]
    
    likelihood_ratio_partitions = []
    for idx_part in range(0, len(partitions)):
        partition_single = partitions[idx_part]
        N_s = len(partitions[idx_part]) ### for the formula
        partition_single_df = pd.DataFrame(partition_single)
        unique = partition_single_df[0].unique()
        
        ## Count the unique
        x_item_obs=[] #count of diff item inside each partition
        for i in unique:
            x_item_obs.append(list(partition_single).count(i))
        
        
        summatory = []
        f_item_h0 = float(1)/m**n #frequency expected of each item with random h0
        for x_i in x_item_obs:
            summatory.append( x_i * np.log(f_item_h0/ (float(x_i)/N_s )))
        
        likelihood_ratio = -2*sum(summatory)
        #https://en.wikipedia.org/wiki/Multinomial_test
        correction = 1 + ( (m**n +1) /  (6*N_s)   ) + ((m**n)**2 / (6*N_s**2)   )
        likelihood_ratio_single_partition_c = likelihood_ratio / correction
        likelihood_ratio_partitions.append(    likelihood_ratio_single_partition_c   )
    
    ###
    likelihood_ratios.append(np.mean(  likelihood_ratio_partitions  ))
    score = np.mean(likelihood_ratios)
    
            
            
        
###### Higher the value, less random        
        
        
        
        
        
        