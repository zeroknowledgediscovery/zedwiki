## MODELTEST


https://github.com/deepmind/alphafold

https://www.sciencedirect.com/science/article/pii/S0092867420310035 


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

Measures of genetic distance based on alignment methods are confined to studying sequences
that are conserved and identifiable in all organisms under study. A number of alignment-free
techniques based on either statistical linguistics or information theory have been developed to
overcome the limitations of alignment methods. We present a novel alignment-free approach
to measuring the similarity among genetic sequences that incorporates elements from both
word rank order-frequency statistics and information theory.

We have recently developed and validated a generic information-based similarity index to quantify
the similarity between symbolic sequences. This method, which has been used for analysis of complex
physiologic signals (Yang et al., 2003a) and literary texts (Yang et al., 2003b), can be readily adapted to
genetic sequences by examining usages of n-tuple nucleotides (“words”). We first determine the frequencies
for each n-tuple by applying a sliding window (moving one nucleotide/step) across the entire genome, and
then rank each n-tuple according to its frequency in descending order. To compare the similarity between
genetic sequences, we plot the rank number of each n-tuple in the first sequence against that of the
second sequence.

Produces phylogeny but not useful fot sampling or genertion/prediction of new sequences



```
@article{neher2014predicting,
  title={Predicting evolution from the shape of genealogical trees},
  author={Neher, Richard A and Russell, Colin A and Shraiman, Boris I},
  journal={Elife},
  volume={3},
  pages={e03568},
  year={2014},
  publisher={eLife Sciences Publications Limited}
}
```
## Predicting evolution from the shape of genealogical trees

Given a sample of genome sequences from an asexual population, can one predict its
evolutionary future? Here we demonstrate that the branching patterns of reconstructed genealogical
trees contains information about the relative fitness of the sampled sequences and that this
information can be used to predict successful strains. Our approach is based on the assumption
that evolution proceeds by accumulation of small effect mutations, does not require species
specific input and can be applied to any asexual population under persistent selection pressure.
We demonstrate its performance using historical data on seasonal influenza A/H3N2 virus. We
predict the progenitor lineage of the upcoming influenza season with near optimal performance in
30% of cases and make informative predictions in 16 out of 19 years. Beyond providing a tool for
prediction, our ability to make informative predictions implies persistent fitness variation among
circulating influenza A/H3N2 viruses.

A general method to predict the evolutionary trajectories of asexual populations would be extremely
valuable for understanding the population dynamics of pathogens or of malignant cells. For example,
the vaccine against seasonal influenza needs to be updated frequently since virus populations evolve
to evade increasing immunity among humans (Hampson, 2002; Nelson and Holmes, 2007). Reliable
prediction of the strains most likely to circulate in the upcoming season, and particularly the ability to
predict antigenic change, would be transformative to the vaccine strain selection process.

Predictability from genetic sequence data requires heritable fitness variation among the sampled
sequences. Neutral evolution - population dynamics in the absence of selective pressure - is by defini-
tion unpredictable: all sequences are equally fit. Yet even when selection determines the success of
individual lineages, predictability depends on the effect size of fitness-altering mutations.

# Integrating genotypes and phenotypes improves long-term forecasts of seasonal influenza A/H3N2 evolution

```
@article{huddleston2020integrating,
  title={Integrating genotypes and phenotypes improves long-term forecasts of seasonal influenza A/H3N2 evolution},
  author={Huddleston, John and Barnes, John R and Rowe, Thomas and Xu, Xiyan and Kondor, Rebecca and Wentworth, David E and Whittaker, Lynne and Ermetal, Burcu and Daniels, Rodney Stuart and McCauley, John W and others},
  journal={Elife},
  volume={9},
  pages={e60067},
  year={2020},
  publisher={eLife Sciences Publications Limited}
}
```

Integrates phenotypi information with sequnec edata. Only works fro flu, and results are crappy.


