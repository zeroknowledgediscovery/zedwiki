# [https://www.statsmodels.org/stable/glm.html](https://www.statsmodels.org/stable/glm.html)

# Examples

`# Load modules and data
In [1]: import statsmodels.api as sm

In [2]: data = sm.datasets.scotland.load(as_pandas=False)

In [3]: data.exog = sm.add_constant(data.exog)

# Instantiate a gamma family model with the default link function.
In [4]: gamma_model = sm.GLM(data.endog, data.exog, family=sm.families.Gamma())

In [5]: gamma_results = gamma_model.fit()

In [6]: print(gamma_results.summary())
                 Generalized Linear Model Regression Results                  
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
==============================================================================`