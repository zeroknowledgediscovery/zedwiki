# Universal Risk

## The Hypothesis


##  Risk Calculation Approach

+ We hypothesize that the seasonal flu epidemic encodes patterns that drive COVID epidemiology and collect countywise infection count data over a period of 9 years from 2003 to 2013 flu season in US
+ We use a novel approach to quantifying similarity between categorical time series samples to identify natural clustering of the counties, according to the sequential count variations
+ Using insight from our previous work (https://elifesciences.org/articles/30756), and this similarity metric,  we determine the cluster of counties whichinclude the set corresponding to epidemic initiation on average over the flu seasons. These are  coastal counties with high population  and the right conjunction of weather, demographic, and socio-economic factors that trigger the seasonal flu epidemic. We hypothesize that the risk of initiation of the yearly flu season also track sthe risk of COVID infections during the current pandemic.
+ Using the infection count variations in these "high initial risk" counties (lets denote this set as  \\\(G_0\\\)  and our prior work on inferring finite state probabilistic automata (PFSA) models of finite valued  stochastic processes (https://royalsocietypublishing.org/doi/full/10.1098/rsta.2011.0543), we infer a generative model \\\(\mathcal{G}_0 \\\) from the set of quantized count variatoions \\\( G_0\\\).

 <!--img src="http://34.66.189.202:4567/uploads/mc.png"  width="250"/-->  


+ Finally we use sequence likelihood divergence to quantify teh deviation of the count variation in each county from this model, thus hgiving us a static measure of universal initiation risk in each county (denote this as \\\(\mathbf{u}_0\\\))

 <!--img src="http://34.66.189.202:4567/uploads/urisk.png"  width="250"/-->  


+ We construcnt a General Linear Model (Poisson log-linear regression) to connect this covraiate along with other suspected co-variates to observed and confirmed COVID counts in each US county, thus solving a well-defined GLM problem.

# Results & Implications

<!--img src="http://34.66.189.202:4567/uploads/fig3.png" width="500"/--> 


The GLM solution has the following implications, results and observations:

1. The \\\(\mathbf{u}_0 \times r\\\) is the most imprtant covaraite where \\\( r \\\) is the fraction of the population living in an urban environment (non-rural as defined by US census)  in each county
2. The model we find correlates very well with confirmed COVID cases across US counties
3. The model is robust, in the sense that it is stable to diverse perturbations we experimented with
4. We can use this model to make county-specific forecast of  COVID counts in the near term


## Impact of \\\(\mathbf{u}_0 \times r\\\) Dominance
 
 This shows that learning patterns from the seasonal flu epidemic may be meaningfully transferred to the case of COVID infection, or perhaps any infection that shares similarities in the transmission process. And the information encoded in these patterns is hard to replicate by manually including co-variates; there is always some degree of pattrens that are unmodeled, or cannot be effectively explained by covraiates we can think of; nevertheless it apperas that thgis unmodlled degrress of freedome o fthe underlying driving dynamics shares features between COVID and flu, such that teh risk computed by us enmds up being th emost important co-vraiate with the largest coefficients. Also, teh model we develop correlates very well with catual count data within the modeling period. Other measures of goodness of fit and explainability are also demonstrated, clearly establishing that including this measure of risk does indeed significantly improve county wise count prediction for the COVID-19 pandemic in the USA.
 
## Forecasts: What we Bring To the Table

### State of the Art
https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/forecasts-cases.html
<img src="https://www.cdc.gov/coronavirus/2019-ncov/images/case-updates/National-Forecast-Incident-Cases-2020-10-19.jpg" width="1000"/> 



### GenESeSS Command used
`
./genESeSS -f 
`


# Innovation

# Impact

