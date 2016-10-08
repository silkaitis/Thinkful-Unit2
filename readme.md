# Thinkful Unit 2 Exercises

**Purpose**

Explore and learn various tools available in Pandas, Statsmodels and Scipy

**Exercise Descriptions**

1. chisquare.py
  * Purpose
    * Determine if loan data fits a Chi-squared distribution.
  * Learning Objectives
    * Use Pandas to load data into a DataFrame
    * Generate histogram of the loan data using matplotlib
    * Calculate p-value of the chi-squared test using SciPy
  * Output
  ```
    Chi = 2408.43, p = 0.00
  ```
    ![Chi-square](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/Chi_square.png?raw=true)
2. linear_regression.py
  * Purpose
    * Build linear regression model of loan data; IntRate = f(FICO.Score, Amount.Requested)
  * Learning Objectives
    * Use Pandas to load data into a DataFrame
    * Generate scatter plot matrix to inspect data
    * Build linear regression model using OLS from statsmodels
  * Output
  ```
    OLS Regression Results
    ==============================================================================
    Dep. Variable:                      y   R-squared:                       0.657
    Model:                            OLS   Adj. R-squared:                  0.656
    Method:                 Least Squares   F-statistic:                     2388.
    Date:                Thu, 06 Oct 2016   Prob (F-statistic):               0.00
    Time:                        08:23:50   Log-Likelihood:                 5727.6
    No. Observations:                2500   AIC:                        -1.145e+04
    Df Residuals:                    2497   BIC:                        -1.143e+04
    Df Model:                           2
    Covariance Type:            nonrobust
    ==============================================================================
    coef    std err          t      P>|t|      [95.0% Conf. Int.]
    ------------------------------------------------------------------------------
    const          0.7288      0.010     73.734      0.000         0.709     0.748
    x1            -0.0009    1.4e-05    -63.022      0.000        -0.001    -0.001
    x2          2.107e-06    6.3e-08     33.443      0.000      1.98e-06  2.23e-06
    ==============================================================================
    Omnibus:                       69.496   Durbin-Watson:                   1.979
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):               77.811
    Skew:                           0.379   Prob(JB):                     1.27e-17
    Kurtosis:                       3.414   Cond. No.                     2.96e+05
    ==============================================================================
  ```
    ![scatter_matrix](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/loan_scatter_matrix.png?raw=true)
3. logistic_regression.py / logistic_regression.ipynb
  * Purpose
    * Build logistic regression model of loan data; IntRate = f(FICO.Score, Amount.Requested)
    * Determine if a person with a FICO score of 720 would obtain a loan for $10,000 at 12% interest.
  * Learning Objectives
    * Use Pandas to load data into a DataFrame
    * Generate scatter plot matrix to inspect data
    * Implement logistic regression method using Logit and OLS from statsmodels
    * Predict outcome from the OLS model
  * Output
  ```
    OLS Regression Results
    ==============================================================================
    Dep. Variable:          Interest.Rate   R-squared:                       0.619
    Model:                            OLS   Adj. R-squared:                  0.616
    Method:                 Least Squares   F-statistic:                     262.7
    Date:                Thu, 06 Oct 2016   Prob (F-statistic):           9.95e-36
    Time:                        08:31:48   Log-Likelihood:                -352.33
    No. Observations:                 164   AIC:                             708.7
    Df Residuals:                     162   BIC:                             714.9
    Df Model:                           1
    Covariance Type:            nonrobust
    ==============================================================================
    coef    std err          t      P>|t|      [95.0% Conf. Int.]
    ------------------------------------------------------------------------------
    const         78.8800      4.087     19.299      0.000        70.809    86.951
    FICO.Score    -0.0948      0.006    -16.207      0.000        -0.106    -0.083
    ==============================================================================
    Omnibus:                       46.629   Durbin-Watson:                   1.865
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):               88.422
    Skew:                           1.339   Prob(JB):                     6.30e-20
    Kurtosis:                       5.401   Cond. No.                     1.75e+04
    ==============================================================================
  ```
    ![log_func](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/Logistic_function.png?raw=true)
    ![loan_log_regress](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/Loan_Log_Regression.png?raw=true)
    * Model predicts an individual with a minimum FICO score of 705 would receive a loan for $10,000 with a 12% interest rate.
4. multivariate.py / multivariate.ipynb
  * Purpose
    * Build multivariate model of loan data; IntRate = f(Yearly_Income, Home_Ownership)
  * Learning Objectives
    * Use Pandas to load and clean data in a DataFrame
    * Create univariate model using statsmodels
    * Create multivariate models using statsmodels
    * Scatter plot Yearly_Income and Interest.Rate to check conclusions drawn from model performance
  * Output
  ```
      OLS Regression Results
    ======================================================================================
    Dep. Variable:     loansData["Interest.Rate"]   R-squared:                       0.000
    Model:                                    OLS   Adj. R-squared:                 -0.000
    Method:                         Least Squares   F-statistic:                    0.4168
    Date:                        Thu, 06 Oct 2016   Prob (F-statistic):              0.519
    Time:                                18:07:22   Log-Likelihood:                -7115.5
    No. Observations:                        2498   AIC:                         1.424e+04
    Df Residuals:                            2496   BIC:                         1.425e+04
    Df Model:                                   1
    Covariance Type:                    nonrobust
    ==============================================================================================
     coef    std err          t      P>|t|      [0.025      0.975]
    ----------------------------------------------------------------------------------------------
    Intercept                     12.9929      0.146     88.807      0.000      12.706      13.280
    loansData["Yearly.Income"]  1.136e-06   1.76e-06      0.646      0.519   -2.31e-06    4.59e-06
    ==============================================================================
    Omnibus:                       69.741   Durbin-Watson:                   1.989
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):               54.034
    Skew:                           0.273   Prob(JB):                     1.85e-12
    Kurtosis:                       2.530   Cond. No.                     1.45e+05
    ==============================================================================
  ```
  ```
      OLS Regression Results
    ======================================================================================
    Dep. Variable:     loansData["Interest.Rate"]   R-squared:                       0.007
    Model:                                    OLS   Adj. R-squared:                  0.006
    Method:                         Least Squares   F-statistic:                     8.274
    Date:                        Thu, 06 Oct 2016   Prob (F-statistic):           0.000262
    Time:                                18:07:22   Log-Likelihood:                -7107.5
    No. Observations:                        2498   AIC:                         1.422e+04
    Df Residuals:                            2495   BIC:                         1.424e+04
    Df Model:                                   2
    Covariance Type:                    nonrobust
    ==============================================================================================
    coef    std err          t      P>|t|      [0.025      0.975]
    ----------------------------------------------------------------------------------------------
    Intercept                     12.5221      0.187     66.918      0.000      12.155      12.889
    loansData["Yearly.Income"]  2.687e-06    1.8e-06      1.496      0.135   -8.36e-07    6.21e-06
    loansData["Home_Coded"]        0.2374      0.059      4.016      0.000       0.121       0.353
    ==============================================================================
    Omnibus:                       67.032   Durbin-Watson:                   1.990
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):               53.954
    Skew:                           0.281   Prob(JB):                     1.92e-12
    Kurtosis:                       2.550   Cond. No.                     1.90e+05
    ==============================================================================
  ```
  ```
      OLS Regression Results
    ======================================================================================
    Dep. Variable:     loansData["Interest.Rate"]   R-squared:                       0.008
    Model:                                    OLS   Adj. R-squared:                  0.007
    Method:                         Least Squares   F-statistic:                     6.588
    Date:                        Thu, 06 Oct 2016   Prob (F-statistic):           0.000197
    Time:                                18:07:22   Log-Likelihood:                -7105.9
    No. Observations:                        2498   AIC:                         1.422e+04
    Df Residuals:                            2494   BIC:                         1.424e+04
    Df Model:                                   3
    Covariance Type:                    nonrobust
    ======================================================================================================================
                             coef    std err          t      P>|t|      [0.025      0.975]
    ----------------------------------------------------------------------------------------------------------------------
    Intercept                                             12.6724      0.205     61.802      0.000      12.270      13.074
    loansData["Yearly.Income"]                          7.914e-07   2.09e-06      0.380      0.704    -3.3e-06    4.88e-06
    loansData["Home_Coded"]                                0.0736      0.109      0.675      0.499      -0.140       0.287
    loansData["Yearly.Income"]:loansData["Home_Coded"]  2.561e-06   1.43e-06      1.789      0.074   -2.47e-07    5.37e-06
    ==============================================================================
    Omnibus:                       66.657   Durbin-Watson:                   1.994
    Prob(Omnibus):                  0.000   Jarque-Bera (JB):               53.272
    Skew:                           0.277   Prob(JB):                     2.70e-12
    Kurtosis:                       2.548   Cond. No.                     3.97e+05
    ==============================================================================
  ```
    ![img](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/YearlyIncome_vs_InterestRate.png?raw=true)
5. prob_lending_club.py
  * Purpose
    * Explore loan data using graphical methods for any additional meaning / understanding
  * Learning Objectives
    * Create histogram using Pandas built-in function
    * Create boxplot using Pandas built-in function
    * Create probability plot using SciPy
  * Output

    ![G1](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/Amount.Funded.By.Investors.png?raw=true)
    ![G2](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/Amount.Requested.png?raw=true)
    ![G1](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/Hist-Amount.Funded.By.Investors.png?raw=true)
    ![G2](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/Hist-Amount.Requested.png?raw=true)
    ![G1](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/QQ-Amount.Funded.By.Investors.png?raw=true)
    ![G2](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/QQ-Amount.Requested.png?raw=true)
6. Time_Series.py / TimeSeries.ipynb
  * Purpose
    * Evaluate loans per month for trends or patterns and understand the effect of stabilizing the dataset
  * Learning Objectives
    * Create ACF and PACF plots using statsmodels
  * Output

    ![LoanData](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/ACF_PACF_Loan_Data.png?raw=true)
    ![DiffLoanData](https://github.com/silkaitis/Thinkful-Unit2/blob/master/images/ACF_PACF_Diff_Loan_Data.png?raw=true)
7. Unit2Proj1.py
  * Purpose
    * Explore descriptive statistics on a simple dataset of alcohol and tobacco in various regions
  * Learning Objectives
    * Print descriptive statistics using Pandas and Scipy
  * Output
  ```
    The mean of the Alcohol dataset is 5.44
    The median of the Alcohol dataset is 5.63
    The mode of the Alcohol dataset is 4.02
    The range of the Alcohol dataset is 2.45
    The variance of the Alcohol dataset is 0.64
    The standard deviation of the Alcohol dataset is 0.80

    The mean of the Tobacco dataset is 3.62
    The median of the Tobacco dataset is 3.53
    The mode of the Tobacco dataset is 2.71
    The range of the Tobacco dataset is 1.85
    The variance of the Tobacco dataset is 0.35
    The standard deviation of the Tobacco dataset is 0.59

    The mean of the Alcohol and Tobacco dataset is 4.53
    The median of the Alcohol and Tobacco dataset is 4.51
    The mode of the Alcohol and Tobacco dataset is 2.71
    The range of the Alcohol and Tobacco dataset is 3.76
    The variance of the Alcohol and Tobacco dataset is 1.34
    The standard deviation of the Alcohol and Tobacco dataset is 1.16
  ```
