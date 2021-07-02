## MODELTEST

```
@article{posada1998modeltest,
  title={Modeltest: testing the model of DNA substitution.},
  author={Posada, David and Crandall, Keith A.},
  journal={Bioinformatics (Oxford, England)},
  volume={14},
  number={9},
  pages={817--818},
  year={1998}
}

@article{huelsenbeck1997phylogeny,
  title={Phylogeny estimation and hypothesis testing using maximum likelihood},
  author={Huelsenbeck, John P and Crandall, Keith A},
  journal={Annual Review of Ecology and systematics},
  volume={28},
  number={1},
  pages={437--466},
  year={1997},
  publisher={Annual Reviews 4139 El Camino Way, PO Box 10139, Palo Alto, CA 94303-0139, USA}
}
```

The program MODELTEST uses log likelihood scores to establish the model of DNA evolution that
best fits the data.

All phylogenetic methods make assumptions, whether explicit or implicit, about the process of DNA substitution (Felsenstein, 1988). For example, an assumption common to many phylogenetic methods is a **bifurcating tree** to describe the phylogeny of species (Huelsenbeck and Crandall, 1997)~\cite{huelsenbeck1997phylogeny}. 

Consequently, all the methods of phylogenetic inference depend on their underlying models. To have confidence in inferences it is necessary to have confidence in the models (Goldman, 1993). Because of this, all the methods based on
explicit models of evolution should explore which is the model that fits the data best, justifying then its use. In traditional statistical theory, a widely accepted statistic for testing the goodness of fit of models is the likelihood ratio test statistic \\\( \delta = 2 log \Lambda \\\) where:

$$ \Lambda = \frac{\max L_0 (null \ model \vert Data)}{\max L_1 (alternate \  model \vert Data)} $$

where \\\(L_0\\\) is the likelihood under the null hypothesis (simple
model) and \\\(L_1\\\) is the likelihood under the alternative hypoth-
esis (more complex, parameter rich, model). When the models compared are nested (the null hypothesis is a special
case of the alternative hypothesis), and the null hypothesis is
correct, the \\\(\delta\\\)  statistic is asymptotically distributed as \\\(\chi^2\\\) with
\\\(q\\\) degrees of freedom, where q is the difference in number of
free parameters between the two models; equivalently, q is
the number of restrictions on the parameters of the alternative
hypothesis required to derive the particular case of the null
hypothesis (Kendall and Stuart, 1979). To preserve the nesting of the models, the likelihood scores are estimated using
the same tree, and then, once the models have been compared, a final tree is estimated using the chosen model of
evolution. When the models are not nested, an alternative
means of generating the null distribution of the \\\(\delta\\\) statistic is through the Monte Carlo simulation (parametric bootstrapping) (Goldman, 1993). Another way of comparing different models without the
nested requirement is the Akaike information criterion
(minimum theoretical information criterion, AIC) (Akaike,
1974). The AIC is a useful measure that rewards models for
good fit, but imposes a penalty for unnecessary parameters
(e.g. Hasegawa, 1990). If L is the maximum value of the likelihood function for a specific model using n independently
adjusted parameters within the model, then \\\(AIC = –2ln L + 2n\\\). Smaller values of AIC indicate better models.

## Huelsenbeck and Crandall, 1997~\cite{huelsenbeck1997phylogeny}

One of the strengths of the maximum likelihood method of phylogenetic estima-
tion is the ease with which hypotheses can be formulated and tested.

```
@article{goldberger2005genomic,
  title={Genomic classification using an information-based similarity index: application to the SARS coronavirus},
  author={Goldberger, Ary L and Peng, C-K},
  journal={Journal of Computational Biology},
  volume={12},
  number={8},
  pages={1103--1116},
  year={2005},
  publisher={Mary Ann Liebert, Inc. 2 Madison Avenue Larchmont, NY 10538 USA}
}
```
## Genomic Classification Using an Information-Based Similarity Index: Application to the SARS Coronavirus







