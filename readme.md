# Thinkful Unit 2 Exercises

**Purpose**

Explore and learn various tools available in Statsmodels and Scipy

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

      ![Chi-square](https://raw.githubusercontent.com/silkaitis/Thinkful-Unit2/master/Chi_square.png)

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

![scatter_matrix](https://raw.githubusercontent.com/silkaitis/Thinkful-Unit2/master/loan_scatter_matrix.png)

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
![log_func](https://raw.githubusercontent.com/silkaitis/Thinkful-Unit2/master/Logistic_function.png)

![loan_log_regress](https://raw.githubusercontent.com/silkaitis/Thinkful-Unit2/master/Loan_Log_Regression.png)

4. multivariate.py / multivariate.ipynb
  * Purpose
    * Build multivariate model of loan data; IntRate = f(Yearly_Income, Home_Ownership)
  * Flow
    * Load data into DataFrame and clean
    * Create univariate model using statsmodels.formula.api and inspect performance
    * Create multivariate models using statsmodels.formula.api  with increasing complexity and evaluate performance
    * Scatter plot Yearly_Income and Interest.Rate to check conclusions drawn from model performance
5. prob_lending_club.py
  * Purpose
    * Explore loan data using graphical methods for any additional meaning / understanding
  * Flow
    * Load data into DataFrame and clean
    * Create histogram using Pandas built-in function
    * Create boxplot using Pandas built-in function
    * Create probability plot using scipy probability plot
6. prob.py
  * Similar flow as prob_lending_club.py but with simple dataset
7. Time_Series.py / TimeSeries.ipynb
  * Purpose
    * Evaluate loans per month for trends or patterns and understand the effect of stabilizing the dataset
  * Flow
    * Load data into DataFrame, clean and transform
    * Execute ACF and PACF on the original dataset using statsmodels.api.graphics.tsa.plot_acf & .plot_pacf
    * Calculate the delta between data points to stabilize the data
    * Execute ACF and PACF on the original dataset using statsmodels.api.graphics.tsa.plot_acf & .plot_pacf
8. Unit2Proj1.py
  * Purpose
    * Explore descriptive statistics on a simple dataset of alcohol and tobacco in various regions
  * Flow
    * Clean data and load into DataFrame
    * Print descriptive statistics using Pandas and Scipy functionality
