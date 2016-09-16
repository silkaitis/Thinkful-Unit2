Description of the Thinkful exercises completed:

1. chisquare.py
  * Purpose
    * Determine if loan data fits a Chi-squared distribution.
  * Flow
      * Load data into DataFrame
      * Generate histogram of the loan data using matplotlib.pyplot.lib
      * Calculate p-value of the chi-squared test using stats.chisquare
2. linear_regression.py
  * Purpose
    * Build linear regression model of loan data; IntRate = f(FICO.Score, Amount.Requested)
  * Flow
    * Load data into DataFrame and clean
    * Inspect data using matrix of scatter plots
    * Build model using OLS from statsmodels.api
    * Print model p-value and R^2
3. logistic_regression.py / logistic_regression.ipynb
  * Purpose
    * Build logistic regression model of loan data; IntRate = f(FICO.Score, Amount.Requested)
    * Determine if a person with a FICO score of 720 would obtain a loan for $10,000 at 12% interest.
  * Flow
    * Load data into DataFrame and clean
    * Inspect data using matrix of scatter plots
    * Build model using OLS from statsmodels.api
    * Print model p-value and R^2
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
    * 
8. Unit2Proj1.py
