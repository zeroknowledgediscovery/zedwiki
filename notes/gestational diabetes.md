# Figure Stack

[Latest Figures](http://34.66.189.202:4567/uploads/figs.pdf)


# New To Do

## 1.Distribution of GD diagnosis time
## GD diagnosis time vs birth time
## GD diagnosis with other pregnancy complications

You can probably produce a single dataframe to have all this info.
Having a bunch of patients with diagnosis time, birth time, and  other 
complications (maybe flags for certain complications) would suffice


## 2. Indicative Diseases With obvious codes

Need to put this as supplementary. So dont rewrite what there is now

## 3. Perturbation Analysis

Increase of raw risk with one extra endocrine code, and one extra infection,
asa function of time (in the training period)


# To Do

## ![ID](https://img.shields.io/badge/1--blue) Update results with BEST Auc 

Please stop hobbling the results. We need to put our best (but correct) foot forward

<<Warn("Careful, Do not change file formats or headers")>>


## ![ID](https://img.shields.io/badge/2--blue) Generate Precision-Recal Curves 

The following snippets are helpful. 

<<Note(Note that *RHO* is the prevalence 
which we should look up from literarure.)>>

Please generate PRC for each time points that you ahev used in the rest of the 
analysis

```
def selROC(df,fpr=.1,tpr=None,th=None,eps=0.01,p=0.017,ppv=False):
    row=df[df.fpr.between(fpr-eps,fpr+eps)].max()
    if ppv:
        ppv=row.tpr/(row.tpr+row.fpr*((1./p - 1)))
        return row,ppv
    else:
        return row.tpr
def getPPV(row,RHO):
    return row.tpr/(row.tpr + row.fpr*(1./RHO -1))
```

## ![ID](https://img.shields.io/badge/3--blue) Short labels for feature names 

Please write short, undertstandable labels for fetaure names, that we can use in the ylabels of
Fig. 1C. You can also have slightly longer description of what things like *mean position* etc. means that we can add to teh figure caption, and which makes sense when someone reads the caption only.

## ![ID](https://img.shields.io/badge/4--blue) Confidence Bounds for AUC

Please draw samples from the population, compute AUCs for the different time points, and 
compute upper and lower confidence bounds using the formula:
$$\hat{y} = y \pm \frac{2.63\sigma}{\sqrt{n}} $$

The header of the resultant csv file is the following:
```
lb,v,ub,time,gender,dataset
```
where *dataset* currently is just `TRUVEN`, and *time* here is one of  0,-1,-2,-4

## ![ID](https://img.shields.io/badge/5--blue) Generate Publisher Files for Postpartem

