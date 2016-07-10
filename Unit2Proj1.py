# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 07:33:08 2016

@author: Danius
"""

import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.split('\n')
data = [i.split(',') for i in data]
df=pd.DataFrame(data[1::],columns=data[0])
df['Alcohol']=df['Alcohol'].astype(float)
df['Tobacco']=df['Tobacco'].astype(float)

for col in df.columns:
    col=str(col)
    if col != 'Region':
        print('The mean of the %s dataset is %.2f' % (col,df[col].mean()))
        print('The median of the %s dataset is %.2f' % (col,df[col].median()))
        print('The mode of the %s dataset is %.2f' % (col,stats.mode(df[col])[0][0]))
        print('The range of the %s dataset is %.2f' % (col,max(df[col])-min(df[col])))
        print('The variance of the %s dataset is %.2f' % (col,df[col].var()))
        print('The standard deviation of the %s dataset is %.2f\n' % (col,df[col].std()))

col = 'Alcohol and Tobacco'
fulldata = pd.concat([df['Alcohol'],df['Tobacco']])
print('The mean of the %s dataset is %.2f' % (col,fulldata.mean()))
print('The median of the %s dataset is %.2f' % (col,fulldata.median()))
print('The mode of the %s dataset is %.2f' % (col,stats.mode(fulldata)[0][0]))
print('The range of the %s dataset is %.2f' % (col,max(fulldata)-min(fulldata)))
print('The variance of the %s dataset is %.2f' % (col,fulldata.var()))
print('The standard deviation of the %s dataset is %.2f\n' % (col,fulldata.std()))