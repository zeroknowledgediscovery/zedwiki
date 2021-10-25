# Reverse-engineering Societal Fracture

**Quantifying Difference in Opinion**

**Role of economic hardship in fomenting ideological divide in US society**


## Abstract

We report the development of a novel computational framework to uncover, represent and leverage hidden dependecies between opinions on contentious social topics, to ultimately craft a predictive theory of how opinions shift and mature in social groups. Using data from the General Social Survey that curates responses from approximately 40,000 US participants over 4 decades, we show that the ideological divide between the liberal and conservative thought-centers are modulated by economic variables, indicating the possibility of a causal influence from a faltering economy to worsening social polarization. Our data-driven framework, powered by novel learning algorithms, also quantifies the dependencies between key "hot-button topics", and induce a computable yet intrinsically meaningful metric to compare and contrast world-views at the level of individuals, groups, and communities across the societal hierarchy. Understanding how opinions shift, and coalesce is  key to informing  effective domestic policy, and opens the dorr to new research direction in social theory.


# Polarization

https://www.journals.uchicago.edu/doi/full/10.1086/688938

Polarization is a topic of intense interest among social scientists, but there is significant
disagreement regarding the character of the phenomenon and little understanding of underlying mechanics. 

As a fact of social reality, polarization seems ubiquitous and all too easy to produce. Any small room filled with enough people and any remotely contentious issue seems to suffice to create polarization between rival factions. As a fact of modeling, however, it proves surprisingly difficult to produce a model in which simple and intuitive mechanisms produce patterns that even roughly resemble familiar patterns of polarization.

Imitation and the influence of social contacts are an obvious and ubiquitous aspect of opinion dynamics, but as early as 1964 Robert Abelson noted that models in which agents imitate the opinions of others seem to tend inevitably toward central convergence. Abelson points out one way computational models often fail: "Since universal ultimate agreement is an ubiquitous outcome of a very broad class of mathematical models, we are naturally led to inquire what on earth one must assume in order to generate the bimodal outcome of community cleavage studies"~\cite{abelson1964mathematical}. Another way that simple computational models can fail is by producing bifurcation that under iteration progressively drives all agents from middle values to the extremes at 0 and 1. Neither inevitable movement toward a central consensus nor inevitable movement to full polarized extremes seems characteristic of social polarization as we know it.


It has been repeatedly emphasized that models are constructed for many
purposes. Point predictions and a detailed mirroring of a complex reality are
typically not the point and are not at any rate to be expected from simplified
formal models (Epstein and Axtell 1996; Epstein 2006, 2008; Epstein et al.
2007; Miller, Page, and LeBaron 2008; Grim et al. 2013). It is often said of
physical phenomena, for example, that it is simple models constructed in
terms of spheres moving without friction on perfect planes that offers the
clearest explanation and most fundamental understanding. The challenge
for models of polarization that we pursue here, however, is in achieving even
such a basic explanatory model and simple fundamental understanding. The
question is not whether the simple computational models currently available
for opinion polarization offer a realistic portrayal of empirical phenomena.

Major families of models for social phenomena that have been appealed to as offering clues to the central mechanisms of polarization: 1) Axelrod’s Cultural Diffusion and Polarization models
represent one modeling tradition (Axelrod 1997; Klemm et al. 2005; Flache
and Macy 2006a; Centola et al. 2007). 2) The Hegselmann-Krause Bounded
Confidence model and Deffuant’s Relative Agreement model define another
approach (Deffuant et al. 2002; Hegselmann and Krause 2002; Deffuant
2006). 3) Models in a Structural Balance tradition constitute a third family
(Heider 1946; Cartwright and Harary 1956; Harary 1959; Macy et al. 2003;
Klemm et al. 2005; Kitts 2006). We extend the analysis to mechanisms for
‘group polarization’ suggested within social psychological theories of selfcategorization (Lord, Ross, and Lepper 1979; Hogg, Turner, and Davidson 1990). Each of the models analyzed purports to capture polarization, but it is
clear that both the kinds and the patterns of phenomena they generate vary
widely.

Common wisdom has it that American society is becoming increasingly polarized (Fiorina, Abrams, and Pope
2005; Brownstein 2007; McCarty, Poole, and Rosenthal 2008; Hetherington
and Weiler 2009). There are measurable aspects of political reality that support that common wisdom. In 1980, only 43% of Americans polled said that they thought there were important differences between the parties. The figure is now 74%. In 1976, almost a third thought it did not make a difference who was president. That figure is now cut in half. Between 1969 and 1976,
the Nixon and Ford years, the rate at which Republicans voted along party
lines was about 65% in both the House and the Senate. The same was true
of Democrats. Between 2001 and 2004, under George W. Bush, Republicans
voted with their party 90% of the time. Democrats voted with their party
85% of the time (McCarty et al. 2008).

It has been argued, however, that a focus on political polarization within the political elite obscures a stable or declining cultural polarization within the broader population. On most issues, public polarization has not increased
between groups, regardless of what groups are being compared: the young and the old, men and women, the more and the less educated, different regions of the country, or different religious affiliations. On a number of points, polarization has clearly decreased. Racial integration was once fought vociferously by major portions of the population, but that is certainly not true now. Views on women’s roles in public life were once extremely contentious in ways that are now quite generally recognized as archaic. 

Polarization is currently a topic of intense interest among social scientists, with analysis of congressional affiliation and voting patterns, sociological studies on popular attitudes, and laboratory studies on media influence and
attitude change all in search of a better understanding of central mechanisms (Fiorina and Abrams 2008; Iyengar, Sood, and Lelkes 2012; Ura and Ellis 2012; Druckman, Peterson, and Slothuus 2013; Großer and Palfrey 2013;
Lauderdale 2013; Levendusky 2013; Prior 2013; Leeper 2014; Thomsen 2014; Weinschenk 2014; Mason 2015). Claims regarding polarization, however, often remain frustratingly vague. The problem is not restricted to popular presentations but appears in the technical literature of sociology, economics, and political science as well. Entire articles appear on polarization with little attempt to make it clear what precisely is meant by the term~\cite{bramson2017understanding,bramson2016disambiguation}.


## Polarization type 1: Spread
An obvious way to measure polarization is in terms of the breadth of opinions; that is, how far apart are the extremes? DiMaggio, Evans, and Bryson call this ‘dispersion’: “the event that opinions are diverse, ‘far apart’ in content” (DiMaggio, Evans, and Bryson 1996, 694). They also outline a dispersion principle: “Other things being equal, the more dispersed opinion becomes, the more difficult it will be for the political system to establish and maintain centrist political consensus” (693).
**Polarization in the sense of spread does not consider whether the agents with the minimum and maximum beliefs are extreme case outliers or the edges of large clusters.** Spread also ignores group characteristics, and any groups in between the extremes. This lack of sensitivity to the shape of the distribution makes spread a weak measure of polarization in isolation.

## Polarization type 2: Dispersion
Another simple way to measure polarization is statistical dispersion (or statistical variation). Any of various measures of statistical dispersion might be used: mean difference, average absolute deviation, standard deviation, coefficient of variation, or entropy. Like spread, dispersion is a measure across the distribution, without being tied to notions of groups or subpopulations.

Bimodality is frequently mentioned as a feature of polarized distributions and sometimes as part of the definition~\cite{fiorinasamuel} (Fiorina et al. 2005).
   
## Polarization type 3: Coverage
The views of polarized factions are often thought of as constituting narrow and tightly packed sets of beliefs. A polarized society is thought of as one with little diversity of opinion, one in which only narrow bands of the opinion space are occupied. A simple way to envisage polarization in this sense is to think of the spectrum of possible beliefs as divided into small bins. The proportion of empty bins will then constitute a measure of polarization as coverage. 

## Polarization type 4: Regionalization
Coverage represents how much of the belief spectrum is occupied by a society, without accounting for the pattern of areas occupied. ‘Polarization’ can also be used to indicate belief regionalization, without attending to the total area covered over all. In considering small bins of possible belief, for example, we might measure polarization not in terms of how many bins are filled but in terms of how many empty regions there are between filled areas.

### Group Definition
No concept of groups is required for measures of polarization in terms of spread, dispersion, coverage, or regionalization. Other senses of polarization must be explicitly defined in terms of groups. One way to categorize groups is identify them directly from the histogram as collections of individuals categorized by the basins of attraction between local peaks, defining groups endogenously by the patterns in belief values,
~\cite{downey2001attitudinal}.

‘Polarization’ in various group-dependent senses is also used for cases in which groups are exogenously defined (e.g., by region, ethnicity, sex, education level, or other categories). Groups might also be defined in terms of network links representing association, influence, or communication. For example, one can first identify network-based groups using community structure algorithms, then use those collections of nodes as exogenously defined groups in order to break down the belief histogram.

## Polarization type 5: Community Fracturing
A first group-dependent sense of ‘polarization’ is community fracturing: the degree to which the population can be broken into subpopulations.
If agents are connected via a network structure, however, subcommunities may be referred to as ‘polarized’ simply in the sense that there is little or no communication between them. A similar phenomenon occurs in spatial models in which the locations of agents, or clusters of agents, are far apart [REF].

## Polarization type 6: Distinctness
People are polarized “insofar as people with different positions on an issue cluster into separate camps, with locations between the two modal positions sparsely occupied” (DiMaggio et al. 1996, 694); distinctness focuses on the sparse intermodal region. Attitudes toward abortion between 1970 and 1990, for example, show clear and persistent distinctness

## Polarization type 7: Group Divergence
While group distinctness captures how distinct the separation is between groups, regardless of how far away those groups are in their beliefs, group divergence captures the opposite: how distant the groups’ characteristic ideas are without attention to potential group overlap. 

## Polarization type 8: Group consensus
The beliefs of group members can be highly scattered across the spectrum or extremely focused on the group’s central ideology (fig. 11). The diversity of opinions within groups constitutes another sense in which those groups can be polarized, independent of how far apart their central ideas are and how distinct the groups are. Prima facie, the greater the variance in beliefs within groups, the more likely it would seem that members of one group might move toward common ground with other groups. The more single-minded or unanimous views are within the groups, the greater the polarization between them and the less likely any such conciliation. The smaller the variance within each distinct group, the greater this sense of polarization across the population. As previously mentioned, this is the main sense in which polarization has increased in the US legislature (McCarty et al. 2008).

## Polarization type 9: Size parity
A society that has one dominant opinion group with a few small minority outliers seems less polarized than one with a few comparably sized competing groups. Using the proportions of the population for each group, one can also use an entropy measure or a diversity indicator such as the inverse Simpson index.

# Multiple dimensions of polarization
One example of a sense of polarization requiring multiple dimensions is belief convergence. Given groups that are polarized on issue A, are these same groups polarized on B, C, and D? The more connected rival beliefs are within rival groups, the greater the polarization across the community. This can be measured using a data-clustering technique. Another example is belief coherence: are changes in one belief accompanied by analogous changes in another belief—a solidarity of ideas?

# Modeling Polarization

The first family of models that we consider targets cultural diffusion and differentiation as a basic mechanism for polarization. The extensive literature begins with Axelrod (1997) followed by significant further contributions in Klemm et al. (2003a, 2003c, 2005), Flache and Macy (2006a), and Centola et al. (2007). Bounded confidence and relative agreement models form a second family of models, in which the mechanism put forward for polarization is one in which updating on others’ opinions is constrained by a window or graded extent of prior agreement (Deffuant et al. 2002; Hegselmann and Krause 2002; Deffuant 2006). A third family we consider are models in the structural balance tradition (Heider 1946; Cartwright and Harary 1956; Harary 1959; Macy et al. 2003; Klemm et al. 2005; Kitts 2006). Here the basic mechanism of polarization is a change in network links of amity and enmity, further developed in terms of opinion or belief and employing mechanisms of Hebbian learning and Hopfield networks. Beyond these three families of models, we also consider ‘group polarization’ from social psychology (Lord et al. 1979; Hogg et al. 1990).

As indicated by our use of histograms in explicating the senses of polarization above, much of the literature on belief polarization uses ordinal or cardinal-valued belief spectra, such as those derived from Likert scale surveys and discretized population data. Although still discrete, variables of this type come with a lesser-to-greater order and usually an implicit/assumed scale such that a value of 1 is closer to 2 than it is to a value of 5. This creates a metric space that allows the use of distance measurements between values. Making this move for the Axelrod model, the similarity of two agents can be calculated as how far apart their trait values are rather than just how many features have strictly identical traits~\cite{bramson2017understanding}


The Axelrod family of models succeeds in producing a variety of senses of polarization, or their analogues, from a simple mechanism of similarity-based imitation across local interaction. It has a deep appeal because of this variety and the intuitive representation of cultures and interaction. But it should be noted that the Axelrod tradition also faces major limitations even within some of the areas to which it most clearly applies. In reality, social polarization of all sorts seems easy to produce, is robust across a wide range of characteristics, and often proliferates despite efforts to generate consensus. It is therefore natural to compare how changes in polarization in the model align with the social polarization we would expect.

<<Warn("In the Axelrod models, polarization only occurs strongly when the number of traits is greater than the number of features: the characteristics in which cultures can vary are few relative to the number of ways each characteristic can be expressed. It is not clear how we could systematically or objectively enumerate the number of either features or traits for real societies in order to check the plausibility of this claim. As a formal requirement for at least some cases, however, it may not be implausible. For example, one interpretation is that there must be more potential positions to take on each political issue than there are distinct issues on the table.")>>

<<Warn("The common reality of familiar forms of social polarization is that of roughly balanced oppositional groups. Polarization of the type that appears in the Axelrod models at equilibrium, in contrast, almost always either a is radically one-sided or b appears as a myriad of tiny groups. There is only a small window around the threshold q* in which a moderate number of moderately sized groups can be achieved as a final outcome, and even that is not robust to noise or the use of cardinal-valued features. Thus, the familiar social reality of group size parity polarization—a small number of equally balanced groups—is not something produced by either Axelrod’s mechanism or its extensions. We also note that the social world, along with almost all of its socially polarized subsystems, is not in equilibrium. The end-state polarized equilibrium of these models therefore cannot be expected to resemble the time series of opinions captured in sociological or political surveys.")>>




A major appeal of the Axelrod model remains, despite the limitations noted. That such a mechanism alone can produce divergence does accord with some recent empirical research that indicates that in-group members can be drawn together without any demonstrable psychological out-group repulsion (Bicchieri 2006; Dreu et al. 2010, 2011). There are other classic results, however, that show that even neutral evidence on an issue can have a distancing effect on groups that are already separated (Lord et al. 1979). The basic mechanism of the Axelrod model, then, may be an important, albeit incomplete, piece of the polarization puzzle.


In an influential series of articles, Hegselmann and Krause develop a ‘bounded confidence’ model of opinion polarization that functions in terms of mutual influence among those within a specific threshold of similarity (Hegselmann and Krause 2002, 2005, 2006). The primary results of the model are the formation of consensus given certain thresholds for who counts as ‘close enough’ and the formation of polarized groups with narrower thresholds. Furthermore, the number and location of the formation of polarized groups occurs at different points for different thresholds. Stated simply, this is another case of seeming incongruity between a plausible mechanism that can only increase the similarity of agents yet results in social fragmentation into separate ‘polarized’ attitude groups.

Opinions in the Hegselmann-Krause model are mapped onto the [0, 1] interval, with initial opinions spread uniformly at random. Belief updating is done by taking a weighted average of the opinions that are ‘close enough’ to an agent’s own. As agents’ beliefs change, a different set of agents or a different set of values can be expected to influence further updating. One way to think about the Hegselmann-Krause model is that all agents are effectively linked in a complete network, since it is possible for any agent to be influenced by any other. The primary mechanism of the model is then the threshold for what counts as ‘close enough’ for actual influence. Alternatively, one can think of the model as representing a dynamic network in which only those with opinions ‘close enough’ to an agent’s are linked in ways effective for belief updating.

The dynamics of an individual run make a few features immediately clear. First, in this model the groups are defined endogenously in exactly the way described in section 2.4. As a run progresses, the number of groups, and hence polarization in the sense of community fragmentation, decreases. Second, the averaging mechanism forces all the opinions within a group to be eventually identical. Polarization as group consensus therefore necessarily increases through the process. Third, because the opinion-averaging mechanism fuses any groups that are within the threshold of each other, the resulting groups are always completely distinct at equilibrium, another sense in which the mechanism necessarily increases polarization. In addition to these, it is clear from the second two frames of figure 15 that spread decreases as agents at extreme positions are pulled toward the population center, coverage decreases as agents coalesce into single-opinion groups, and the number of empty regions (regionalization) decreases along with the number of groups.

Deffuant’s Relative Agreement Model.—Deffuant and his collaborators introduce a number of additional mechanisms in what they term a ‘relative agreement’ model. Whereas the bounded confidence mechanism updates agents’ opinions in terms of the average opinion of those within a certain threshold range of current opinion, Deffuant et al. update agents in randomized pair-wise interactions. Any agent may be paired with any other agent to determine influence, reflecting something like a completely connected underlying interaction network (Deffuant et al. 2002; Deffuant 2006; Meadows and Cliff 2012).

One of the major goals of the Deffuant model is the attempt to produce extremism: convergence of opinion at an extreme end of the opinion range. Deffuant et al. note that this is possible in the Hegselmann-Krause model with asymmetric tolerance ranges but that it requires extreme parameters to produce. Related to this, the model is intended to demonstrate that a position that is initially extreme and held by only a few individuals can persuade the whole population to accept concordant extreme opinions.

Perhaps the greatest strike against this second family of models is that the central mechanism itself seems distinctly unreal. The main driver of the Hegselmann and Krause results is a mechanism of ‘peeling back from the edges’. The opinion distribution exhibited occurs for the very specific reason that agents at the left and right edges of the opinion space have no one to pull them left or right. They therefore drift toward the center, with either central or separated points of convergence dictated by the ε threshold. Despite the change in treatment of thresholds, the Deffuant et al. models inherit that central mechanism.

<<Warn("All models in this family cite and draw on a long tradition of belief averaging as a simple representation of the important psychological phenomenon of peer influence (French 1956; DeGroot 1974). But we are aware of virtually no evidence that real polarization occurs ‘from the edges’ as it does in these models or that it crystallizes in virtue of a specific distance from the edges as it does here. Indeed, there is a great body of evidence that the dynamics of developing polarization are quite different. The classic study by Lord et al. (1979) shows groups in laboratory conditions that progressively polarize, increasing the distance between them over time despite balanced bodies of evidence (see also Miller et al. 1993; Kuhn and Lao 1996). Cooper, Kelly, and Weaver claim that “one of the most robust findings in social psychology is that of attitude polarization following discussion with like-minded others” (2001, 267).")>>

---

<<Warn("Repeated studies show average attitudes among groups shifting toward extremes in terms of some mechanism not captured in the family of attraction-driven models considered here. The reality of increasing polarization of these familiar types, wherever it occurs, is a dynamic that this family of models is incapable of producing. These models also seem to capture an important and intuitive piece of the story of social opinion dynamics; however, it is not the whole story, and in many particulars it may not be most profitably read as a story of ‘polarization’ at all.")>>

![polar distance]( /uploads/polardistance.png)

# Central Narrative
**Gross domestic product (GDP)** is the value of a nation's finished domestic goods and services during a specific time period. A related but different metric, the gross national product (GNP), is the value of all finished goods and services owned by a country's residents over a period of time.

<<Note("GNP __explains__ Polar distance over time. Note that GDPcap, GNI are also good predictors, but GNP is the best predictor that produces low enough llk and statistically significant coefficients. Most importantly this underlines the observation that as economic condition improves, the ideological divide between opinion poles falls. Relates economic conditions to the geometry of ideology")>>


## Structural Balance Theory

Although less heralded in the computational literature, a third family of models for polarization has equal claim to consideration. Structural balance theory, also known as social balance theory, originated in the mid-1940s through the work of Fritz Heider, who studied patterns of belief coherence in individual psychology (Heider 1946). In the mid-1950s, Cartwright and Harary generalized and formalized Heider’s theory using basic graph theory (Cartwright and Harary 1956; Harary 1959). Consider a set of nodes (e.g., people or countries) joined into a network capturing not just whether they have a relationship but also the valence of that relationship. In the base version, if two nodes are joined then they are either friends or enemies; later versions allow valence weights between −1 and 1 (Kulakowski, Gawronski, and Gronek 2005). In the original analyses, a structure was considered ‘balanced’ whenever all paths—all unique sequences of links connecting each pair of nodes—had an odd number of negative links. Although there is some recent work that returns to the original ‘all paths’ version of balance calculations (Facchetti, Iacono, and Altafini 2011), Abell (1968) made the case against longer paths being meaningful for social relationships, and in most structural balance research the fundamental unit of analysis has been a triad of three mutually linked nodes.


A promise for understanding polarization can be seen in that dynamic. It is easy to prove that, for any complete network, progressively flipping valences within unstable triads will necessarily lead to either universal harmony or (with much higher probability) a ‘social mitosis’ resulting in precisely two groups, linked only by friendship internally and only by links of enmity between the two groups (Wang and Thorngate 2003; Sack et al. 2014). Social networks that are less than fully connected allow for more than two factions and the possibility of mixed networks, but the pattern toward social mitosis of the groups is still very much a dominant one (Hummon and Doreian 2003).

## Other SIgned Networks

A number of other models produce results closely related to structural balance, using a Hopfield mechanism of dynamic attraction that also echoes aspects of similarity interaction in Axelrod (Macy et al. 2003; Flache and Macy 2006b; Kitts 2006). In a Hopfield network, edge weights are determined through local calculations similar to those proposed in the section above but in which each node’s attribute is set to 1 or −1 depending on whether it is above or below 0 (Hopfield 1982). In Macy et al. (2003), nodes are characterized with either one or more binary states or one or more continuous states between 1 and 0. Link weights, or influence levels, are updated in Axelrod fashion as a function of the similarity between two linked nodes. If they occupy the same spot in the state space, the link between them becomes increasingly positive; if not, increasingly negative. Node characteristics are asynchronously updated by taking the link-weighted average node characteristics across one’s local neighbors and checking it against a threshold, then moving up to 1 or down to 0 accordingly. Where multiple characteristics are used, the process is repeated for each one independently.

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

+ lessreg (very little info)
+ confed
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

@article{abelson1964mathematical,
  title={Mathematical models of the distribution of attitudes under controversy},
  author={Abelson, Robert P},
  journal={Contributions to mathematical psychology},
  year={1964},
  publisher={Holt, Reinehart and Winston, Inc.}
}

@article{bramson2017understanding,
  title={Understanding polarization: Meanings, measures, and model evaluation},
  author={Bramson, Aaron and Grim, Patrick and Singer, Daniel J and Berger, William J and Sack, Graham and Fisher, Steven and Flocken, Carissa and Holman, Bennett},
  journal={Philosophy of science},
  volume={84},
  number={1},
  pages={115--159},
  year={2017},
  publisher={University of Chicago Press Chicago, IL}
}

@article{bramson2016disambiguation,
  title={Disambiguation of social polarization concepts and measures},
  author={Bramson, Aaron and Grim, Patrick and Singer, Daniel J and Fisher, Steven and Berger, William and Sack, Graham and Flocken, Carissa},
  journal={The Journal of Mathematical Sociology},
  volume={40},
  number={2},
  pages={80--111},
  year={2016},
  publisher={Taylor \& Francis}
}

@misc{fiorinasamuel,
  title={with Samuel J. Abrams and Jeremy C. Pope. 2005. Culture war? The myth of a polarized America},
  author={Fiorina, Morris P},
  publisher={New York: Pearson Longman}
}

@article{downey2001attitudinal,
  title={Attitudinal polarization and trimodal distributions: measurement problems and theoretical implications},
  author={Downey, Dennis J and Huffman, Matt L},
  journal={Social science quarterly},
  volume={82},
  number={3},
  pages={494--505},
  year={2001},
  publisher={Wiley Online Library}
}

```
