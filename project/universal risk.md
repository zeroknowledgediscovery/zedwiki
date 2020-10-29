# Universal Risk

##  Risk Calculation Approach
 <div style="width: 120%; overflow: hidden;">
 <div style="width: 250px; float: left;"> 
 <p> Fig 1. Initial Clustering and Risk Calculation</p>
 <img src="http://34.66.189.202:4567/uploads/urisk.png"  width="250"/>  
 <img src="http://34.66.189.202:4567/uploads/mc.png"  width="180"/>  
 </div>
    <div style="width: 500px; margin-left: 250px;">
     <p> Fig 2. Results of Model Coefficients, Fit & Forecast</p>
    <img src="http://34.66.189.202:4567/uploads/fig3.png" width="500"/> 
    </div>
</div>

+ We hypothesize that the seasonal flu epidemic encodes patterns that drive COVID epidemiology
+ We collect countywise infection count data over a period of 9 years from 2003 to 2013 flu season in US
+ We use a novel approach to quantifying simialrity between categorical time series samples to identify natural clustering of the counties
+ Using insight from our previous work we determine the cluster which correspond to epidemic initiation on average. This is teh cluster which included coastal high population  counties, and have the right conjunction of factors that trigger the seasonal epidemic
+ Using the infection count variations in these "high initial risk" counties (lets denote this set as the Ground Zero Set \\\(G_0\\\) )
+ Using our prior work on inferreing finite state probabilistic automata (PFSA) models of a class of stochastic processes, we infer a model \\\(\mathcal{G}_0 \\\) from the set of quantized count variatoions \\\( G_0\\\).
+ Finally we use sequence likelihood divergence to quantify teh deviation of the count variation in each county from this model, thus hgiving us a static measure of universal initiation risk in each county (denote this as \\\(\mathbf{u}_0\\\))
+ We construcnt a General Linear Model (Poisson log-linear regression) to connect this covraiate along with other suspected co-variates to observed and confirmed COVID counts in each US county, thus solving a well-defined GLM problem.
+ The GLM solution has the following implications, results and observations:
    - **The \\\(\mathbf{u}_0 \times r\\\) is the most imprtant covaraite where \\\( r \\\) is the fraction of the population living in an urban environment (non-rural as defined by US census)  in each county**
    - **The model we find correlates very well with confirmed COVID county**
    - **The model we find is robust, in the sense it is stable to perturbations** 
    - **We can use this model to make predictions on future COVID counts**


## Innovation

## So What

