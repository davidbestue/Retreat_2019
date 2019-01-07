# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 11:18:34 2019

@author: David
"""

#### Analysis beer competition

import pandas as pd
import numpy as np
import itertools

### Random data
a = np.random.randint(2, size=100)
b = np.random.randint(2, size=100)

df = pd.DataFrame({'blind':a, 'seen':b})

subjects = ['alba', 'delfi', 'anna', 'sandra', 'david', 'mariona', 'rosa', 'joao', 'genis', 'albert']
subj_st = []
comb = []
for s in subjects:
    subj_st.append([ s for x in range(0,10)])
    comb.append([ str(i) for i in range(1,11)])    

df['subj'] = list(itertools.chain.from_iterable(subj_st))
df['comb'] = list(itertools.chain.from_iterable(comb))