# Infant Microbiome Modeling 
+   We have a set of `control variables` namely connected to the mode of feeding (3 modes)
+   We have a set of `internal state` observations in the form of bacterial colonization profiles
+   We have one or more `outcome measures` such as head circumeference measurement as a proxy of cognitive development
+   All these measurements have tagged timestamps

## Aim one: Reverse-engineering the Wiring between control to state to oucome
![http://34.66.189.202:4567/uploads/Untitled.jpeg](http://34.66.189.202:4567/uploads/Untitled.jpeg)

## Aim two: How Does Perturbations in Internal States or Control Variables Affect the Rest of the Parameters

## How do we incorporate time in the analysis

## Can we carry out modeling at the highest entity resolution?

# Relative Biome Dynamics

```
@article{lee2020exploring,
  title={Exploring the Role of Gut Bacteria in Health and Disease in Preterm Neonates},
  author={Lee, Jimmy Kok-Foo and Hern Tan, Loh Teng and Ramadas, Amutha and Ab Mutalib, Nurul-Syakima and Lee, Learn-Han},
  journal={International journal of environmental research and public health},
  volume={17},
  number={19},
  pages={6963},
  year={2020},
  publisher={Multidisciplinary Digital Publishing Institute}
}
```
File [here](/uploads/ijerph-17-06963.pdf)

...the postnatal very preterm gut is colonised in a structured sequence by facultative anaerobes followed by obligate anaerobes. The initial class is Bacilli followed by a bloom of Gammaproteobacteria and finally an increase in Clostridia. There is a paucity of Lactobacillus,Bifidobacillus and the phyla Bacteroidetes and Actinobacteria. 
+ The final pattern is well established by 30 to 36 weeks corrected age. 
+ At phylum level, Firmicutes dominates at 1 week and Proteobacteria at 1 month. 
+ The prevalence of Firmicutes at 1 week is 0.65 decreasing to 0.32 by 1 month while Proteobacteria increases from 0.28 to 0.66 over the same period. 
+ The Shannon diversity index ranges from 0.38 to 1.4 at 1 week, increases by 2 weeks and reaches 0.71 to 0.9 by 1 month.

1. measure the Shannon diversity index

```
@article{pammi2017intestinal,
  title={Intestinal dysbiosis in preterm infants preceding necrotizing enterocolitis: a systematic review and meta-analysis},
  author={Pammi, Mohan and Cope, Julia and Tarr, Phillip I and Warner, Barbara B and Morrow, Ardythe L and Mai, Volker and Gregory, Katherine E and Kroll, J Simon and McMurtry, Valerie and Ferris, Michael J and others},
  journal={Microbiome},
  volume={5},
  number={1},
  pages={31},
  year={2017},
  publisher={Springer}
}

```

File [here](https://microbiomejournal.biomedcentral.com/articles/10.1186/s40168-017-0248-8)


Microbial dysbiosis preceding NEC in preterm infants is characterized by increased relative abundances of Proteobacteria and decreased relative abundances of Firmicutes and Bacteroidetes. Microbiome optimization may provide a novel strategy for preventing NEC.


# causal analysis and directional inference
```
@article{sazal2021causal,
  title={Causal effects in microbiomes using interventional calculus},
  author={Sazal, Musfiqur and Stebliankin, Vitalii and Mathee, Kalai and Yoo, Changwon and Narasimhan, Giri},
  journal={Scientific reports},
  volume={11},
  number={1},
  pages={1--15},
  year={2021},
  publisher={Nature Publishing Group}
}

@article{john2016gut,
  title={The gut microbiome and obesity},
  author={John, George Kunnackal and Mullin, Gerard E},
  journal={Current oncology reports},
  volume={18},
  number={7},
  pages={1--7},
  year={2016},
  publisher={Springer}
}

@article{li2017gut,
  title={The gut microbiota and autism spectrum disorders},
  author={Li, Qinrui and Han, Ying and Dy, Angel Belle C and Hagerman, Randi J},
  journal={Frontiers in cellular neuroscience},
  pages={120},
  year={2017},
  publisher={Frontiers}
}
@article{honda2012microbiome,
  title={The microbiome in infectious disease and inflammation},
  author={Honda, Kenya and Littman, Dan R},
  journal={Annual review of immunology},
  volume={30},
  pages={759},
  year={2012},
  publisher={NIH Public Access}
}

@article{aarts2017gut,
  title={Gut microbiome in ADHD and its relation to neural reward anticipation},
  author={Aarts, Esther and Ederveen, Thomas HA and Naaijen, Jilly and Zwiers, Marcel P and Boekhorst, Jos and Timmerman, Harro M and Smeekens, Sanne P and Netea, Mihai G and Buitelaar, Jan K and Franke, Barbara and others},
  journal={PloS one},
  volume={12},
  number={9},
  pages={e0183509},
  year={2017},
  publisher={Public Library of Science San Francisco, CA USA}
}


@article{fischbach2018microbiome,
  title={Microbiome: focus on causation and mechanism},
  author={Fischbach, Michael A},
  journal={Cell},
  volume={174},
  number={4},
  pages={785--790},
  year={2018},
  publisher={Elsevier}
}


@inproceedings{sazal2018inferring,
  title={Inferring relationships in microbiomes from signed bayesian networks},
  author={Sazal, Musfiqur Rahman and Ruiz-Perez, Daniel and Cickovski, Trevor and Narasimhan, Giri},
  booktitle={2018 IEEE 8th International Conference on Computational Advances in Bio and Medical Sciences (ICCABS)},
  pages={1--1},
  year={2018},
  organization={IEEE}
}
```

With advancements in high-throughput sequencing technology, it is now possible to examine microbial diversity in microbiomes with increased precision, and has elucidated associations between the microbiome and phenotypes such as obesity, neurological disorders, inflammation, immune disorders, metabolic diseases, and more~\cite{john2016gut,li2017gut,honda2012microbiome,aarts2017gut}. Interest in constructing causal networks for microbiomes is recent~\cite{}. Focused experiments in the laboratory to elicit causal relationships within microbiomes do exist~\cite{fischbach2018microbiome}, but do not employ computational causal inferencing approaches. Sazal et al. were among the first to construct causal networks for microbiomes~\cite{sazal2018inferring}.

