# Reverse-engineering Societal Fracture

** Role of economic hardship in fomenting ideological divide in US society**


## Abstract

We report the development of a novel computational framework to uncover, represent and leverage hidden dependecies between opinions on contentious social topics, to ultimately craft a predictive theory of how opinions shift and mature in social groups. Using data from the General Social Survey that curates responses from approximately 40,000 US participants over 4 decades, we show that the ideological divide between the liberal and conservative thought-centers are modulated by economic variables, indicating the possibility of a causal influence from a faltering economy to worsening social polarization. Our data-driven framework, powered by novel learning algorithms, also quantifies the dependencies between key "hot-button topics", and induce a computable yet intrinsically meaningful metric to compare and contrast world-views at the level of individuals, groups, and communities across the societal hierarchy. Understanding how opinions shift, and coalesce is  key to informing  effective domestic policy, and opens the dorr to new research direction in social theory.

![polar distance]( /uploads/polardistance.png)

# Central Narrative
Gross domestic product (GDP) is the value of a nation's finished domestic goods and services during a specific time period. A related but different metric, the gross national product (GNP), is the value of all finished goods and services owned by a country's residents over a period of time.

GNP "explains" Polar distance over time. Note that GDPcap, GNI are also good predictors, but GNP is the best predictor that produces low enough llk and statistically significant coefficients. Most importantly this underlines the observation that as economic condition improves, the ideological divide between opinion poles falls. Relates economic condition to ideological opinions

# Metric Space for Beliefs, Opinions and Worldviews

[opinion space](https://www.cs.uoi.gr/~tsap/publications/polarization.pdf)

[polarization exposure](https://www.science.org/doi/10.1126/science.aaa1160)


@inproceedings{garimella2018political,
  title={Political discourse on social media: Echo chambers, gatekeepers, and the price of bipartisanship},
  author={Garimella, Kiran and De Francisci Morales, Gianmarco and Gionis, Aristides and Mathioudakis, Michael},
  booktitle={Proceedings of the 2018 World Wide Web Conference},
  pages={913--922},
  year={2018}
}

We also find that users who try to bridge the echo chambers, by sharing content with diverse leaning, have to pay a »price of bipartisanship» in terms of their network centrality and content appreciation. In addition, we study the role of »gatekeepers,» users who consume content with diverse leaning but produce partisan content (with a single-sided leaning), in the formation of echo chambers. Finally, we apply these findings to the task of predicting partisans and gatekeepers from social and content features. While partisan users turn out relatively easy to identify, gatekeepers prove to be more challenging.


@inproceedings{musco2018minimizing,
  title={Minimizing polarization and disagreement in social networks},
  author={Musco, Cameron and Musco, Christopher and Tsourakakis, Charalampos E},
  booktitle={Proceedings of the 2018 World Wide Web Conference},
  pages={369--378},
  year={2018}
}

The rise of social media and online social networks has been a
disruptive force in society. Opinions are increasingly shaped by
interactions on online social media, and social phenomena including
disagreement and polarization are now tightly woven into everyday
life. In this work we initiate the study of the following question:
Given n agents, each with its own initial opinion that reflects its core value on a topic, and an
opinion dynamics model, what is the structure
of a social network that minimizes disagreement
and controversy simultaneously?
This question is central to recommender systems: should a recommender system prefer a link suggestion between two online
users with similar mindsets in order to keep disagreement low, or
between two users with different opinions in order to expose each
to the others viewpoint of the world, and decrease overall levels of
polarization and controversy? Such decisions have an important
global effect on society [48].


@article{mao2018spread,
  title={Spread of information with confirmation bias in cyber-social networks},
  author={Mao, Yanbing and Bolouki, Sadegh and Akyol, Emrah},
  journal={IEEE Transactions on Network Science and Engineering},
  volume={7},
  number={2},
  pages={688--700},
  year={2018},
  publisher={IEEE}
}

This paper provides a model to investigate information spread over cyber-social network of agents. The cyber-social network considered here comprises individuals and information sources. Each individual holds an opinion represented by a scalar that evolves over time. The information sources are stubborn, in the sense that their opinions are time-invariant. Individuals receive the opinions of information sources that are closer to their belief, confirmation bias is explicitly incorporated into the model. The proposed dynamics of cyber-social networks is adopted from DeGroot-Friedkin model, where an individual's opinion update mechanism is a convex combination of her innate opinion, her neighbors' opinions at the previous time step (obtained from the social network), and the opinions passed along by information sources from cyber layer which she follows.

@inproceedings{aslay2018maximizing,
  title={Maximizing the diversity of exposure in a social network},
  author={Aslay, Cigdem and Matakos, Antonis and Galbrun, Esther and Gionis, Aristides},
  booktitle={2018 IEEE International Conference on Data Mining (ICDM)},
  pages={863--868},
  year={2018},
  organization={IEEE}
}

Social-media platforms have created new ways for citizens to stay informed and participate in public debates. However, to enable a healthy environment for information sharing, social deliberation, and opinion formation, citizens need to be exposed to sufficiently diverse viewpoints that challenge their assumptions, instead of being trapped inside filter bubbles. In this paper, we take a step in this direction and propose a novel approach to maximize the diversity of exposure in a social network. We formulate the problem in the context of information propagation, as a task of recommending a small number of news articles to selected users. We propose a realistic setting where we take into account content and user leanings, and the probability of further sharing an article. This setting allows us to capture the balance between maximizing the spread of information and ensuring the exposure of users to diverse viewpoints. The resulting problem can be cast as maximizing a monotone and submodular function subject to a matroid constraint on the allocation of articles to users. 



@inproceedings{chen2018quantifying,
  title={Quantifying and minimizing risk of conflict in social networks},
  author={Chen, Xi and Lijffijt, Jefrey and De Bie, Tijl},
  booktitle={Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery \& Data Mining},
  pages={1197--1205},
  year={2018}
}

Controversy, disagreement, conflict, polarization and opinion divergence in social networks have been the subject of much recent research. In particular, researchers have addressed the question of how such concepts can be quantified given people's prior opinions, and how they can be optimized by influencing the opinion of a small number of people or by editing the network's connectivity.  In this paper, we depart from the
existing literature in focusing on risk of conflict, rather than on
conflict around one particular issue. In this way, we overcome both
shortcomings of prior work discussed above. We still rely on Friedkin and Johnsen’s model of opinion formation to quantify the risk of networks to conflict. However,
the proposed quantifications are independent of any particular set
of internal (or external) opinions, depending purely on the topology
of the network. In this way, we bypass the problem that quantifying
internal opinions is beyond reach in practice.

[Link to paper]( /uploads/conflictrisk.pdf)

### Models of Opinion Shift

+ **Dynamic Model** According to DeGroot’s model [11], people’s
opinions are updated gradually through repeated communication.
In the model, every person i ∈ V has an opinion si(t) at time t, and
it is influenced by its direct neighbors so as to evolve into a different
opinion si(t +1) in the next time step. More precisely, their opinion
is updated as the weighted sum of their own opinion (with weight
wi i ) and those of the neighbors (with weight wij for neighbor j).
Given a weighted graph G = (V, E,w), and the opinions si(t) of the
nodes at time t, the updating rule is defined as: **This model formalizes opinion formation as a repeated averaging process of one’s opinion with one’s neighbors**
    - **issue** Opinions are modlled as 1D scalar. They are not that in practice
    - **issue** The "update rule" is fixed and defined into existance
    - **issue** How do we learn the influence weights in practice
    - **issue** Not very applicable in reality

+ **Static model** In 1990, Friedkin and Johnsen extended the
model by DeGroot to have two different kinds of opinions [14]: an internal opinion si and an expressed opinion zi. The internal
opinions of every person are assumed fixed, while the expressed
opinions are influenced by the node’s own internal opinion as well
the expressed opinions of the neighbors. Expressed in matrix-vector notation, and with wi i = 1 (a common
assumption in the literature that we also make in this paper), this
equation is solved by (3) below at equilibrium [6. In this model, the internal opinion si of node i is considered
a constant, and private to each individual, while the expressed
opinion zi is public, and a compromise between the internal opinion
of node i and the expressed opinion of node i’s neighbors.

> Within this framework, then we can quantify internal/external conflict, controversy and resistance

@inproceedings{chitra2020analyzing,
  title={Analyzing the impact of filter bubbles on social network polarization},
  author={Chitra, Uthsav and Musco, Christopher},
  booktitle={Proceedings of the 13th International Conference on Web Search and Data Mining},
  pages={115--123},
  year={2020}
}

