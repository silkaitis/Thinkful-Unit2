# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 09:55:39 2016

@author: Danius
"""
import matplotlib.pyplot as plt
import scipy.stats as stats

x=[1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.figure()
plt.boxplot(x)
plt.title('Boxplot')
plt.ylabel('Values')
plt.show()
plt.savefig('Boxplot.png')

plt.figure()
plt.hist(x,histtype='bar')
plt.title('Histogram')
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.show()
plt.savefig('Histogram.png')

plt.figure()
stats.probplot(x,dist='norm',plot=plt)
plt.xlabel('Quantiles')
plt.ylabel('Ordered Values')
plt.show()
plt.savefig('Probability Plot.png')