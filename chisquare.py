# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 19:23:50 2016

@author: Danius
"""

import collections

import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.close('all')
#%%
loansData=pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.dropna(inplace=True)
#%%
freq=collections.Counter(loansData['Open.CREDIT.Lines'])
plt.figure()
plt.bar(freq.keys(),freq.values(),width=1)
plt.title('Open.CREDIT.Lines')
plt.xlabel('Number of Credit Lines')
plt.ylabel('Frequnecy')
plt.show()
#%%
chi, p = stats.chisquare(freq.values())
print('Chi = %f' % chi)
print('p = %f' % p)
#%%
#What if a random distribution is inputed into the Chi-square function?
randfreq=[np.random.randint(min(freq.keys()),max(freq.keys())) for i in range(0,len(freq))]

plt.figure()
plt.bar(freq.keys(),randfreq,width=1)
plt.title('Random Frequency')
plt.show()

chiR, pR = stats.chisquare(freq.values(),randfreq)
print('Chi = %f' % chiR)
print('p = %f' % pR)
#P remains zero because the random distribution doesn't match
#the data at all.
