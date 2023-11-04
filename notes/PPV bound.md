# IPF

IPF has a prevalence of ~ 0.0005. Thus, any screening will 
necessarily have high false positives. Note that (s is sensitivity, c is specificity, and p is prevalence)

$$PPV = \frac{s}{s+ (\frac{1}{p}-1)(1-c)} $$

So for prevalence = 0.0005 (5 in 10,000), for 90% sensitivity and 
90% specificity, the PPV is 0.005 or 0.5% For 100% sensitivity, the PPV is still around 0.5%.
To get really high PPV, you need to get ridiculously high specificities. Even for 99% specificity and 
100% sensitivity, the PPV is still around just 5%.

So undertsandly while you really want to know what is the percentage of flagged patients have IPF,
the real question is whether you should send them for detailed evaluation. And that answer is 
given by the positive likelihood ratio, which is independent of prevalence.

$$LR+ = s/(1-c) $$

If a person tests positive, then they having the disease is LR+ times more likely compared to the pre-test odds.
Thus, id prevalence is the pre-test odds, then teh population of patients with a positive test is 
at > 30 times that risk. So perhaps follow up is warranted.

Note the study is NOT making a diagnostic claim. The claim is that it flags patienst who need a pulmonary consult.