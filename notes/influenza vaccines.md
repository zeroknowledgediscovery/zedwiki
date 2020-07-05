The accessible surface area (ASA) or solvent-accessible surface area (SASA) is the surface area of a biomolecule that is accessible to a solvent. Measurement of ASA is usually described in units of square Ångstroms (a standard unit of measurement in molecular biology). ASA was first described by Lee & Richards in 1971 and is sometimes called the Lee-Richards molecular surface.[1] ASA is typically calculated using the 'rolling ball' algorithm developed by Shrake & Rupley in 1973.[2] Accessible surface area is often used when calculating the transfer free energy required to move a biomolecule from aqueous solvent to a non-polar solvent such as a lipid environment. It is recently suggested that (predicted) accessible surface area can be used to improve prediction of protein secondary structure.[5][6]

```
%[1] 
@article{lee1971interpretation,
  title={The interpretation of protein structures: estimation of static accessibility},
  author={Lee, Byungkook and Richards, Frederic M},
  journal={Journal of molecular biology},
  volume={55},
  number={3},
  pages={379--IN4},
  year={1971},
  publisher={Academic Press}
}

%[2]
@article{shrake1973environment,
  title={Environment and exposure to solvent of protein atoms. Lysozyme and insulin},
  author={Shrake, Andrew and Rupley, John A},
  journal={Journal of molecular biology},
  volume={79},
  number={2},
  pages={351--371},
  year={1973},
  publisher={Elsevier}
}

%5
@article{momen2008impact,
  title={Impact of residue accessible surface area on the prediction of protein secondary structures},
  author={Momen-Roknabadi, Amir and Sadeghi, Mehdi and Pezeshk, Hamid and Marashi, Sayed-Amir},
  journal={Bmc Bioinformatics},
  volume={9},
  number={1},
  pages={357},
  year={2008},
  publisher={Springer}
}
%6
@article{adamczak2005combining,
  title={Combining prediction of secondary structure and solvent accessibility in proteins},
  author={Adamczak, Rafa{\l} and Porollo, Aleksey and Meller, Jaros{\l}aw},
  journal={Proteins: Structure, Function, and Bioinformatics},
  volume={59},
  number={3},
  pages={467--475},
  year={2005},
  publisher={Wiley Online Library}
}
```


We indexed the 200 possible amino acid pairs for their compatibility regarding the three major physicochemical properties – size, charge and hydrophobicity – and constructed Size, Charge and Hydropathy Compatibility Indices and Matrices (SCI & SCM, CCI & CCM, and HCI & HCM). Each index characterized the expected strength of interaction (compatibility) of two amino acids by numbers from 1 (not compatible) to 20 (highly compatible). We found statistically significant positive correlations between these indices and the propensity for amino acid co-locations in real protein structures (a sample containing total 34630 co-locations in 80 different protein structures)
```
@article{biro2006amino,
  title={Amino acid size, charge, hydropathy indices and matrices for protein structure analysis},
  author={Biro, JC},
  journal={Theoretical Biology and Medical Modelling},
  volume={3},
  number={1},
  pages={15},
  year={2006},
  publisher={Springer}
}
```
Hydropathy patterning complements charge patterning to describe conformational preferences of disordered proteins
```
@article{zheng2020hydropathy,
  title={Hydropathy patterning complements charge patterning to describe conformational preferences of disordered proteins},
  author={Zheng, Wenwei and Dignon, Gregory and Brown, Matthew and Kim, Young C and Mittal, Jeetain},
  journal={The journal of physical chemistry letters},
  volume={11},
  number={9},
  pages={3408--3415},
  year={2020},
  publisher={ACS Publications}
}
```
Conformations of Intrinsically Disordered Proteins Are Influenced by Linear Sequence Distributions of Oppositely Charged Residues
```
@article{das2013conformations,
  title={Conformations of intrinsically disordered proteins are influenced by linear sequence distributions of oppositely charged residues},
  author={Das, Rahul K and Pappu, Rohit V},
  journal={Proceedings of the National Academy of Sciences},
  volume={110},
  number={33},
  pages={13392--13397},
  year={2013},
  publisher={National Acad Sciences}
}
```
# Comparative structural analysis of haemagglutinin proteins from type A influenza viruses: conserved and variable features
```
@article{righetto2014comparative,
  title={Comparative structural analysis of haemagglutinin proteins from type A influenza viruses: conserved and variable features},
  author={Righetto, Irene and Milani, Adelaide and Cattoli, Giovanni and Filippini, Francesco},
  journal={BMC bioinformatics},
  volume={15},
  number={1},
  pages={363},
  year={2014},
  publisher={Springer}
}
```

## Background
Genome variation is very high in influenza A viruses. However, viral evolution and spreading is strongly influenced by immunogenic features and capacity to bind host cells, depending in turn on the two major capsidic proteins. Therefore, such viruses are classified based on haemagglutinin and neuraminidase types, e.g. H5N1. Current analyses of viral evolution are based on serological and primary sequence comparison; however, comparative structural analysis of capsidic proteins can provide functional insights on surface regions possibly crucial to antigenicity and cell binding.

## Results
We performed extensive structural comparison of influenza virus haemagglutinins and of their domains and subregions to investigate type- and/or domain-specific variation. We found that structural closeness and primary sequence similarity are not always tightly related; moreover, type-specific features could be inferred when comparing surface properties of haemagglutinin subregions, monomers and trimers, in terms of electrostatics and hydropathy. Focusing on H5N1, we found that variation at the receptor binding domain surface intriguingly relates to branching of still circulating clades from those ones that are no longer circulating.

## Conclusions
Evidence from this work suggests that integrating phylogenetic and serological analyses by extensive structural comparison can help in understanding the ‘functional evolution’ of viral surface determinants. In particular, variation in electrostatic and hydropathy patches can provide molecular evolution markers: intriguing surface charge redistribution characterizing the haemagglutinin receptor binding domains from circulating H5N1 clades 2 and 7 might have contributed to antigenic escape hence to their evolutionary success and spreading.

## IMPORTANT

Variation of some protein properties sometimes may depend only on local and limited hanges, e.g. mutation of a few - or even only one - residue(s) within linear or conformational motifs. In fact, even when local variation in sequence is seemingly poorly evident, it may result in locally dramatic changes in accessible surface area, electrostatic potential, hydropathy or hydrophilicity features that can deeply change motif functionality. It is common knowledge that variation in surface features of a protein can modulate recognition interactions of the protein itself. Since variation often depends on mutation of a number of residues and changes in side chains can vary multiple biochemical features, it is difficult or even nonsense trying to establish a priori which specific property (among e.g. surface area and shape, electrostatics or hydrophobicity) should be more relevant than others in modulating recognition interactions. In fact, changes in each specific property can result in such modulation, and this can be independent on variation of other features, or modulation can result from the aggregate or synergistic effect of multiple feature changes. So far, several sequence-based studies on variation could provide valuable phylogenetic evidence; however, such studies are of minor help in inferring variation at protein regions including amino acids that are far each other in the primary sequence and quite close within the 3D protein structure (conformational epitopes). In practice, while sequence-based investigation can be good in highlighting very evident changes at individual positions of a protein chain, in general they fail in highlighting meaningful `group variation’, i.e. in identifying - especially when the overall variation is relevant and spread - relationship of specific multiple changes to variation in conformational epitopes hence in interactions they mediate.

## The two track Rule

Stressing relevance of local surface variation is particularly important when considering special constraints addressing viruses evolution: keeping basic properties in simplified but complex pathogenic systems while simultaneously varying - as much as possible - all variable epitopes, in order to escape the immune responses of their hosts. Therefore, viral genome evolution runs along two parallel tracks, both of which, like in railways, must be followed: (i) mutations in sites crucial to protein machinery mediating basic functions (e.g. in motifs relevant to host recognition or cell entrance) are not allowed because they strongly impair viral fitness, and at the same time, (ii) hyper-variability is needed to escape recognition by neutralizing antibodies (`antigenic drift’, [7]). Given that surface viral proteins do not interact only with antibodies (as their original function is to contact the host), in addition to determining antigenic drift, variation can also influence pathogenicity (because e.g. of modified interaction with cell receptors in different tissues and organ districts) or host specificity. Influenza viruses do not escape such a two-tracks rule, hence while global structure conservation ensures basic functions, limited or even subtle changes in local structural features may modulate interactions of the viral proteins with the host molecules/cells and thus mechanisms underlying antigenic drift, pathogenicity shifts and host specificity change.


## sequence based studies

Thanks to the availability of thousands of viral genomes/gene sequences and of several specific antibodies/vaccines, a large number of sequence-based/phylogenetic and serological analyses of avian flu viruses have been performed and published so far. This notwithstanding, mechanisms in viral evolution are still elusive, as genome/proteome-wide analyses on sequence variation or antigenic features are able to only partially unveil a number of relevant changes, because of the overall mutational noise. Therefore, structural zoom in is needed to integrate such analyses by identifying `meaningful’ variation. This prompted us to take advantage from availability of structural templates to perform structural comparison among different HA subtypes, in order to identify subtype- and subregion-specific feature variation suggestive for possible involvement in antigenic recognition, or pathogenicity and host specificity. Last but not least, evidence from structural comparison can check relationship among serological, phylogenetic and structural closeness.

## comparison among solved HA structures: prior work
 Preliminary analysis of the six available HA structures was performed in order to evaluate intra- and inter-group structural variation by superposition of all structure pairs and computation of their Root Mean Square Deviation (RMSD). Indeed, the RMSD of two superposed structures indicates their `structural divergence’ from one another. As both sequence mutation and conformational variation inflate the RMSD, values up to 2 Ångstrom indicate structural similarity [17].
 
 
 ```
 %17
 @article{carugo2001normalized,
  title={A normalized root-mean-spuare distance for comparing protein three-dimensional structures},
  author={Carugo, Oliviero and Pongor, S{\'a}ndor},
  journal={Protein science},
  volume={10},
  number={7},
  pages={1470--1473},
  year={2001},
  publisher={Wiley Online Library}
}
```

Evidence that RMSD values for monomer pairs are lower than those ones for corresponding HA1 or RBD regions is not surprising, because RBDs are major determinants in antigenic variation [9].

```
%9
@article{russell2004h1,
  title={H1 and H7 influenza haemagglutinin structures extend a structural classification of haemagglutinin subtypes},
  author={Russell, RJ and Gamblin, SJ and Haire, LF and Stevens, DJ and Xiao, B and Ha, Y and Skehel, JJ},
  journal={Virology},
  volume={325},
  number={2},
  pages={287--296},
  year={2004},
  publisher={Elsevier}
}

```

Structural fold and architecture can be highly conserved even among proteins and protein domains showing no sequence homology because of either long evolutionary divergence or even convergent evolution [21]. At the same time, within such families, fold can be disrupted (resulting in loss of function and disease) by single or few specific mutation(s), which indeed result in keeping 99% or higher sequence identity values [22],[23]. 


```
%21
@article{de2014longin,
  title={Longin and GAF domains: structural evolution and adaptation to the subcellular trafficking machinery},
  author={De Franceschi, Nicola and Wild, Klemens and Schlacht, Alexander and Dacks, Joel B and Sinning, Irmgard and Filippini, Francesco},
  journal={Traffic},
  volume={15},
  number={1},
  pages={104--121},
  year={2014},
  publisher={Wiley Online Library}
}
%22
@article{jang2002crystal,
  title={Crystal structure of SEDL and its implications for a genetic disease spondyloepiphyseal dysplasia tarda},
  author={Jang, Se Bok and Kim, Yeon-Gil and Cho, Yong-Soon and Suh, Pann-Ghill and Kim, Kyung-Hwa and Oh, Byung-Ha},
  journal={Journal of Biological Chemistry},
  volume={277},
  number={51},
  pages={49863--49869},
  year={2002},
  publisher={ASBMB}
}
%23
@article{jeyabalan2010sedlin,
  title={SEDLIN forms homodimers: characterisation of SEDLIN mutations and their interactions with transcription factors MBP1, PITX1 and SF1},
  author={Jeyabalan, Jeshmi and Nesbit, M Andrew and Galvanovskis, Juris and Callaghan, Richard and Rorsman, Patrik and Thakker, Rajesh V},
  journal={PloS one},
  volume={5},
  number={5},
  pages={e10646},
  year={2010},
  publisher={Public Library of Science}
}

```

Mutations altering the overall backbone/fold of the RBD would impair binding to host cells hence conservation (track 1) is needed to keep such basic function. However, local variation (track 2) is needed to modulate surface features hence interactions. Therefore, we did not further investigate secondary structure variation and moved instead to surface analysis, considering both most relevant features: (i) electrostatic charge distribution and (ii) hydropathy/hydrophilicity patches.

## Why we Need Phylogeny: And Hence q-phylogeny should be better

Evidence from this work shows that sequence homology is often, but not always, related to structural similarity and vice versa. In fact, in some instances, protein domains with less related sequences can show intriguing structural closeness. Therefore, in order to obtain a more complete view of the `functional evolution’, phylogenetic analyses based on sequence comparison and resulting in trees, might be integrated taking into account information from structural comparison.




# Efforts to Improve the Seasonal Influenza Vaccine

```
@article{harding2018efforts,
  title={Efforts to improve the seasonal influenza vaccine},
  author={Harding, Alfred T and Heaton, Nicholas S},
  journal={Vaccines},
  volume={6},
  number={2},
  pages={19},
  year={2018},
  publisher={Multidisciplinary Digital Publishing Institute}
}
```

Data from the WHO Global Influenza Surveillance and Response System ensures the strains in the vaccine match circulating viruses; hence, the term “seasonal vaccine” [5]. This need for continual adjustment of the vaccine formula is a result of influenza viruses’ ability to accumulate mutations over time, a process termed “antigenic drift” [6]. Influenza viruses, like many RNA viruses, have a much higher mutation rate than organisms with DNA genomes due to the lower fidelity of RNA polymerases [7]. Intrinsic viral mutation combined with immune selective pressures result in the fixation of viral variants that are antigenically distinct from their predecessors. These “drifted” viruses are frequently capable of escaping the immune response elicited by the previous vaccination or infection, leading to the requirement for constant monitoring and testing of isolated strains to ensure the current vaccine is a match to circulating viruses. Vaccine mediated protection against influenza viruses is further complicated by the fact that the segmented viral genome permits two different virus strains to reassort genetic material with one another upon coinfection, potentially leading to “antigenic shift” [8]. Antigenic shift enables the creation of antigenically novel viral strains capable of causing pandemic outbreaks. Thus, seasonal influenza vaccine production must be flexible enough to deal with the annual acquisition of mutations in circulating strains and to rapidly respond to pandemic outbreaks as occurred with a reassortant H1N1 strain in 2009 [9].

Rapid influenza virus evolution leads to the yearly requirement for massive vaccine manufacturing infrastructure capable of generating hundreds of millions doses. Currently, the majority of influenza virus vaccines are manufactured using embryonated chicken eggs [10].

Increased production time reduces the flexibility of the manufacturing process, necessitating the start of production long before the start of the season. This timeline reduces the ability of public health officials to adapt to sudden changes in circulating strains. This process of egg-adaptation is both slow and, at times, ineffective. Despite efforts to adapt reassortant viruses to culture in eggs, some strains, especially H3N2 viruses, continue to grow poorly in eggs [25]. This inability to adapt strains can result in significant delays in vaccine production due to the lower yield of these strains and, in some severe cases, may necessitate the removal of a predicted strain due to its inability to be grown to sufficient levels [25,26]. This problem occurred during the 2003–2004 season, when the predicted A/Fujian/411/2002 strain was unable to be grown successfully in chicken eggs and was subsequently replaced by the prior year’s H3N2 strain [27].

Thus, many of the mutations influenza viruses accumulate during egg-adaptation result in altered antigenicity. This potentially changed antigenicity is usually controlled for during the generation of CVVs by continually testing the antigenicity of isolated strains. However, due to the complex nature of influenza immune responses in individuals with multiple exposures to different strains, it can be difficult to accurately predict the antigenicity of a given vaccine strain

Despite the fluctuating efficacy of the seasonal influenza vaccine from year to year, it remains the best strategy for combating infection. Experimental universal influenza vaccines are intended to broadly protect against many (if not all) influenza virus strains regardless of antigenic mutation in the HA head domain (reviewed in [86,87,88]). As with the development of any new vaccine, the timeline for their widespread use in humans, as well as their true efficacy against divergent viral strains is uncertain. Thus, as a short-term measure, efforts to improve the efficacy of the seasonal vaccine as well as the development of other anti-viral therapeutics are still needed. The development and application of new approaches to improve on the current technologies, along with the development of completely new vaccines, makes this an exciting time to be part of the influenza virus research community. Current efforts and further optimization of many complementary strategies for influenza vaccine development are critical to our ability to reduce and even prevent the epidemic and pandemic outbreaks of the future.

# DNA Vacccines against Influenza

[DNA Vaccines](http://34.66.189.202:4567/uploads/dnavaccines.pdf)

```
@article{stachyra2014dna,
  title={DNA vaccines against influenza.},
  author={Stachyra, Anna and G{\'o}ra-Sochacka, Anna and Sirko, Agnieszka},
  journal={Acta Biochimica Polonica},
  volume={61},
  number={3},
  year={2014}
}
```

