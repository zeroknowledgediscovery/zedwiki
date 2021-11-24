# Ustatistic
+ [Use of U statistic](/uploads/mannU.pdf)
+ [Variance of U statistic](/uploads/boundsU.pdf)

# Sample Size Estimate in Diagnostic Trials

 [Sample size estimation in diagnostic test studies of biomedical
informatics](/uploads/powercalculation.pdf)

# Likelihood Ratios

The higher value of positive LR corresponds with greater information of positive test result while the
lower value of negative LR associates with more information of
negative test results. In particular, the positive and negative LR is
of greater interest in comparative studies of two diagnostic tests.

# ROC

For a quantitative diagnostic test or the test results are recorded on
ordinal scale, the sensitivity and specificity varies across the different
thresholds and the sensitivity is inversely related with specificity
[2,4,14]. Then, the plot of sensitivity versus 1-specificity is called receiver operating characteristic (ROC) curve and the area under the curve (AUC), as an effective measure of accuracy has been considered
and it has a meaningful interpretations [15]. This curve plays a central
role in evaluating diagnostic ability of tests to discriminate the true
state of subjects and comparing two alternative diagnostic tasks
when each task is performed on the same subject.

# Power Statement

The required sample sizes were calculated and tabulated with different levels of accuracies and
marginal errors with 95% confidence level for estimating and for various effect sizes with 80% power for
purpose of testing as well.


# Formula
Let \\\( d\\\) be the marginal error, and \\\( \rho\\\) is the prevalence, and \\\(s,c\\\) are sensitivity and specificity respectively, Then, we have:


Sample size based on sensitivity:
$
n_{s} = \frac{z^2_{\alpha/2} s (1-s) }{d^2 \rho}
$

Sample size based on specificity:
$
n_{c} = \frac{z^2_{\alpha/2} c (1-c) }{d^2 (1-\rho)}
$

# Power definition

For the purpose of testing, instead
of third element, the difference of sensitivity (or specificity) under
the null and alternative hypothesis is required (i.e. the maximum
difference to be detected in statistical test with power of \\\(1 - \beta \\\)
where b is the probability of type II error). Thus, the power of sta-
tistical test (the compliment of type II error) should be considered
the prior sample size calculation.

# Power calculation against existing test wrt sensitivity or specificity

At \\\(1-\beta\\\) power, and confidence \\\(\alpha\\\), we have:

$
n =\left ( \frac{z_{\alpha/2}\sqrt{p_0(1-p_0)} + z_{\beta}\sqrt{p_1(1-p_1)}}{p_0-p_1}\right)^2
$

where \\\(p_0,p_1\\\) are the sensitivity or specifity values for old and new tests respectively.


