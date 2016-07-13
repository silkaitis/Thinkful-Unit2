# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 19:10:17 2016

@author: Danius
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

#%%
#Load Data and Clean
loansData=pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData['FICO.Score']=loansData['FICO.Range'].str.split('-',return_type='frame').astype(int)[0]
loansData['Interest.Rate']=loansData['Interest.Rate'].str.strip('%').astype('float')/100
#%%
#Plot histogram of FICO.Score
plt.figure()
loansData['FICO.Score'].hist()
plt.title('FICO.Score')
plt.xlabel('FICO Score')
plt.ylabel('Frequency')
#%%
#Plot matrix of scatter plots
pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10))
#%%
#Load data into variables
intrate=loansData['Interest.Rate']
loanamt=loansData['Amount.Requested']
fico=loansData['FICO.Score']
#%%
#Create linear model
y=np.matrix(intrate).transpose()
x1=np.matrix(fico).transpose()
x2=np.matrix(loanamt).transpose()
x=np.column_stack([x1,x2])
X=sm.add_constant(x)
model=sm.OLS(y,X)
f=model.fit()
f.summary()

#%%
print('Model P-Values: '+', '.join([str(round(p)) for p in f.pvalues]))
print('Model R^2: '+str((round(f.rsquared,2))))