# Links

https://www.statsmodels.org/stable/glm.html
https://www.statsmodels.org/stable/examples/notebooks/generated/glm_formula.html


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
# Using Formula

```
import statsmodels.api as sm
import statsmodels.formula.api as smf
star98 = sm.datasets.star98.load_pandas().data
formula = 'SUCCESS ~ LOWINC + PERASIAN + PERBLACK + PERHISP + PCTCHRT + \
           PCTYRRND + PERMINTE*AVYRSEXP*AVSALK + PERSPENK*PTRATIO*PCTAF'
dta = star98[['NABOVE', 'NBELOW', 'LOWINC', 'PERASIAN', 'PERBLACK', 'PERHISP',
              'PCTCHRT', 'PCTYRRND', 'PERMINTE', 'AVYRSEXP', 'AVSALK',
              'PERSPENK', 'PTRATIO', 'PCTAF']].copy()
endog = dta['NABOVE'] / (dta['NABOVE'] + dta.pop('NBELOW'))
del dta['NABOVE']
dta['SUCCESS'] = endog
```
Then we fit model:

```
mod1 = smf.glm(formula=formula, data=dta, family=sm.families.Binomial()).fit()
print(mod1.summary())
```

```
                Generalized Linear Model Regression Results
==============================================================================
Dep. Variable:                SUCCESS   No. Observations:                  303
Model:                            GLM   Df Residuals:                      282
Model Family:                Binomial   Df Model:                           20
Link Function:                  logit   Scale:                          1.0000
Method:                          IRLS   Log-Likelihood:                -127.33
Date:                Thu, 06 Aug 2020   Deviance:                       8.5477
Time:                        13:05:53   Pearson chi2:                     8.48
No. Iterations:                     4
Covariance Type:            nonrobust
============================================================================================
                               coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------------------
Intercept                    0.4037     25.036      0.016      0.987     -48.665      49.472
LOWINC                      -0.0204      0.010     -1.982      0.048      -0.041      -0.000
PERASIAN                     0.0159      0.017      0.910      0.363      -0.018       0.050
PERBLACK                    -0.0198      0.020     -1.004      0.316      -0.058       0.019
PERHISP                     -0.0096      0.010     -0.951      0.341      -0.029       0.010
PCTCHRT                     -0.0022      0.022     -0.103      0.918      -0.045       0.040
PCTYRRND                    -0.0022      0.006     -0.348      0.728      -0.014       0.010
PERMINTE                     0.1068      0.787      0.136      0.892      -1.436       1.650
AVYRSEXP                    -0.0411      1.176     -0.035      0.972      -2.346       2.264
PERMINTE:AVYRSEXP           -0.0031      0.054     -0.057      0.954      -0.108       0.102
AVSALK                       0.0131      0.295      0.044      0.965      -0.566       0.592
PERMINTE:AVSALK             -0.0019      0.013     -0.145      0.885      -0.028       0.024
AVYRSEXP:AVSALK              0.0008      0.020      0.038      0.970      -0.039       0.041
PERMINTE:AVYRSEXP:AVSALK  5.978e-05      0.001      0.068      0.946      -0.002       0.002
PERSPENK                    -0.3097      4.233     -0.073      0.942      -8.606       7.987
PTRATIO                      0.0096      0.919      0.010      0.992      -1.792       1.811
PERSPENK:PTRATIO             0.0066      0.206      0.032      0.974      -0.397       0.410
PCTAF                       -0.0143      0.474     -0.030      0.976      -0.944       0.916
PERSPENK:PCTAF               0.0105      0.098      0.107      0.915      -0.182       0.203
PTRATIO:PCTAF               -0.0001      0.022     -0.005      0.996      -0.044       0.044
PERSPENK:PTRATIO:PCTAF      -0.0002      0.005     -0.051      0.959      -0.010       0.009
============================================================================================
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

# Comprehensive Link

https://online.stat.psu.edu/stat504/node/216/

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