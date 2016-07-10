# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 10:12:58 2016

@author: Danius
"""
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

plt.close('all')

loansData=pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.dropna(inplace=True)

cases=['Amount.Requested','Amount.Funded.By.Investors']

for case in cases:
    plt.figure()
    loansData.boxplot(column=case)
    plt.show()
    plt.title(case)
    plt.ylabel('Dollars')
    plt.savefig('%s.png' % case)
    
    loansData.hist(column=case)
    plt.show()
    plt.title(case)
    plt.xlabel('Dollars')
    plt.ylabel('Frequency')
    plt.savefig('Hist-%s.png' % case)
    
    plt.figure()
    stats.probplot(loansData[case],dist='norm',plot=plt)
    plt.show()
    plt.title(case)
    plt.xlabel('Quantiles')
    plt.ylabel('Ordered Values')
    plt.savefig('QQ-%s.png' % case)

#Amount Funded versus Amount Requested

#There are subtle differences between the amount
#requested and funded. Investors are more likely to grant loans 
#within the $3,500 to $14,000 range.  The number of loans outside
#this range is less than the number of requests and vice versa
#within this range. Requests too small may receive a larger loan
#and requests too large may receive a smaller loan. 