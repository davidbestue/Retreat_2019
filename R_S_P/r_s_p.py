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


### Acumulate randomness
Acumulate_randomness = []
control_randomness =[]
### formula to now all the possible combinations
#m**n (m is 3: 'p, r, s', and n is the group (2, 3.... (n-1)))
m=3


for n in range(1, int(N/2)): ##length of grouping
    
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
        print( 'No rep freq of ' + str(n))
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
            print( 'Rep of ' + str(n) + ', p_value = ' + str(p_value))
                
                
        
        else: ## memory error
            print( 'Rep of ' + str(n))
            Acumulate_randomness.append(m**n * 1/0.05)
            control_randomness.append(m**n * 1/1)





control =  sum(control_randomness)
rand_seq = round( sum(Acumulate_randomness) - control, 3)

print('')
print('Randomness of the sequence: ')
##### Bigger the number, less random is!!!!!
print(rand_seq)



####### formula for likelihood in multinomial

# https://en.wikipedia.org/wiki/Multinomial_test


freq_obs=[5,4,1,2.5.7]

p_i = freq_obs / N 
n_i = m**n / N

lk = -2 * sum( freq_obs[i] * np.log( n_i / p_i )])


q2 = 1+(m**n + 1 / 6*N ) + ( (m**n)**2 / 6*N**2)



### groups as Lluis said


for n in range(3, 4): ##length of grouping   1,   int(N/2)
    
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
        N = len(sublists[n_analysis]) ### for the formula
        seq_anal_p = pd.DataFrame(seq_anal)
        unique = seq_anal_p[0].unique()
        
        ## Count the unique
        f_obs_filt_rep=[]
        for i in unique:
            f_obs_filt_rep.append(list(seq_anal).count(i))
        
        
        summatory = []
        for x in f_obs_filt_rep:
            summatory.append( x * np.log())
        
        p_i = np.array(f_obs_filt_rep)/N
        n_exp = m**n / N
        n_i =[n_exp for i in range(0, len(p_i))]
        

        













    

