+ Intermediate weakness: To what extent do there exist standards for reporting and characterizing
virus isolates beyond their sequence? What is the meta-data (beyond year of isolation and host
animal) that will be used to "chart trajectories of wild pathogens at scale?” Such details were not
readily apparent from the project description.

• Minor weakness: Since most viral sequences in data bases are likely to be based on short-read
technology, how will the full intact sequence of a "virus strain" be defined or assembled from such
data? So far, the examples of the methodology focus on single genes (e.g., spike of SARS-CoV-2
or HA of influenza); how can such analyses be extended to full 30kb genome sequences if the full
sequences are an infinitesimally small fraction of the total sequences in the database; of course,
full-length sequences could be assembled from the fragments, but this would introduce
assumptions.

• Minor weakness: Binding of the spike protein to its receptor and susceptibility of the binding to
neutralization by anti-spike antibody are important facets of the protein’s function and fitness.
However, they are incomplete; there is no consideration of other important measure provide
measures of spike function and fitness (e.g., fusion of the virus with the cell membrane).
Apparently, the analysis of vast viral genomic sequences are limited to the S1 domain of the spike
protein.

• Minor weakness: Although the plan mentions implementation of q-distance as a Findable,
Accessible, Interoperable, and Reusable (FAIR) tool, details on the implementation are absent.

• Data requirements for the model construction are not addressed. What is the DB size? Sequence
variability? Bias in sampling?

• Performance evaluation of constructed models is not addressed. With uncertain amount of data
(likely thousands or tens of thousands) and relatively complex models constructed, overfitting can
be a serious issue. Models should employ regularization, and performance should be assessed
using cross-validation / hold-out set. Using simulated data to assess performance and understand
data requirements would be helpful.

• What is the estimation of the computational cost? How does cost scale with sequence length?
Building in additional biological constraints so that not all positional dependencies need to be
modeled, would be useful.

• Similarly, zoonotic emergence potential requires large amounts of sequence data from zoonotic
reservoirs, limiting applicability.

• Fairly robust metrics of viral sequence evolution already exist, based on pretty solid sequence
mutation and evolutionary conservation principles. Unclear how this methodology would contrast
with these versus reinventing the wheel on known constraints for (e.g. Coronaviruses or Influenza)
pathogens to what this proposal is tailored (large scale, temporal datasets).

Several analyses and studies of viral sequence evolution, as well as systemic analyses of fitness
effects exist for viral pathogens such as Influenza (over the past 2 decades) and COVID-19. The
same is true for other pathogens.

• Unclear how methodologies will be applied or advanced broadly to research groups.

• Zoonotic prediction approach is only mentioned with no concrete implementation plans.

• In general, inadequate details or references to methods are given throughout the description of
the approach.

• Inadequate pitfalls or alternative approaches for any of the studies.

No timelines or estimated activities. This is especially key for the validation assays, which require
actionable outputs.
• Unclear what the input data will be for all of these studies. An example of HA from human influenza
A in 2008, and spike protein from “all” bat coronaviruses, but no concrete training sets are
described. No description of testing the robustness of q-value/qnet outputs (e.g. testing vs training
sets, altering input data richness).
• Insufficient description of how q-net outputs will be translated to (immediately) variants of interest
to phenotype in later aims, nor to (longer term) strains which can be predicted to emerge in coming
years. The q-net describes likely relations between nucleotides or residues, but how a single (or
subset of) sequences are extracted based on some scoring or abundance in the qnet is not
described.
• Little/no acknowledgment that sampling bias in sequence datasets exists
• Figure 3 suggests Qnet out predicts WHO recommendations, but no descriptions of metrics for
this performance. As above, no discussion of how the qnet output sequence was chosen in this
metric.
• WHO recommendations are not state of the art, but user guided. Many other approaches exist
which out predict WHO. There is a large literature on these, and thus benchmarking of the q-net
is not defined.
• Assumptions of the background population being relevant for modeling require clear annotation
of sequence provenance. It is unclear how this will be collected or addressed. This is key as
underlying assumptions are that given input sets for qnet construction require identical
background environment (based on their claim that the same pair of strains have different
distances between two ‘environments’: 2008 and 2009).

Validation assays are not well described. Increased receptor binding is not a metric of fitness.
Assays described for ‘neutralization’ are not even pseudo type neutralization assays, simply
protein-protein interaction hinderances. The antibody the authors describe is an anti-nucleocapsid
antibody, whereas their assay is a spike protein assay. Neutralization results in figure are not
clear given this information.

The costs of specific machinery, equipment, and usage fees needed for this proposal is not
accounted for in the budget.

Validation experiments are unclear, but flu (BSL-2 or higher) and COVID-19 (BSL-3) require
dedicated safety equipment and laboratory space, which is not well described.


