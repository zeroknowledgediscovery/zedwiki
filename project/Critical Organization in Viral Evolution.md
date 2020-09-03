# Graphical Differences Between QNets of Coronavius and Influenza
<img alt='QNET' src="../uploads/crop_from_Li2020.PNG" width="700px">

QNet is a collection of decision trees, describing the dependency between different amino acids along the protein sequence of a virus [(Li2020)](https://www.medrxiv.org/content/10.1101/2020.07.17.20156364v3.full.pdf). Each tree yields the probability distribution of the animo acid at a certain position, given the protein sequence. By attaching all trees together, we obtain complex networks as in the figure above. We notice the visual differences between the networks of coronavirus and influenza. For example, the network for influenza have few central nodes with many connections, while the network for coronavirus have more nodes with high connections. These speculations are vague and untested, but if they were true, this knowledge could help us distinguish highly infectious virus, like coronavirus, from a common influenza.

# Statistical Differences in the Degree Distribution
<img alt='DegreeDistribution' src="../uploads/DegreeDistribution.PNG" width="700px">
By fitting the power-law model on the degree distribution of QNets, we observed the statistical difference on the value of alpha, the scaling parameter, between QNets built from coronavirus and from influenza. The estimation procedure follows section 3 of [Clauset2009](https://arxiv.org/pdf/0706.1062.pdf). Later, I should compare the power-law model with alternative hypotheses such as binomial distribution. 

Even though we show the difference in the scaling parameters, it is still not clear if it is due to 

1. the difference between controlled disease like influenza and epidemic disease lkike coronavirus
2. Biases from the creation of QNet because of the difference in the number of data. For coronavirus, the number of nodes is around 3000, while for influenza, it is only around 100-300. Perhaps, I should sample only 300 data points from coronavirus.

# 