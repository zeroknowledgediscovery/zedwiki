# Research Topics: Overview

* [EHR Projects](https://readymag.com/zed/zero/)
* Qnets: Modeling Ultra High Dimensional Dependency Networks
* Cynet: Deep Learning without Neural Networks
* Cognitive Dissonance Modeling
* Sequence to Function Mapping in Biology
* Actionable Forecasting of Urban Crime
* Preempting the next pandemic

---

# Algorithms

---

+ XgenESeSS

## Cynet
### Purpose
The Cynet Package performs analysis on **spatio-temporal data**. It allows us to study **weather events** in the US spanning from 2016-2019 using a dataset containing 4 years of recorded weather events (cold, snow, fog, rain, storm) from over 2000 weather stations. 
 
### Results 
Current average AUC of 0.76 from the 2079 existing models.
 
### Method
 1. Algorithm input is the log of events.
     * An item of event log is the what, where, when of a weather event.
 2. The event log is preprocessed and converted to a time series which contains location and event type.


For example...


     - A time series for location "UofC" and event type “rain” may look like 0 1 0 0 0 1
     - It means no rain at the first time step, rain at the second time step, no rain for the third to fifth time 
       steps, and rain for the last time step.

 3. Cynet generates a directed network for all the time series.
 4. The influence of one time series on another is captured in the edges of the network.


For example...


     - Assume we have time series UofC - “Rain” and O'Hare - “Storm”
     - The edge from O'Hare - “Storm” to UofC - “Rain” is a model showing how storms around O'Hare can be used as           
       predictors for rain around UofC.
     - Let us say that typically in Chicago, wind blows from O'Hare to UofC, then the model will have strong 
       predicting power.
     - We note that the influence may very well be asymmetric.
     - We also infer models for different time lag because some influences may be short-term while others may take 
       some more time to be apparent.

 5. Once the network is generated for all source and target series, it is pruned to remove weak edges.
 6. Each edge serves as a predictor for a weather pattern.
     * Location and time lag are very influential. 
 7. The Cynet package integrates all these predictions by producing scalar coefficients from each data source in order to make a final prediction about the weather at the desired location.
 8. Once the network is pruned and scalar coefficients are established for each link in the network, **Cynet can make predictions**.


## Qnet
### Purpose
To effectively **model the evolutionary properties of viruses** with a novel machine learning algorithm. The **Quasinet (Qnet) framework** can be used to simulate the evolution of virus strains, predict the probability of a pandemic risk, and decide better vaccine components.

### Results
* Using Qnets, we successfully predicted the global Influenza pandemic in 2009.
* This method provided targets for H1N1 influenza that are much more accurate than the recommended targets from the World Health Organization.

### Method
#### Background of Viruses for Computational Biology - 
**Viruses are infectious agents** that latch onto a host, such as a human or animal, in order to replicate. A virus usually has multiple strains, or variations of that virus that performs similar functions. Each strain consists of proteins which originate from a specific sequence of amino acids. These amino acids can be thought of as specific letters, and the entire sequence can be thought of as a sentence. However, a strain can mutate (lose, gain, or exchange amino acids), and these mutations can be significant; changing enough amino acids may change the properties of the strain.

#### Qnet Framework  
* **Learns structural dependencies** of symbols within sequences
* The Qnet is composed of many **conditional inference trees**
* Each tree corresponds to a **specific location** in a sequence
* Once the trees are trained, each tree uses all locations within the sequence to **predict the probabilities** of certain occurrences at other locations based on the corresponding index

#### Qnets and Virological Understanding 
* In the case of a virus, the **Qnet learns the structural dependencies between amino acids**. The conditional inference decision trees use all the amino acids within a given sequence to **predict the probability** of an amino acid occurrence at its corresponding index.
* Within a Qnet a distance measure can be defined, called the Qdistance. **The Qdistance describes how close one sequence is to another**. Given a virus, we can measure the Qdistance between every pair of strains, and then construct phylogenetic trees and **understand the evolutionary trajectory** of the virus using these Qdistances. 
* The trained Qnet model can also **simulate the evolution of a strain until convergence** by using the Qnet induced probabilities to decide which amino acids we want to mutate. We use this simulation process to **predict risk of a pandemic**, and we say such a risk exists if two following conditions are met. 
 1. After simulating the evolution of a strain with a non-human host, we find that the strain moves closer to the closest strain with a human host. 
 2. After performing another simulation, we find that the same strain fails to mutate towards the most common human strain.

* The Qnet framework can be used to **choose vaccine targets** for each year. Our choice for the target sequence comes from the common strain (as computed by the Qdistance) of a population from previous years. 

#### Qnets and Coronavirus
When applied to the **coronavirus**, we find that the phylogenetic trees constructed from the Qdistance provides a better representation of the evolutionary process than existing methods.




# Public Tools