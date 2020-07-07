# Deep Learning without NN


<img alt='nn comparison' src="uploads/structcomp.png" width="700px">

[https://pypi.org/project/cynet/](https://pypi.org/project/cynet/)

![https://img.shields.io/pypi/dm/cynet.svg](https://img.shields.io/pypi/dm/cynet.svg)
![https://img.shields.io/pypi/v/cynet.svg](https://img.shields.io/pypi/v/cynet.svg)

We develop a framework for modeling the coupled evolution of  discrete time stochastic processes, with the aim of predicting rare events.  A rare event in our setting is defined to have an occurrence frequency < 2%; thus extreme weather in US as measured by the network of weather stations,  seismic events in locations around the tectonic plate boundaries around the world, and violent urban crime in major US cities, all fall in this category. 

# Fraction-nets & Self-similar Compression

<img alt='fraction Net' src='uploads/fnet.png' width="600px" >

We begin by noting that in our approach, we employ **no neurons, no fixed activation functions,  no user-specified loss functions, and no global optimization via back-propagation**. Instead an assembly of local models inferred via **self-similar compression (SSC)** is distilled from data. Deviations from target behavior is measured via an **universal notion of divergence**, thus eliminating the need for user-specified loss functions. 

# Result Montage

<img alt='fraction Net' src='uploads/results.png' width="800px" >

# To Do
##  Extended Data
```diff
- Fix extended data figure 5. Currently, we are starting the caption with "panel f".
- Move the pfsas to left, and plots to right
- THE FIGURE MUST READ FROM LEFT TO RIGHT, not jump randomly between panels
```

## Fast Example Notebook
```diff
- gpu implementation for rapid split file generation
```
## Results Montage
```diff
- ROC plots NN/fracnet 
- colorbar horizontal for column 1
- Note outperformance measure over NN
- TIME: June 26
```

## Parsimony
```diff
- Show plot of number of parameters with performance. 
- This should produce a single scatter plot with colors indicating different applications and NN/fractionnet
- June 29
```

## Depth
```diff
- Need to show depth realization with Link state multiplicity
- Show plot on spatial and temporal depth: we have influence over space and time, Figure 1 might be sufficient to argue temporal depth. Still need to show spatial depth (SHAP analysis?)
```

## Multi-scale
```diff
+ With no vanishing gradient 
+ **Done** in Figure 1 above for syntheic data 
- Need to do the same for the physical examples

```
## Partial updates
```diff
- Need to evaluate which ones we need to update by looking at `llk` degradation
- show we can maintain performance without full recompute
- July 1
```
## Rigorous performance bounds
```diff
+ **Done** in theory development, see below in Fig 4
```
<img alt='nn comparison' src="uploads/theoryscheme.png" width="700px">



