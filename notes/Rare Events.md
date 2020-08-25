# Power Law Recovery

## Omori's law 
The frequency of aftershocks decreases roughly with the reciprocal of time after the main shock. This empirical relation was first described by Fusakichi Omori in 1894 and is known as Omori's law.[1] It is expressed as
$$ n(t)=\frac{k}{(c+t)}$$
where k and c are constants, which vary between earthquake sequences. A modified version of Omori's law, now commonly used, was proposed by Utsu in 1961.[2][3] $$ n(t)=\frac {k}{(c+t)^{a}}$$
where a is a third constant which modifies the decay rate and typically falls in the range 0.7–1.5.


## Relating Omori-Utsu Law to \\\(\gamma\\\)

Let \\\(p(\Delta)\\\) be the probability of the rare event of interest at time-shift \\\(\Delta\\\). Then considering \\\(N\\\) spatial tiles, the average event frequency may be estimated as \\\(p N \\\). Expecting this to follow the OU Law would require:
$$ p \sim \frac{k/N}{(c+\Delta)^a} $$

First, recovering event probability \\\(p\\\) approximately from the observed \\\(\gamma\\\):

$$ \gamma \sim 1 - \frac{h(p)}{h_0}$$
where \\\(h\\\) is th ebinary entropy function, and \\\(h_0\\\) is the binary entropy of the average event frequency. Thus:
$$ p \sim h^{-1}((1-\gamma)h_0)) $$
Inverting the binary entropy in \\\([0,0.5]\\\) is problematic. We use the approximation:
$$ h^{-1}(x) \sim \frac{x}{log_2(1/x)} $$
Finally, we must solve the curve fitting problem:

$$
p(\Delta) = \frac{d_0}{(d_1 + \Delta)^{d_2}}
$$

---
*Notes Follow*
---
# decay interpretation

## Can we relate the decay behavior to omori-utsu law?

## Can we show that simialr law exists for weather?

## can we show generalization for social systems

## How do we relate \\\( \gamma \\\) to after shock frequency with time



In statistics, a record $$x_i , i \in \{ 1 , 2 , \cdots , N \}$$ is called a rare event if its value is above (or below) a given threshold $q$. Altering this threshold alters th enumber and dependencies of events. A large number of factors nonlinearly interact with each other, leading to rare events being erratic, unstable, or chaotic.

```
@article{zhao2016universal,
  title={Universal and non-universal properties of recurrence intervals of rare events},
  author={Zhao, Xiaojun and Shang, Pengjian and Lin, Aijing},
  journal={Physica A: Statistical Mechanics and its Applications},
  volume={448},
  pages={132--143},
  year={2016},
  publisher={Elsevier}
}
```
Nowadays, some recent studies involving areas of geography [26,27], hydrology [28,29], climate [30,31], and finance [32]
indicate that rare events do not appear randomly. Records in many systems were found to show long-range persistence
[33–35]. Consequently, the clustering of rare events (also the clustering of non-rare events) make that the probabilities of
having recurrence intervals well below τ¯ and well above τ¯ are strongly enhanced in the correlated records, where τ¯ is closely related with the threshold q [36]. Furthermore, it was revealed that the distribution of recurrence intervals for long-range persistent records by the Fourier-filtering method generally followed a stretched exponential function [30],

```
%26
@article{telesca2004detrended,
  title={Detrended fluctuation analysis of the spatial variability of the temporal distribution of Southern California seismicity},
  author={Telesca, Luciano and Cuomo, Vincenzo and Lapenna, Vincenzo and Macchiato, Maria},
  journal={Chaos, Solitons \& Fractals},
  volume={21},
  number={2},
  pages={335--342},
  year={2004},
  publisher={Elsevier}
}
%27
@article{yakovlev2006simulation,
  title={Simulation-based distributions of earthquake recurrence times on the San Andreas fault system},
  author={Yakovlev, Gleb and Turcotte, Donald L and Rundle, John B and Rundle, Paul B},
  journal={Bulletin of the Seismological Society of America},
  volume={96},
  number={6},
  pages={1995--2007},
  year={2006},
  publisher={Seismological Society of America}
}
%28
@article{ouarda2001regional,
  title={Regional flood frequency estimation with canonical correlation analysis},
  author={Ouarda, Taha BMJ and Girard, Claude and Cavadias, George S and Bob{\'e}e, Bernard},
  journal={Journal of Hydrology},
  volume={254},
  number={1-4},
  pages={157--173},
  year={2001},
  publisher={Elsevier}
}
%29
@article{kantelhardt2006long,
  title={Long-term persistence and multifractality of precipitation and river runoff records},
  author={Kantelhardt, Jan W and Koscielny-Bunde, Eva and Rybski, Diego and Braun, Peter and Bunde, Armin and Havlin, Shlomo},
  journal={Journal of Geophysical Research: Atmospheres},
  volume={111},
  number={D1},
  year={2006},
  publisher={Wiley Online Library}
}
%30
@article{lennartz2008long,
  title={Long-term memory in earthquakes and the distribution of interoccurrence times},
  author={Lennartz, S and Livina, VN and Bunde, A and Havlin, S},
  journal={EPL (Europhysics Letters)},
  volume={81},
  number={6},
  pages={69001},
  year={2008},
  publisher={IOP Publishing}
}
%31
@article{bodai2012annual,
  title={Annual variability in a conceptual climate model: Snapshot attractors, hysteresis in extreme events, and climate sensitivity},
  author={B{\'o}dai, Tam{\'a}s and T{\'e}l, Tam{\'a}s},
  journal={Chaos: An Interdisciplinary Journal of Nonlinear Science},
  volume={22},
  number={2},
  pages={023110},
  year={2012},
  publisher={American Institute of Physics}
}
%32
@article{siokis2013multifractal,
  title={Multifractal analysis of stock exchange crashes},
  author={Siokis, Fotios M},
  journal={Physica A: Statistical Mechanics and its Applications},
  volume={392},
  number={5},
  pages={1164--1171},
  year={2013},
  publisher={Elsevier}
}

```

$$    \gamma^{s}_{r, \Delta} = 1 - \frac{\textrm{uncertainty of the next output in $x_r$ given  observation of  $x_s$}}{\textrm{unconditional uncertainty of the next output in $x_r$}}
$$

For simple single varaible  systems, e.g., with just  \\\(x(t)\\\) , the \\\( \gamma \\\) is simialr to auto-correlation. However, it generalizes to situations with arbitrary number fo varaibles and where the dependence structure has a non-trivial and unknown state structure. Under such generalizations, theliterature tries to use ARIMA or FARIMA models, which are plagued by a host of different prior assumptions. The problem is the inference of states is in explicably linked to computing any dependency measures like \\\( \gamma \\\).


## Modelling heavy-tailed time series

### Standard time series models

Classical time series analysis has been concerned mostly with linear processes:
$$ X_t = \sum_{j=-\infty}^{\infty} \psi_jZ_{t-j}, t \in \mathbb{Z} $$

where \\\( \psi_j \\\)  is an appropriate sequence of real coefficients and \\\( Z_t\\\)  is a innovations
sequence. The sequence \\\( Z_t \\\) is classically assumed to be white noise (i.e. stationary, uncorrelated and mean-zero); in most applications \\\( Z_t \\\) is even supposed
to be i.i.d. The model ( includes stationary ARMA and FARIMA processes
which are the time series models used most frequently in applications in engineering, physics, chemistry, meteorology, hydrology, etc. ARMA processes and, more
generally, linear processes with finite variance are exible to model any kind of
autocorrelation structure of a stationary sequence.  These are some reasons for
the success story of linear processes whose theory and applications are described
in Brockwell and Davis [12, 13]. As a matter of fact, the estimation of the parameters of an ARMA or FARIMA
process is closely related to the estimation of their covariances and correlations,
and so is the prediction of future values in a time series based on its past and
present values. 

+ Do LSTMS do better than ARMA models?
+ DO LSTM models do better in specific situations?



---


# [PNAS REF](http://34.66.189.202:4567/uploads/pnasrare.pdf)



Rare or extreme events are events that occur with low frequency, and often refers to infrequent events that have widespread impact and which might destabilize systems (for example, stock markets,[1] ocean wave intensity[2] or optical fibers [3] or society[4]). Rare events encompass natural phenomena (major earthquakes, tsunamis, hurricanes, floods, asteroid impacts, solar flares, etc.), anthropogenic hazards (warfare and related forms of violent conflict, acts of terrorism, industrial accidents, financial and commodity market crashes, etc.), as well as phenomena for which natural and anthropogenic factors interact in complex ways (epidemic disease spread, global warming-related changes in climate and weather, etc.).

---

 Consider the following events: a pressure tank within a rocket propulsion system fails  during a launch; tectonic plates shift, causing the first significant earthquake in a lo cale for several decades; a stock market experiences a crash after a prolonged run-up  in price levels. The commonality here is that all of these events are ultimately charac terized by a "rupture" in the underlying system, following a buildup of "pressure"
 over a period of time. The recognition of certain engineering and geologic events as  analogous in this way to financial market crashes was the impetus for the interesting  and enjoyable new book *Why Stock Markets Crash: Critical Events in Complex Financial
 Systems*, by Didier Sornette.
 
  The major thesis of this book is that a stock market crash is not the result of short-term  exogenous events, but rather involves a long-term endogenous buildup, with exoge nous events acting merely as triggers. In particular, Sornette examines financial crashes  within the framework of the "spontaneous emergence of extreme events in self- organizing systems," noting that "extreme events are characteristic of many... 'complex systems."' The author employs mathematical tools-specifically, log-periodic  power laws-to study the prebubble or precrash buildup in a financial system to its  critical point.
 
 ---
 
 [Why Markets Crash?](http://34.66.189.202:4567/uploads/whyMarketsCrash.pdf)
 
 
 It turns out that most complex systems around us do exhibit rare and sudden transitions, that occur over time
intervals that are short compared with the characteristic time scales of their posterior evolution. Such extreme events
express more than anything else the underlying “forces” usually hidden by almost perfect balance, and thus provide
the potential for a better scientific understanding of complex systems. These crises have fundamental societal
impacts and range from large natural catastrophes, catastrophic events of environmental degradation, to the failure
of engineering structures, crashes in the stock market, social unrest leading to large-scale strikes and upheaval,
economic drawdowns on national and global scales, regional power blackouts, traffic gridlock, diseases and epidemics,
etc. **It is essential to realize that the long-term behaviour of these complex systems is often controlled in large part by these rare catastrophic events:** the universe was probably born during an extreme explosion  (the  “big-bang”);  the nucleosynthesis of most important atomic elements constituting our matter results from the colossal explosion of
supernovae; the largest earthquake in California repeating about once every two centuries accounts for a significant
fraction of the total tectonic deformation; landscapes are more shaped by the “millennium” flood that moves large
boulders rather than the action of all other eroding agents; the largest volcanic eruptions lead to major topographic
changes as well as severe climatic disruptions; evolution is characterized by phases of quasi-stasis interrupted by
episodic bursts of activity and destruction;  financial crashes can destroy in an instant trillions of dollars;
political crises and revolutions shape the long-term geopolitical landscape; even our personal life is shaped on the long
run by a few key decisions and happenings.



 [Network Dimension](http://34.66.189.202:4567/uploads/nature03248.pdf)
 
 [Fractal Slide](http://34.66.189.202:4567/uploads/FractalSlides.pdf)
 
 [http://nora.nerc.ac.uk/id/eprint/501966/1/grl50103.pdf](http://nora.nerc.ac.uk/id/eprint/501966/1/grl50103.pdf)


# Refs

```
@article{goodwin2010limits,
  title={The limits of forecasting methods in anticipating rare events},
  author={Goodwin, Paul and Wright, George},
  journal={Technological forecasting and social change},
  volume={77},
  number={3},
  pages={355--368},
  year={2010},
  publisher={Elsevier}
}
```

```
@article{watkins2013bunched,
  title={Bunched black (and grouped grey) swans: Dissipative and non-dissipative models of correlated extreme fluctuations in complex geosystems},
  author={Watkins, Nicholas W},
  journal={Geophysical research letters},
  volume={40},
  number={2},
  pages={402--410},
  year={2013},
  publisher={Wiley Online Library}
}
```

# Datasets

+ [https://ucdp.uu.se/downloads/index.html#ged_global](https://ucdp.uu.se/downloads/index.html#ged_global)
+ [https://guides.ucf.edu/war/wardata#s-lg-box-wrapper-1778686](https://guides.ucf.edu/war/wardata#s-lg-box-wrapper-1778686)
 