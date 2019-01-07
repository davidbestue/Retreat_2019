# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:18:34 2019

@author: David
"""

#### Analysis beer competition

import pandas as pd
import numpy as np
import itertools
import matplotlib.pyplot as plt
import seaborn as sns

### Random data
a = np.random.randint(2, size=100)
b = np.random.randint(2, size=100)

df = pd.DataFrame({'blind':a, 'seen':b})

subjects = ['alba', 'delfi', 'anna', 'sandra', 'david', 'mariona', 'rosa', 'joao', 'genis', 'albert']
b1 = ['heineken', 'heineken', 'heineken', 'heineken', 'e_dam', 'e_dam',   'e_dam',  'e_gal',  'e_gal',  'cruzcampo']
b2 = ['china',    'cruzcampo', 'e_gal',    'e_dam',   'china', 'cruzcampo', 'e_gal', 'china', 'cruzcampo', 'china']

subj_st = []
comb = []
b1s = []
b2s = []


for s in subjects:
    subj_st.append([ s for x in range(0,10)])
    comb.append([ str(i) for i in range(1,11)])    
    b1s.append(b1)
    b2s.append(b2)

df['subj'] = list(itertools.chain.from_iterable(subj_st))
df['comb'] = list(itertools.chain.from_iterable(comb))
df['beer1'] = list(itertools.chain.from_iterable(b1s))
df['beer2'] = list(itertools.chain.from_iterable(b2s))


##
# column of consistency (1: you are consisten blind-seen, 0:not consistent)
df['int'] = 1
df['consistency'] = abs( df['blind'] - df['seen'] )

## Subjcet consistency.
plt.figure()
plt.title('Consistency of subjects')
sns.factorplot(x='subj', y='consistency', kind='bar', data=df)
plt.plot([0, len(df.subj.unique())-1], [0.5, 0.5], 'k--')
plt.show(block=False)

## Population consistency
## Subjcet consistency.
plt.figure()
plt.title('Consistency of subjects')
sns.factorplot(x='int', y='consistency', kind='bar', data=df)
plt.plot([-1, 1], [0.5, 0.5], 'k--')
plt.show(block=False)


############
############## rank of beers
############

blind_win=[]
seen_win=[]

for i in range(0, len(df)):
    ### blind
    res = df['blind'].iloc[i]
    if res == 0:
        blind_win.append(  df['beer1'].iloc[i]  )
    elif res==1:
        blind_win.append(  df['beer2'].iloc[i]  )
    
    ### seen
    res_s = df['seen'].iloc[i]
    if res_s == 0:
        seen_win.append(  df['beer1'].iloc[i]  )
    elif res_s ==1:
        seen_win.append(  df['beer2'].iloc[i]  )



df['blind_win'] = blind_win
df['seen_win'] = seen_win 


beers=[]
counts_b=[]
counts_s=[]
for beer in df['blind_win'].unique():
    beers.append(beer)
    counts_b.append( df.loc[df.blind_win == beer, 'blind_win'].count())
    counts_s.append( df.loc[df.seen_win == beer, 'seen_win'].count())


##   
df_b = pd.DataFrame({ 'beer':beers, 'counts': counts_b}) 
df_b['condition'] = 'blind'
#
df_s = pd.DataFrame({ 'beer':beers, 'counts': counts_s}) 
df_s['condition'] = 'seen'

df_b_s = pd.concat([df_b, df_s])


plt.figure()
plt.title('Rank')
sns.factorplot(x='beer', y='counts', hue='condition', kind='bar', data=df_b_s)
plt.show(block=False)


#####
df_bs = pd.DataFrame({ 'beer':beers, 'counts_b': counts_b, 'counts_s': counts_s}) 
df_bs['social_overrating'] = df_bs['counts_b'] - df_bs['counts_s']

plt.figure()
plt.title('Social overrating') ## if +, the beer is socaily overrated. If -, it is socially underrated
sns.factorplot(x='beer', y='social_overrating', kind='bar', data=df_bs)
plt.show(block=False)
        
    






