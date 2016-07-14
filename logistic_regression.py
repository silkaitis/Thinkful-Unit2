
# coding: utf-8

# In[10]:

import pandas as pd
import statsmodels.api as sm
import math
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')


# In[3]:

loansData=pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.dropna(inplace=True)
loansData['FICO.Score']=loansData['FICO.Range'].str.split('-',expand=True).astype(int)[0]
loansData['Interest.Rate']=loansData['Interest.Rate'].str.strip('%').astype(float)
loansData['IR_TF']=[0 if x < 12 else 1 for x in loansData['Interest.Rate']]


# In[6]:

loansData['Intercept']=1
ind_vars=['Amount.Funded.By.Investors','FICO.Score','Intercept']


# In[7]:

logit=sm.Logit(loansData['IR_TF'],loansData[ind_vars])
result=logit.fit()
coeff=result.params
print(coeff)


# In[8]:

def logistic_function(FICO,LoanAmt,coeff):
    prob = 1/(1 + math.exp(coeff[2] + (coeff[1]*FICO) +(coeff[0]*LoanAmt)))
    return(round(prob,3))


# In[9]:

logistic_function(720,10000,coeff)


# In[15]:

p1 = [logistic_function(x,10000,coeff) for x in range(550,950)]
p2 = [logistic_function(x,10000,-1*coeff) for x in range(550,950)]
plt.plot(range(550,950),p1)
plt.plot(range(550,950),p2)
plt.legend(['Coeff','-Coeff'])
plt.show()


# In[19]:

loansData[loansData['Amount.Funded.By.Investors']==10000].head()


# In[21]:

plt.scatter(loansData['Amount.Funded.By.Investors'],loansData['Interest.Rate'])


# In[24]:

cd Desktop/Python/Thinkful/Thinkful-Unit2/

