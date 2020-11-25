# Kaplan–Meier estimator

The Kaplan–Meier estimator,[1][2] also known as the product limit estimator, is a non-parametric statistic used to estimate the survival function from lifetime data. In medical research, it is often used to measure the fraction of patients living for a certain amount of time after treatment. In other fields, Kaplan–Meier estimators may be used to measure the length of time people remain unemployed after a job loss,[3] the time-to-failure of machine parts, or how long fleshy fruits remain on plants before they are removed by frugivores. The estimator is named after Edward L. Kaplan and Paul Meier, who each submitted similar manuscripts to the Journal of the American Statistical Association. The journal editor, John Tukey, convinced them to combine their work into one paper, which has been cited about 57,000 times since its publication.[4][5]

The estimator of the survival function \\\(S(t)\\\) (the probability that life is longer than \\\(t\\\) is given by:

$$ \widehat{S}(t)= \prod_{i: t_i \leq t} \left ( 1 - \frac{d_i}{n_i}  \right )$$

with \\\( t_{i} \\\) a time when at least one event happened, \\\(d_i\\\)  the number of events (e.g., deaths) that happened at time \\\( t_{i}\\\), and \\\( n_{i}\\\) the individuals known to have survived (have not yet had an event or been censored) up to time \\\( t_{i}\\\).

https://lifelines.readthedocs.io/en/latest/Survival%20analysis%20with%20lifelines.html

```
from lifelines import KaplanMeierFitter
kmf = KaplanMeierFitter()

```
```
T = data["duration"]
E = data["observed"]

kmf.fit(T, event_observed=E)
```
```
from matplotlib import pyplot as plt


kmf.survival_function_.plot()
plt.title('Survival function of political regimes');
```
![](https://lifelines.readthedocs.io/en/latest/_images/lifelines_intro_kmf_curve.png)

```
kmf.plot()

```

![](https://lifelines.readthedocs.io/en/latest/_images/lifelines_intro_kmf_fitter.png)

```
kmf.median_survival_time_
#   4.0
```
```
from lifelines.utils import median_survival_times
median_ci = median_survival_times(kmf.confidence_interval_)
```
We might be interested in estimating the probabilities in between some points. We can do that with the timeline argument. We specify the times we are interested in and are returned a DataFrame with the probabilities of survival at those points:

```
import numpy as np

ax = plt.subplot(111)

t = np.linspace(0, 50, 51)
kmf.fit(T[dem], event_observed=E[dem], timeline=t, label="Democratic Regimes")
ax = kmf.plot(ax=ax)

kmf.fit(T[~dem], event_observed=E[~dem], timeline=t, label="Non-democratic Regimes")
ax = kmf.plot(ax=ax)

plt.title("Lifespans of different global regimes");
```

![](https://lifelines.readthedocs.io/en/latest/_images/lifelines_intro_multi_kmf_fitter_2.png)

