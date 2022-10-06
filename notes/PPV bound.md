
# IPF

IPF has a prevalence of ~ 0.0005. Thus, any screening will 
necessarily have high false positives. Note that:

$$PPV = \frac{s}{s+ (\frac{1}{p}-1)(1-c)} $$

So for prevalence = 0.0005 (5 in 10,000), for 90% sensitivity and 
90% specificity, the PPV is 0.005 or 0.5% For 100% sensitivity, the PPV is still around 0.5%.
To get really high PPV, you need to get ridiculously high specificities. Even for 99% specificity and 
100% sensitivity, the PPV is still around just 5%.

So undertsandly while you really want to know what is the percentage of flagged patients have IPF,
the real question is whether you should send them for detailed evaluation. And that answer is 
given by the positive likelihood ratio, which is independent of prevalence.

$$LR+ = s/c $$