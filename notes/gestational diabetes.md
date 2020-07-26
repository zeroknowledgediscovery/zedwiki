# To Do

## Generate Precision-Recal Curves 

The following snippets are helpful. Note that *RHO* is the prevalence,
which we should look up from paper.

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

## Short labels for feature names 

Please write short, undertstandable labels for fetaure names, that we can use in the ylabels of
Fig. 1C. You can also have slightly longer description of what things like *mean position* etc. means that we can add to teh figure caption, and which makes sense when someone reads the caption only.

## Confidence Bounds for AUC

Please draw samples from the population, compute AUCs for the different time points, and 
compute upper and lower confidence bounds using the formula:
$$\hat{y} = y \pm \frac{2.63\sigma}{\sqrt{n}} $$