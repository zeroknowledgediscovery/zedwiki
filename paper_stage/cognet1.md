# Reverse-engineering Societal Fracture

**Quantifying Difference in Opinion**

**Role of economic hardship in fomenting ideological divide in US society**


## Abstract

We report the development of a novel computational framework to uncover, represent and leverage hidden dependecies between opinions on contentious social topics, to ultimately craft a predictive theory of how opinions shift and mature in social groups. Using data from the General Social Survey that curates responses from approximately 40,000 US participants over 4 decades, we show that the ideological divide between the liberal and conservative thought-centers are modulated by economic variables, indicating the possibility of a causal influence from a faltering economy to worsening social polarization. Our data-driven framework, powered by novel learning algorithms, also quantifies the dependencies between key "hot-button topics", and induce a computable yet intrinsically meaningful metric to compare and contrast world-views at the level of individuals, groups, and communities across the societal hierarchy. Understanding how opinions shift, and coalesce is  key to informing  effective domestic policy, and opens the dorr to new research direction in social theory.

![polar distance]( /uploads/polardistance.png)

# Central Narrative
**Gross domestic product (GDP)** is the value of a nation's finished domestic goods and services during a specific time period. A related but different metric, the gross national product (GNP), is the value of all finished goods and services owned by a country's residents over a period of time.

<<Note("GNP __explains__ Polar distance over time. Note that GDPcap, GNI are also good predictors, but GNP is the best predictor that produces low enough llk and statistically significant coefficients. Most importantly this underlines the observation that as economic condition improves, the ideological divide between opinion poles falls. Relates economic conditions to the geometry of ideology")>>

# Key Insight

Our key insight is that opinions or beliefs on different topics or questions, either in an individual's mind or collectively in a social group, have conditional dependencies. These depedencies imply that conditional to the rest of one's beliefs, an opinion on a particular topic has a specific latent distribution. This conditional distrbution of an individual's opinion on a  topic is not necessarily degenerate, implying that this individual is free to alter their response when querried, provided the responses follow this latent distribution of responses. It follows that responses that define an empircal distribution subtantially different from the latent distribution are overwhelmingly unlikely, while those that define an empirical distribution close to the latent one are substantially more likely. Moreover, since  large deviations of an empirical distribution can be quantified, we can define a distance between two opinion vectors as follows: the probability of an opinion vector to realize the second one due to a perturbation in an empirical draw process.



# Definition of Ideological Consistency

+ https://www.pewresearch.org/politics/2014/06/12/section-1-growing-ideological-consistency/

Throughout this report we utilize a scale composed of 10 questions asked on Pew Research Center surveys going back to 1994 to gauge peoples’ ideological worldview. The questions cover a range of political values including attitudes about size and scope of government, the social safety net, immigration, homosexuality, business, the environment, foreign policy and racial discrimination. 

## Pew Research 10 questions

+ Government regulation of business does more harm than good
+ Government is wasteful and inefficient
+ Poor people have it easy because they can get benefits without doing anything
+ Government cannot afford to do much more to help the needy
+ Blacks who cant get ahead are responsible for their own condition
+ Immigrants are a burden becuase they take jobs, housing and healthcare
+ Most corporations make fair reasonable profit
+ Stricter environmental laws hurt trh economy
+ Best way to ensure peace is through military strength
+ Homosexuality should be discouraged by society


## add to polar

+ lessreg
+ natsoc
+ natenvir
+ natarms

# Metric Space for Beliefs, Opinions and Worldviews

There seems to be no existing literature on opinion metrization, where opinion vectors are treated as they occure: vector of responses to actual questions on socially relevant and often hot-button topics. Most analyses treat "opinions" as a scalar, which is very loosely related to the actual problem of quantifying opinion deviations in the real world.

Some authors have attempted to model "opinion formation" after vaguely similat physical phenomena. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0140406

In this study we answer the question:

> Are two opinions close or far apart, and by what amount? Can such a notion of distance be obtained which is intrinsic to social systems, and not merely a distance calculated between some vectors. 


![cognet metric]( /uploads/cognet_oneXX.png)


# Opinion polarization Literature
[opinion space](https://www.cs.uoi.gr/~tsap/publications/polarization.pdf)
\cite{matakos2017measuring}

Users tend to create connections with like-minded individuals, and create echo-chambers and filter bubbles that reinforce their existing opinions (Bakshy et al. 2015; Bessi et al. 2016). In such cases, instead of smoothing the differences, online social networks reinforce them, thus leading to increased polarization. 

<<Warn("This might not be true, mixing might also increase polrization counterintuitively")>>

In order to measure polarization, the  opinion
formation model of Friedkin and Johnsen~\cite{friedkin1990social} is used. In this model, opinions are modeled as
real numbers ranging from \\\(−1\\\) to \\\(1\\\). Each user \\\(u\\\)
has an internal opinion \\\(s_u\\\) that is fixed, and an expressed opinion
\\\(z_u\\\) that depends on their own internal opinion and the expressed opinions in their social
network. Using a random walk interpretation of the opinion formation model, we can
interpret \\\(z_u\\\) as the expected opinion that node \\\(u\\\) will reach when taking a random walk
in the social network. High value of \\\(z_u\\\) implies that the user is surrounded mostly
by single-minded individuals with extreme opinions, while low value implies that the social network of \\\(u\\\) adopts moderate and diverse opinions. We view the absolute
value \\\(|z_u| \\\) as a measure of the degree of the polarization of user \\\(u\\\). Given the vector
of expressed opinions \\\(\mathbf{z}\\\) for the whole network, the length of the opinion vector \\\(||\mathbf{z}||^2\\\)
captures the degree of polarization in the network, referred to as the polarization
index \\\(\pi(z)\\\) of the network.

Polarization due to rising social media is a common research topic~\cite{bakshy2015exposure} : [polarization exposure](https://www.science.org/doi/10.1126/science.aaa1160)


Cost of bipartisanship~\cite{garimella2018political}
We also find that users who try to bridge the echo chambers, by sharing content with diverse leaning, have to pay a »price of bipartisanship» in terms of their network centrality and content appreciation. In addition, we study the role of »gatekeepers,» users who consume content with diverse leaning but produce partisan content (with a single-sided leaning), in the formation of echo chambers. Finally, we apply these findings to the task of predicting partisans and gatekeepers from social and content features. While partisan users turn out relatively easy to identify, gatekeepers prove to be more challenging.




The rise of social media and online social networks has been a
disruptive force in society~\cite{musco2018minimizing}. Opinions are increasingly shaped by
interactions on online social media, and social phenomena including
disagreement and polarization are now tightly woven into everyday
life. In this work we initiate the study of the following question:
Given n agents, each with its own initial opinion that reflects its core value on a topic, and an
opinion dynamics model, what is the structure
of a social network that minimizes disagreement
and controversy simultaneously? 


\cite{mao2018spread} investigates information spread over cyber-social network of agents. The cyber-social network considered here comprises individuals and information sources. Each individual holds an opinion represented by a scalar that evolves over time. The information sources are stubborn, in the sense that their opinions are time-invariant. Individuals receive the opinions of information sources that are closer to their belief, confirmation bias is explicitly incorporated into the model. The proposed dynamics of cyber-social networks is adopted from DeGroot-Friedkin model, where an individual's opinion update mechanism is a convex combination of her innate opinion, her neighbors' opinions at the previous time step (obtained from the social network), and the opinions passed along by information sources from cyber layer which she follows.

Social-media platforms have created new ways for citizens to stay informed and participate in public debates. However, to enable a healthy environment for information sharing, social deliberation, and opinion formation, citizens need to be exposed to sufficiently diverse viewpoints that challenge their assumptions~\cite{aslay2018maximizing}, instead of being trapped inside filter bubbles. In this paper, we take a step in this direction and propose a novel approach to maximize the diversity of exposure in a social network. We formulate the problem in the context of information propagation, as a task of recommending a small number of news articles to selected users. We propose a realistic setting where we take into account content and user leanings, and the probability of further sharing an article. This setting allows us to capture the balance between maximizing the spread of information and ensuring the exposure of users to diverse viewpoints. The resulting problem can be cast as maximizing a monotone and submodular function subject to a matroid constraint on the allocation of articles to users. 



Controversy, disagreement, conflict, polarization and opinion divergence in social networks have been the subject of much recent research~\cite{chen2018quantifying}. In particular, researchers have addressed the question of how such concepts can be quantified given people's prior opinions, and how they can be optimized by influencing the opinion of a small number of people or by editing the network's connectivity.  In this paper, we depart from the
existing literature in focusing on risk of conflict, rather than on
conflict around one particular issue. In this way, we overcome both
shortcomings of prior work discussed above. We still rely on Friedkin and Johnsen’s model of opinion formation to quantify the risk of networks to conflict. However,
the proposed quantifications are independent of any particular set
of internal (or external) opinions, depending purely on the topology
of the network. In this way, we bypass the problem that quantifying
internal opinions is beyond reach in practice.

[Link to paper]( /uploads/conflictrisk.pdf)

# SOTA Models of Opinion Shift

+ **Dynamic Model** According to DeGroot’s model~\cite{degroot1974reaching}, people’s
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
    - **issue** Side steps the real issue of quantifying how to measure opinions
    - Much of this analysis comes from~\cite{bindel2015bad}, where again opinions are scalars

+ **Static model** In 1990, Friedkin and Johnsen extended the
model by DeGroot to have two different kinds of opinions~\cite{friedkin1990social}: an internal opinion \\\(s_i\\\) and an expressed opinion \\\(z_i\\\). The internal opinions of every person are assumed fixed, while the expressed
opinions are influenced by the node’s own internal opinion as well
the expressed opinions of the neighbors. Expressed in matrix-vector notation, and with wi i = 1 (a common
assumption in the literature that we also make in this paper), this
equation is solved by (3) below at equilibrium [6. In this model, the internal opinion si of node i is considered
a constant, and private to each individual, while the expressed
opinion zi is public, and a compromise between the internal opinion
of node i and the expressed opinion of node i’s neighbors.

Interestingly, within this framework, then we can quantify internal/external conflict, controversy and resistance, however, these specifications suffrer teh same issues described above


# Filter Bubbles

~cite{chitra2020analyzing}
While social networks have increased the diversity of ideas and information available to users, they are also blamed for increasing the polarization of user opinions. Eli Pariser's "filter bubble" hypothesis~\cite{pariser2011filter} explains this counterintuitive phenomenon by linking user polarization to algorithmic filtering: to increase user engagement, social media companies connect users with ideas they are already likely to agree with, thus creating echo chambers of users with very similar beliefs.

In this paper, we introduce a mathematical framework to assess the impact of this popular, yet unverified, hypothesis. We augment the classical Friedkin-Johnsen opinion dynamics model to include algorithmic filtering by introducing a network administrator --- an external actor that models social media companies by dynamically adjusting the strength of edges in a social network graph. When the network administrator is incentivized to reduce disagreement among interacting users, we experimentally demonstrate on networks from Reddit and Twitter that even small changes by the administrator to social network graphs can increase user polarization. We support our experiments with theoretical results by showing that social networks generated from the stochastic block model are provably sensitive to algorithmic filtering. Finally, we propose a simple modification to the incentives of the network administrator that limits the filter bubble effect without significantly affecting user engagement.

<<Warn("None of this holds up to actual experiments:  Chris Bale's paper~\cite{musco2018minimizing} shows that  more mixing may lead to more polarization, in explicit social media experiments (not graph simulations).")>>
[Chris bale's paper]( /uploads/chrisbail.pdf)



```
@article{matakos2017measuring,
  title={Measuring and moderating opinion polarization in social networks},
  author={Matakos, Antonis and Terzi, Evimaria and Tsaparas, Panayiotis},
  journal={Data Mining and Knowledge Discovery},
  volume={31},
  number={5},
  pages={1480--1505},
  year={2017},
  publisher={Springer}
}

@article{bakshy2015exposure,
  title={Exposure to ideologically diverse news and opinion on Facebook},
  author={Bakshy, Eytan and Messing, Solomon and Adamic, Lada A},
  journal={Science},
  volume={348},
  number={6239},
  pages={1130--1132},
  year={2015},
  publisher={American Association for the Advancement of Science}
}

@book{pariser2011filter,
  title={The filter bubble: What the Internet is hiding from you},
  author={Pariser, Eli},
  year={2011},
  publisher={Penguin UK}
}

@inproceedings{garimella2018political,
title={Political discourse on social media: Echo chambers, gatekeepers, and the price of bipartisanship}, 
author={Garimella, Kiran and De Francisci Morales, Gianmarco and Gionis, Aristides and Mathioudakis, Michael}, booktitle={Proceedings of the 2018 World Wide Web Conference}, 
pages={913--922}, 
year={2018} }

@inproceedings{musco2018minimizing, 
title={Minimizing polarization and disagreement in social networks}, 
author={Musco, Cameron and Musco, Christopher and Tsourakakis, Charalampos E}, 
booktitle={Proceedings of the 2018 World Wide Web Conference}, 
pages={369--378}, 
year={2018} }

@article{mao2018spread, 
title={Spread of information with confirmation bias in cyber-social networks}, 
author={Mao, Yanbing and Bolouki, Sadegh and Akyol, Emrah}, 
journal={IEEE Transactions on Network Science and Engineering}, 
volume={7}, 
number={2}, 
pages={688--700}, 
year={2018}, 
publisher={IEEE} }

@inproceedings{aslay2018maximizing, 
title={Maximizing the diversity of exposure in a social network}, 
author={Aslay, Cigdem and Matakos, Antonis and Galbrun, Esther and Gionis, Aristides}, 
booktitle={2018 IEEE International Conference on Data Mining (ICDM)}, 
pages={863--868}, 
year={2018}, 
organization={IEEE} }

@inproceedings{chen2018quantifying, title={Quantifying and minimizing risk of conflict in social networks}, 
author={Chen, Xi and Lijffijt, Jefrey and De Bie, Tijl}, 
booktitle={Proceedings of the 24th ACM SIGKDD International Conference on Knowledge Discovery & Data Mining}, pages={1197--1205}, 
year={2018} }

@article{bindel2015bad, title={How bad is forming your own opinion?}, 
author={Bindel, David and Kleinberg, Jon and Oren, Sigal}, 
journal={Games and Economic Behavior}, 
volume={92}, 
pages={248--265}, 
year={2015}, 
publisher={Elsevier} }

@inproceedings{chitra2020analyzing, 
title={Analyzing the impact of filter bubbles on social network polarization}, 
author={Chitra, Uthsav and Musco, Christopher}, 
booktitle={Proceedings of the 13th International Conference on Web Search and Data Mining}, 
pages={115--123}, 
year={2020} }

@article{bail2018exposure,
  title={Exposure to opposing views on social media can increase political polarization},
  author={Bail, Christopher A and Argyle, Lisa P and Brown, Taylor W and Bumpus, John P and Chen, Haohan and Hunzaker, MB Fallin and Lee, Jaemin and Mann, Marcus and Merhout, Friedolin and Volfovsky, Alexander},
  journal={Proceedings of the National Academy of Sciences},
  volume={115},
  number={37},
  pages={9216--9221},
  year={2018},
  publisher={National Acad Sciences}
}

@article{degroot1974reaching,
  title={Reaching a consensus},
  author={DeGroot, Morris H},
  journal={Journal of the American Statistical Association},
  volume={69},
  number={345},
  pages={118--121},
  year={1974},
  publisher={Taylor \& Francis}
}

@article{friedkin1990social,
  title={Social influence and opinions},
  author={Friedkin, Noah E and Johnsen, Eugene C},
  journal={Journal of Mathematical Sociology},
  volume={15},
  number={3-4},
  pages={193--206},
  year={1990},
  publisher={Taylor \& Francis}
}
```
