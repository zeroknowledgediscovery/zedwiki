# Expanding Prediction To Multiple Viruses

We will attempt to replicate dominant strain prediction to two more viruses:

+ HIV1-A
    - This will attempt to predict dominant strain within individual patients
+ CCHFV
    - This is attmpt to predict dominant strain oiver time, say for 5 years

The key ponts here are: 1) is there enough data available to carry out this modeling?
And 2) should we consider geographic stratification

Lets start with CCHF. We do the following steps:

+ Download all CCHFV sequences between collection years 2010 and 2020
+ breakdown by 2 year periods
+ check which *segements* are most common (there is S, M, and L segements in the virus)
+ Try making Qnets with this 2 year data (after aliognment, and segment choice)
+ Carry out dominant strain pred and validation (check how well we do from the actual dominant strain prediction)

Currently looking at HIV patient specific data availability



