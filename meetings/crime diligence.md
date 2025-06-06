# Links

+ [paper](/uploads/s41562-022-01372-0 (2).pdf) in Nature Human Behavior
+ FractalNet Theory [Paper ]( /uploads/v1_covered.pdf)
+ slides https://slides.com/ishanuchattopadhyay/fnet?token=0L45fQ-T (Round 1)
+ slides Round 2 https://slides.com/ishanuchattopadhyay/fractalnetalgo2?token=X8h7x4It

# Round 2 questions
1) Following up on the encouraging results shown or mentioned for the ten cities where the algorithm has been run.  We want to examine/discuss the results in greater detail.

- Review what the example confusion matrix summaries mean.  Is that for an average AUC tile?  An average of tiles? Is there a range of confusion matrices?
    - review calculation
- Why were the horizons different for Boston, Philadelphia, and Chicago?  What drives the horizon selected? Is it always the same for violent crimes and property crimes?
    - we can compute easily for different horizons
- What was the threshold selected for each city (i.e., what was the cutoff for predicting a crime event)? Is it different for violent crimes vs. property crimes?
    - show how threshold is caculated
- In 2024, you re-ran a pilot for Philadelphia?  What was the pilot, and how did the results compare to prior analysis?
For each of the ten cities, is there a summary of the datasets (Training period, training events, Assessment period, Assessment events), range of AUCs, range of confusion matrix results, thresholds used, etc?  (plus any other assumptions or outcome data that is appropriate).  
    - compare results

2) Discuss the impact interventions will have on performance and how often and to what degree (full or partial) retraining is envisioned. Also, discuss if we are successful in reducing crime. Where does the reduction start to materially impact the model performance?

3) What algorithms have the Fractal Net algorithm been compared to? What algorithms were tested during the 2017 Crime Prediction Competition?

    - NIJ papers

4) Discuss the potential of diffuser architectures to transformer & attention models (developed post-2018) to address the problem.

    - transformer and attention architecturers
