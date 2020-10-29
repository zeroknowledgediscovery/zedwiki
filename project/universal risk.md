# Universal Risk

## The Hypothesis


##  Risk Calculation Approach

+ We hypothesize that the seasonal flu epidemic encodes patterns that drive COVID epidemiology and collect countywise infection count data over a period of 9 years from 2003 to 2013 flu season in US
+ We use a novel approach to quantifying similarity between categorical time series samples to identify natural clustering of the counties, according to the sequential count variations
+ Using insight from our previous work (https://elifesciences.org/articles/30756), and this similarity metric,  we determine the cluster of counties whichinclude the set corresponding to epidemic initiation on average over the flu seasons. These are  coastal counties with high population  and the right conjunction of weather, demographic, and socio-economic factors that trigger the seasonal flu epidemic. We hypothesize that the risk of initiation of the yearly flu season also track sthe risk of COVID infections during the current pandemic.
+ Using the infection count variations in these "high initial risk" counties (lets denote this set as  \\\(G_0\\\)  and our prior work on inferring finite state probabilistic automata (PFSA) models of finite valued  stochastic processes (https://royalsocietypublishing.org/doi/full/10.1098/rsta.2011.0543), we infer a generative model \\\(\mathcal{G}_0 \\\) from the set of quantized count variatoions \\\( G_0\\\).
+ Finally we use sequence likelihood divergence to quantify teh deviation of the count variation in each county from this model, thus hgiving us a static measure of universal initiation risk in each county (denote this as \\\(\mathbf{u}_0\\\))
+ We construcnt a General Linear Model (Poisson log-linear regression) to connect this covraiate along with other suspected co-variates to observed and confirmed COVID counts in each US county, thus solving a well-defined GLM problem.

# Results, Observations & Implications

The GLM solution has the following implications, results and observations:
    - **The \\\(\mathbf{u}_0 \times r\\\) is the most imprtant covaraite where \\\( r \\\) is the fraction of the population living in an urban environment (non-rural as defined by US census)  in each county**
    - **The model we find correlates very well with confirmed COVID county**
    - **The model we find is robust, in the sense it is stable to perturbations** 
    - **We can use this model to make predictions on future COVID counts**

### GenESeSS Command used
`
./genESeSS -f 
`


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

## Innovation

## So What

