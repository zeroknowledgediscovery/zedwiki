Notation:

+ sensitivity: \\\(s\\\)
+ specificity: \\\(c\\\)
+ PPV: \\\(p\\\)
+ prevalence: \\\( \rho \\\)
+ NPV: \\\( \nu\\\)

# AUC

# PPV

PPV is the fraction of true positives to all positive flags, i.e.,

$
p = \frac{t_p}{t_p+f_p}
$

From sensitivity and specificity, PPV may be calculated as follows:

PPV = (sensitivity x prevalence) / [ (sensitivity x prevalence) + ((1 – specificity) x (1 – prevalence)) ]

$
p = \frac{s \rho}{s \rho + (1-c)(1-\rho)}
$


# NPV
NPV is the fraction of true negatives in all negative flags, i.e.,

$
\nu = \frac{t_n}{t_n+f_n}
$

From sensitivity and specificity, we can calculate:

NPV = (specificity x (1 – prevalence)) / [ (specificity x (1 – prevalence)) + ((1 – sensitivity) x prevalence) ]

$
\nu = \frac{c(1-\rho)}{c(1-\rho) + (1-s)\rho}
$

