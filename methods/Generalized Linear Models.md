# Quick Example
```
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
data=pd.read_csv('data.csv') # assume columns ar Y XA XB
formula = 'Y ~ XA + XB + XA*XB'
mod1 = smf.glm(formula=formula, data=data).fit()
#assume gaussian family with identity link ie we assume y is normally distributed, and 
# link(y) = x^T \beta, and the link(.) is identity

print(mod1.summary())
```


# Links

+ https://www.statsmodels.org/stable/glm.html
+ https://www.statsmodels.org/stable/examples/notebooks/generated/glm_formula.html
+ https://www.statsmodels.org/stable/generated/statsmodels.genmod.generalized_linear_model.GLM.html#statsmodels.genmod.generalized_linear_model.GLM
+ https://online.stat.psu.edu/stat504/node/216/


# Examples

## Load modules and data
```
In [1]: import statsmodels.api as sm
In [2]: data = sm.datasets.scotland.load(as_pandas=False)
In [3]: data.exog = sm.add_constant(data.exog)
```
## Instantiate a gamma family model with the default link function.
```
In [4]: gamma_model = sm.GLM(data.endog, data.exog, family=sm.families.Gamma())
In [5]: gamma_results = gamma_model.fit()
In [6]: print(gamma_results.summary())
```
```
==============================================================================
Dep. Variable:                      y   No. Observations:                   32
Model:                            GLM   Df Residuals:                       24
Model Family:                   Gamma   Df Model:                            7
Link Function:          inverse_power   Scale:                       0.0035843
Method:                          IRLS   Log-Likelihood:                -83.017
Date:                Thu, 27 Aug 2020   Deviance:                     0.087389
Time:                        16:04:39   Pearson chi2:                   0.0860
No. Iterations:                     6                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
const         -0.0178      0.011     -1.548      0.122      -0.040       0.005
x1          4.962e-05   1.62e-05      3.060      0.002    1.78e-05    8.14e-05
x2             0.0020      0.001      3.824      0.000       0.001       0.003
x3         -7.181e-05   2.71e-05     -2.648      0.008      -0.000   -1.87e-05
x4             0.0001   4.06e-05      2.757      0.006    3.23e-05       0.000
x5         -1.468e-07   1.24e-07     -1.187      0.235   -3.89e-07    9.56e-08
x6            -0.0005      0.000     -2.159      0.031      -0.001   -4.78e-05
x7         -2.427e-06   7.46e-07     -3.253      0.001   -3.89e-06   -9.65e-07
==============================================================================
```

# Data Transformation

```
def double_it(x):
    return 2 * x
formula = 'SUCCESS ~ double_it(LOWINC) + PERASIAN + PERBLACK + PERHISP + PCTCHRT + \
           PCTYRRND + PERMINTE*AVYRSEXP*AVSALK + PERSPENK*PTRATIO*PCTAF'
mod2 = smf.glm(formula=formula, data=dta, family=sm.families.Binomial()).fit()
print(mod2.summary())
```



### Recall a simple linear regression model

Objective: model the expected value of a continuous variable, Y, as a linear function of the continuous predictor, X, E(Yi) = β0 + β1xi
Model structure: Yi = β0 + β1xi + ei
Model assumptions: Y is is normally distributed, errors are normally distributed, ei ∼ N(0, σ2), and independent, and X is fixed, and constant variance σ2.
Parameter estimates and interpretation: β^0 is estimate of β0 or the intercept, and β^1 is estimate of the slope, etc... Do you recall, what is the interpretation of the intercept and the slope?
Model fit: R 2, residual analysis, F-statistic
Model selection: From a plethora of possible predictors, which variables to include?


## Generalized Linear Models (GLMs)

 First, let’s clear up some potential misunderstandings about terminology.  The term general linear model (GLM) usually refers to conventional linear regression models for a continuous response variable given continuous and/or categorical predictors. It includes multiple linear regression, as well as ANOVA and ANCOVA (with fixed effects only). The form is yi∼N(xiTβ,σ2), where xi contains known covariates and β contains the coefficients to be estimated. These models are fit by least squares and weighted least squares using, for example: SAS Proc GLM or R functions lsfit() (older, uses matrices) and lm() (newer, uses data frames).


### There are three components to any GLM:

+ Random Component – refers to the probability distribution of the response variable (Y); e.g. normal distribution for Y in the linear regression, or binomial distribution for Y in the binary logistic regression.  Also called a noise model or error model.  How is random error added to the prediction that comes out of the link function?
+ Systematic Component - specifies the explanatory variables (X1, X2, ... Xk) in the model, more specifically their linear combination in creating the so called linear predictor; e.g., β0 + β1x1 + β2x2 as we have seen in a linear regression, or as we will see in a logistic regression in this lesson.
+ Link Function, η or g(μ) - specifies the link between random and systematic components. It says how the expected value of the response relates to the linear predictor of explanatory variables; e.g., η = g(E(Yi)) = E(Yi) for linear regression, or  η = logit(π) for logistic regression.

# Comparison of Coefficients

We can compare two regression coefficients from two different regressions by using the standardized regression coefficients, called beta coefficients. To get the beta coefficients, first we have to change both the DV and IV into standardized variables. A variable can be standardized by subtracting the mean of the variable from its values and dividing this difference by the standard deviation of that variable. Such standardized variable also is known as Z-variate. 

The standardized regression (beta) coefficients of different regression can be compared, because the beta coefficients are expressed in units of standard deviations (SDs). The interpretation of the beta coefficient is as follows: if the standardized IV changes by one standard deviation, the standardized DV, on average, changes by beta standard deviation units. Remember, in the usual regression model, we measure the relationship in the original units of DV and IV. But here it is in units of SDs, and that is why we are able to compare the different coefficients.

Now, in case the regression coefficients are already given and we are not able to run standardized regression, it is possible to convert the usual regression coefficient into beta coefficients, by making use of their relationships. The relationship between the usual regression coefficient and the beta coefficient is as follows: beta coefficient = usual regression coefficient multiplied by the sample standard deviation of IV(X) and divide by the sample standard deviation of the DV (Y). This relationship holds true in multiple regression also. 

Look also here https://stats.stackexchange.com/questions/59327/how-to-compare-two-regression-slopes-for-one-predictor-on-two-different-outcomes

## Deviance

https://bookdown.org/egarpor/PM-UC3M/glm-deviance.html