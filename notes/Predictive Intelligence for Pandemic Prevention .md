# Directorates 
+ Directorate for Computer and Information Science and Engineering (CISE)
+ Directorate for Biological Sciences (BIO)
+ Directorate for Engineering (ENG)
+ Directorate for Social, Behavioral and Economic Sciences (SBE)

# Grand Challenge Scheme

**Preparing For the Next Pandemic: Learning Wild Mutational Patterns At Scale For Forecasting Risky Sequence Divergence Before The First Human Infection**

As we begin to recover from the COVID-19 pandemic, a key question is if we can avert such disasters in future. Current surveillance protocols generally focus on qualitative impact assessments of viral diversity1. These efforts are primarily aimed at ecosystem and human impact monitoring, and do not help to precisely quantify emergence. We do not have the necessary tools to preempt risk of emergence from specific animal strains. Collecting viral strains from animal hosts is not helpful in mitigating a pandemic risk if we cannot rank individual strains by the risk they pose. We need new breakthroughs in theoretical understanding of the evolutionary processes that inform pattern recognition at scale to identify such risk. 

Thus, biosurveillance as it is done today is not enough to prevent the next pandemic. We need computational tools, backed by evolutionary theory, that allow us to recognize dangerous variants of wild viruses before the first human infection.

The COVID-19 pandemic may be seen as a direct result of this gap in knowledge. Despite ongoing studies on the possible  human infections from zoonotic strains of corona viruses, researchers were unable to precisely determine the true pandemic potential of strains similar to the SARS-CoV-2. This challenge is not unique to corona viruses. Periodic adjustment of the Influenza vaccine components is necessary to account for antigenic drift 4. The flu shot in each hemisphere is annually prepared at least six months in advance, and is based on a cocktail of historical strains determined by the World Health Organization (WHO) via global surveillance5, hoping to match the circulating strain(s) in the upcoming flu season. A variety of hard-to-model effects hinders this prediction, and have limited vaccine effectiveness in recent years7. The risk of emergence of the next swine flu, or an avian flu, thus remains  undetermined. 

Similar to the issue in preempting emergence, a key barrier to improving prediction of dominant circulating strains is the missing ability to numerically estimate the likelihood of specific future mutations. The state of the art urgently needs tools to compute the likelihood of a strain replicating in the wild to spontaneously give rise to another by random chance. Currently this likelihood is qualitatively equated to sequence similarity, which is measured by how many mutations it takes to change one strain to another2,3. In reality, the odds of one sequence mutating to another is a function of not just how many mutations they are apart to begin with, but also how specific mutations incrementally affect fitness. Ignoring the constraints arising from the need to conserve function makes any assessment of the mutation likelihood little more than subjective guesswork.

In a recent work7 supported by the Big Ideas Generator (BIG) project at the University of Chicago, we develop a more meaningful metric for comparison of genomic sequences. Our metric, the q-distance, precisely quantifies the probability of spontaneous jump by random chance. Learning from patterns of mutations from large sequence databases we distill the local dependency structures as conditional inference trees, which then reveals a complex mutational patterns specific to viral organism (see Fig. 1). The q-distance adapts to the specific organism, the background population, and realistic selection pressures; demonstrably improving inference of ancestral relationships and future trajectories. As an important application, we show that the q-distance predicts future strains for seasonal Influenza, outperforming the WHO recommended flu-shot composition almost consistently over two decades. Such performance is demonstrated separately for Northern and Southern hemisphere for different subtypes, and key capsidic proteins. Additionally, we investigate the SARS-CoV-2 origin problem, and precisely quantify the likelihood of different animal species that hosted an immediate progenitor, producing a list of related species of bats that have a quantifiably high likelihood of being the source. Additionally, we identify specific rodents with a credible likelihood of hosting an early ancestor on the possible lineage of SARS-CoV-2. Combining machine learning and large deviation theory, the analysis reported in our preprint may open the door to actionable predictions of future pandemics.

In conclusion, to minimize the odds of a future pandemic at the scale of we are experiencing, multiple fields of study must come together: we much leverage sophisticated algorithmic analysis of biological datasets, carry out subtle pattern discovery in the burgeoning sequence databases to quantify emergence risk -- not as an average measure -- but do so to actionably  identify specific risky strains poised at the edge of emergence. Only then can we take truly preemptive mitigating action. 

To win the war, we must take the fight to the animal reservoir, before a jump to the human populace actually occurs. 


1. Fair, J. & Fair, J. Viral forecasting, pathogen cataloging, and disease ecosystem mapping: Measuring returns on investments (2019)
2. Ozery-Flato, M. & Shamir, R. Two notes on genome rearrangement. Journal of Bioinformatics and Computational Biology 1, 71–94 (2003). 
3. Tesler, G. Efficient algorithms for multichromosomal genome rearrangements. Journal of Computer and System Sciences 65, 587–609 (2002).
4. Dos Santos, G., Neumeier, E. & Bekkat-Berkani, R. Influenza: Can we cope better with the unpredictable? Human vaccines & immunotherapeutics 12, 699–708 (2016).
5. Agor, J. K. & Özaltın, O. Y. Models for predicting the evolution of influenza to inform vaccine strain selection. Human vaccines & immunotherapeutics 14, 678–683 (2018).
6. https://www.cdc.gov/flu/vaccines-work/effectiveness-studies.htm.
7. https://www.medrxiv.org/content/10.1101/2020.07.17.20156364v3

# NORAD for Emergenet Bio-Threats: Global Active Pandemic Surveillance & Defense (PANDORA)

