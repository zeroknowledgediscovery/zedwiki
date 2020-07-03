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
