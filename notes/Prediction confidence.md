# Estimating confidence on prediction

+ When we are computing a risk score such as in ZCoR, we need to estimate what is the confidence of any decision that we make, at teh level of individual patients.
+ We need to also address the problem of claibration. Note that this problem shows up because computing a ROC curve does not tell us actually about the decision thershold that we may want to use in implementation, it only says that there exists one or more good ones. And when we apply our classifier to a new dat aset (say a new patient source), then these thresholds might change, and ideally we may need to generate a ROC curve that is applicable to this new patient source. This will affect how we actually flag individual patients, or in other words, the estimated probability that a ptient is in the case cohort given a computed risk score.


# Probability of positive class

From definition of PPV as the fraction of true positive flags in all raised flags, we conclude that the probability of a ptient being in the case cohort can be estimated as:
$$ p(r) = \min_{u\geqq r} PPV(u)   $$
where \(PPV(u)\) is PPV represented as a function of the threshold u, and \(r\) is the risk score of this patient.Note that we can compute PPV as:
$$PPV = \frac{s}{s+ (\frac{1}{p}-1)(1-c)} $$
which can be also stated as:
$$PPV = \frac{LR+}{LR^+ + (\frac{1}{p}-1)} $$
which for very small prevelence approximates to:
$$ \rho LR^+(r)$$


