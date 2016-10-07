
# coding: utf-8

# In[23]:

import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
# get_ipython().magic(u'matplotlib inline')


# In[5]:

loansData=pd.read_csv('https://github.com/Thinkful-Ed/curric-data-001-data-sets/raw/master/loans/loansData.csv')
loansData.dropna(inplace=True)
loansData['Interest.Rate']=loansData['Interest.Rate'].str.strip('%').astype(float)
loansData['Yearly.Income']=loansData['Monthly.Income']*12
loansData['Home_Coded']=pd.Categorical(loansData['Home.Ownership']).codes


# In[6]:

loansData[['Home.Ownership','Home_Coded']].tail()


# In[7]:

#Univariate Model
#int_rate = f(yearly.income)
model=smf.ols(formula='loansData["Interest.Rate"] ~ loansData["Yearly.Income"]',data=loansData)
results=model.fit()

print(results.summary())

#The model shows that yearly income is significant in predicting the interest rate for a loan but
#it doesn't match the data well (R-squared = 0)


# In[8]:

#Multivariate Model
#int_rate = f(yearly.income)
model=smf.ols(formula='loansData["Interest.Rate"] ~ loansData["Yearly.Income"] + loansData["Home_Coded"]',data=loansData)
results=model.fit()

print(results.summary())

#The model shows that yearly income is significant while home ownership is not significant
#in predicting the interest rate for a loan. The model doesn't match the data well (R-squared = 0.007)


# In[9]:

#Multivariate Model
#int_rate = f(yearly.income, home_coded, yearly.income * home_coded)

model=smf.ols(formula='loansData["Interest.Rate"] ~ loansData["Yearly.Income"] * loansData["Home_Coded"]',data=loansData)
results=model.fit()

print(results.summary())

#The model shows that yearly income, home ownership and the interaction are significant in predicting the
#interest rate for a loan.  Home ownership was not significant in the previous model but it is now significant.
#The switch in significance is due to the interaction term.  Home ownership has to be included in the model to correctly
#describe the interaction term.  Additionally, R-squared is nearly zero so other significant variables are missing from
#this model.  Graphing the data illustrates the lack of fit of the model.


# In[24]:

plt.scatter(loansData['Yearly.Income'],loansData['Interest.Rate'])

codes=[0,2,3]
for c in codes:
    hRate=loansData[loansData['Home_Coded']==c]['Interest.Rate']
    hIncome=sm.add_constant(loansData[loansData['Home_Coded']==c]['Yearly.Income'])
    model=sm.OLS(hRate,hIncome)
    results=model.fit()
    mIncome=range(int(min(hIncome['Yearly.Income'])),int(max(hIncome['Yearly.Income'])),1000)
    mRate=[float(results.params[0])+float(results.params[1])*x for x in mIncome]
    plt.plot(mIncome,mRate)

plt.title('Interest Rate vs Yearly Income')
plt.xlabel('Yearly Income')
plt.ylabel('Interest Rate')
plt.legend(['Mortgage','Own','Rent'])
plt.savefig('YearlyIncome_vs_InterestRate', dpi = 100)
plt.show()
