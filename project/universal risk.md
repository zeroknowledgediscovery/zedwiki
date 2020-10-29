# Geome of Flu-like Transmission 
The spread of infection from a transmissible virus is a complex spatio-temporal process impacted by the specific transmission mechanism of the virus, the survivability of the virus outside the host under varying enviromental factors such as tempretaure and humidity, population density of viable hosts, and possibly the level of enforcement of social distancing policies.
While the key factors that drive such thsi complex  process for infleunza and COVID-19 are broadly understood, making precise actionable forecasts is still a diffcult modeling problem. Faced with the challenge of forecasting the case count in the context of the  COVID-19 pandemic, a diversity of modeling approaches have been suggested. However a single "best" model is yet to emerge. In this study we introduce the concept of a organism-invariant geo-spatial risk measure, **referred to as the geome**, for flu-like transmissions,  and demosntrate that this risk significantly improves current forecasts. 

## The Hypothesis
We hypothesize that the seasonal flu epidemic encodes complex geo-spatial stochastic incidence patterns that are common to, and drive,  COVID epidemiology. Using a novel approach to quantifying similarity of stochastic sample paths, we learn from nearly a decade of historical flu seasonal epidemics, and effectively incorporate these patterns to model and forecast COVID case counts. Our approach demonstrates that broad commonalities in transmission dynamics may be effectively leveraged for forcasting the number of new cases, even if the specific pathogen of interest is biologically distinct from the one whose historical incidence patterns are actually available. In the context of influenza and SARS-CoV2 viral transmission modeling, the geome corresponding to influenza is useful for predicting COVID-19 cases, since the tranbsmission dynamics is believed to be largely similar.

##  Risk Calculation Approach

+ We collect countywise infection count data over a period of 9 years from 2003 to 2013 flu season in US
+ We use a novel approach to quantifying similarity between categorical time series samples to identify natural clustering of the counties, according to the sequential count variations
+ Using insight from our previous work (https://elifesciences.org/articles/30756), and this similarity metric,  we identify the emergent cluster of counties which includes the set corresponding to estimated epidemic initiation over the flu seasons. These are  coastal counties with high population  and the right conjunction of weather, demographic, and socio-economic factors that trigger the seasonal flu epidemic. We hypothesize that the risk of initiation of the yearly flu season also track the risk of COVID-19 infections.
+ Using the infection count variations in these "high initial risk" counties (lets denote this set as  \\\(G_0\\\)  and our prior work on inferring finite state probabilistic automata (PFSA) models of finite valued  stochastic processes (https://royalsocietypublishing.org/doi/full/10.1098/rsta.2011.0543), we infer a generative model \\\(\mathcal{G}_0 \\\) from the set of quantized count variatoions \\\( G_0\\\).

 <!--img src="http://34.66.189.202:4567/uploads/mc.png"  width="250"/-->  


+ Finally we use sequence likelihood divergence to quantify the deviation of the count variation in each county from this model, to formulate a time-independent spatially varying measure of universal initiation risk (\\\(\mathbf{u}_0\\\)), which we call the geome.

 <!--img src="http://34.66.189.202:4567/uploads/urisk.png"  width="250"/-->  


+ We construcnt a General Linear Model (Poisson log-linear regression) to connect this covariate along with other suspected covariates to bi-weekly COVID-19 case counts.

# Results & Implications

<!--img src="http://34.66.189.202:4567/uploads/fig3.png" width="500"/--> 


The GLM solution has the following implications, results and observations:

1. The \\\(\mathbf{u}_0 \times r\\\) is the most imprtant covaraite where \\\( r \\\) is the fraction of the population living in an urban environment (non-rural as defined by US census)  in each county
2. The model we find correlates very well with confirmed COVID cases across US counties
3. The model is robust, in the sense that it is stable to diverse perturbations we experimented with
4. We can use this model to make county-specific forecast of  COVID counts in the near term


## Impact of \\\(\mathbf{u}_0 \times r\\\) Dominance
 
 This shows that learning patterns from the seasonal flu epidemic may be meaningfully transferred to the COVID-19 epidemiology, or perhaps any virus with a  similar transmission mechanism. And the information encoded in these patterns is hard to replicate by manually including new covariates in the model; there are  always some factors that are unmodeled, or observed patterns not effectively explained by covriates we  can a priori imagine to have an impact in the transmission dynamics. Instead of attempting to identify all of such factors along their potentially complex dependencies, our approach treats the past sequential observations as providing the set of similarities or patterns that we expect to drive future infections. Our key assumption here is that these potentially unmodelled degrees of freedom in the underlying driving dynamics are similar for COVID-19 and flu. This insight is vindicated by our result that this universal risk scaled by the fraction of county-specific  urban population, indeed emerges as the most important co-vraiate in our models. Also, outputs from the model we develop correlates very well with actual count data within the same modeling period, as well as in the immediate future. Other measures of goodness of fit and explainability are also demonstrated, clearly establishing that including this measure of risk does indeed significantly improve county wise count prediction for the COVID-19 pandemic in the USA.
 
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

