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



