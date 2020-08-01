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

# Task List

1. generate the alphabeta and the metadata csvs as above
2. Shere  the link with the diffusion simulation u did for the different viruses
3. Dominat strain tracking task (above)
4. We need to do a EPITOPE MATCH task (detailed later)
5. We need to do a IRAT calculation task as well (this will be a seprate paper)

# Epitope Match Task
Let k be the diffusion simulation step.
1. compute the MHCI top epitopes using the application u tried, call this set E_k
2. compute the deviation of E_k from E_0 as follows:
   
   Note these are sets of strings
   Compute   $$average_{x \in E_k} min_{y \in E_0} L(x,y)$$
3. Plot the averge E_k line, averaged over mutiple simulation runs

# IRAT task

1. Show qIRAT for 100 H1N1, 100 H3N2, and sufficient number of recent H5 and H7 sequences (report minimum score over 2010-current, and the current year score)
2. List top 3 for each variety (minimum current year score)
3. as usual report seqName, seqAccession, etc

