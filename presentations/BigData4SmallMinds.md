# TXT

 Welcome to today's topic: *Big Data for Small Minds*, where we  will try to wrap our heads around the notion of bigness of big data; hopefully, by the end, we will convince ourselves that it involves a bit more than raw size, and that such "bigness" has non-trivial implications for how we work with, and reason about, problems in which such datasets arise.
 I am Ishanu Chattopadhyay, Assistant Professor of Medicine, and in my research group, we aim to solve hard questions in biomedicine and the social sciences, particularly where such problems are associated with large and complex datasets. We spend a lot of time thinking about how to analyze such data, how we can use such data to answer important questions, and if such data can point us to questions that we have not yet thought to ask. 
 
 So lets begin at the begining. What is data? As I think about about it, data is a collection of shallow, mechnically gathered
 systematic record of information. By shallow I mean, individula datapts do not necessarily have much nmeaning, but as an aggerate they convery an emergent picture. 
 
 Now, that datasets are important, this notionis not new. Going back to teh Roiman empire, there were tabularia which were fancy buildings housing extensive records of business transcations, with tehgoal of analyzing teh state of commerce in teh city and teh empire. And in science, lareg datasets have time and agaisn been instrumental. Tyco bRahe is perhaps the most obvious example. In the 16th centurey, he spendt his life gtahering precise astronomical observations, position of starts, motion of planets, and whiel he is credietd with some impoartant astronomical discovereies, his biggest contribution was amassing this dataset, which was trhen used by J. Keplar to derive the three keplers's of planetary motion, which directly influences or enabled Newton  to formulate the universal law of gravitation. 
 
 A couple of centuries later, detailed poliination experiments on pea plants led Mendel to formulate the laws of mendemlian genetics, laying teh foundation of modern biology. He carried out some 30K meticulous experiments to come up with jis laws. Now teh question is that "big data", or for that matter, Tyco Brahe's voluminous collection fo astronomical data: is that "big data"?
 
 Lets think about this. Noet that bith tehse data sets led to "simple explanations". Three lwas of planetary motion,. or the law of universal gravitaion, or teh mendelian laws fo genetics. In essensce thse adatsets were "simple", large no doubt, but simple. The way I think about "bigness" of data, is its intrinsic complexity, where we might fail to obtain simple representations of such datasets. Hold that thought for  amoment,
 
 Lets think about what is the purpose of data, in general. Document phenomena, forecast, predict, optimize decisions, and in general, formulate scientifc theories. That ledas us to ask, what then is a scientifci theory? Well, one way tothink of scientific theories are that they are collection of equations, principles, which are compressed representation fo data about teh physical world. Note that scintific theories -- famous scirntific theories -- in physics and biology are always simple. After all the equations of quantum mechanics can be written down on teh back of an envelope, and the equation fo einstenian relativity, using teh right notation, is even simpler. Why is that so? Maybe nature is like that: when lookedat with teh right abstraction, and when asked the right questions, the answers are simple. ANd there is some reasoning that supports that conclusion. Howwever, it may also be that we have uncovered simple equation and imple principles, because that is what we are able to comprehend, thats what we looked for, and the complex pjhenomena were , well too complex, that we havent stumbled on them yet.
 
 And this is a very real possibility. Think about how teh scientific method works. We start with some experiments, which produces data, that data is used to formulate hypotheses (equations, principles, laws), and then we do more experiments to validate those laws, and if there is a mismatch, we update our hypotheses.. leading to this eternal diaglogue with nature. Is there subjectivity build into this process -- why yes off ocurse.. its athe capacity of the human mind that determines these hypotheses. Is thsi possible that really complex processes requires hypothese so complicated that we generally dont consider them as valid theories within this classical cyclical process. 
 
 That is not only plausible, that is actually likely. In fact most questions of interest in biology, biomedicine and teh social sciences fall in this category. Who belives that we we can write down an equation which outlines the detailed operation of cellular machinery. These are emergent phenomena, where clean first principle "laws" either dont exist or are too complex.
 
 What are some examples? Pnademics.. how they manifest, and respond to countermeasures. How novel pathogens emerge.. why are some spillover events result in epidemicda and pandemics, while other dont? How do we model socila dynamics? Are events like crime predictable? How do we screen for complex diseases, diseases which are shaped by the interaction of hundreds of thosands of genes, and unchareted epigentic effects, it is lamost obvious that there phgenomena do not have "simple" explanations, and teh data about them are not compressible by a a few laws.. they are intrinsically complex. 
 
 So what now? Clearly this cyclic approach will not work? Can we salvage it? Yes, we have to reinterpret what we mean by "undertanding". We can make broad hypotheses, but some part of the "model" that we infer, will always be not "simple" or "understandable" in teh classical sense. The complexity has to go somewhere, since simple laws do not exist, the inherent compelxity of the phenomena must be represented somewhere. And we have to be OK with that, because it appears that some problems or phenomena in nature are like that... they have emergent complexity, and to reason abou them, or answer questions about them, we need to work with that irreducible complexity.
 
 How do we doit? Well a popular approach is machine learning. We have inputs and outputs and the tool sof ML will tell you how the inputs conenct with teh outputs. WHat goes on in that jumble of connections might not be undertsandble, but thats ok, that is what capturing the irreducible complexity of the phenomenois you are trying to study.
 
 Lets look at some cncrete  example. 
 



Lets start at the beginining. Lets us ask ourselves: what is data? 




# plan


@startuml
salt
{
{T
 + Presentation: 90 min
 ++ What is Big Data / ML / AI: 15min
 +++ Large amounts of data have been used before
 ++++ Tyco Brah, Johanes Keplar, Mendel, and many others.
 ++++ Even the human genome decoding
 +++ Now, The results are often not simple equations
 ++++Ground truth might be too complex for our small minds
 +++++ We intend to find answers to questions we have not yet thought to ask
 ++ Applications
 +++ EHR data for screening 20 min
 +++ Databases of sequences 20 min
 +++ Complex systems and rare and extreme events 15 min
 +++ Crime  15 min
 }
}
@enduml

<img src="https://cdn.britannica.com/77/83677-050-D0958F1A/Tycho-Brahe.jpg" alt="drawing" width="200"/>

+ Tycho Brahe was in essensce the first dat ascientist. Collected precise astronomical observations, with instruments he himself developed (teh sextant), and amassed data that enabled Keplar to come up with his laws of planetary motion.
+ Johannes Kepler is best known for his three laws of planetary motion. These laws are: Planets move in orbits shaped like an ellipse. A line between a planet and the Sun covers equal areas in equal times.

<img src="https://cdn.britannica.com/57/139557-004-F4E7E357/portrait-Johannes-Kepler-1730.jpg?s=1500x700&q=85" alt="drawing" width="200"/>



## defn of data

+ When we reference data today, we are speaking about very shallow, very specific, and very unambiguous observations.  Consider a buoy out at sea.  One data point from the buoy will tell you the sea temperature, elevation, and direction of the ocean current at a very specific GPS location at 2:05:05 PM on June 22nd, 2015. In fact, the information is so shallow, that we need to take these data points and combine them with many others to get a bigger picture.  This is precisely why the word data is almost always encountered in the plural.  It could be said that a datum is only valuable when it is combined into data (it’s about as valuable as a single pant that’s not joined into pants).
+ data is shallow, mechanically-gathered, systematic information that is recorded in an inanimate device.
+ we can add another constraint: data is self-consciously gathered – it does not result from another activity. Noe tthat this does not always apply, for example EHR data.  In ancient Rome they had tabularia – storehouses of receipts from individual purchases that gave the Romans vision into the state of commerce within the city.

<img src="https://upload.wikimedia.org/wikipedia/commons/d/d0/Depiction_of_the_Forum_Romanum_%281866%29.jpg" alt="drawing" width="200"/>
+ Mendel 


<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Gregor_Mendel_2.jpg/800px-Gregor_Mendel_2.jpg" alt="drawing" width="200"/>

Johann Gregor Mendel (1822–1884) was a lifelong learner, teacher, scientist, and man of faith. As a young adult, he joined the Augustinian Abbey of St. Thomas in Brno in what is now the Czech Republic. Supported by the monastery, he taught physics, botany, and natural science courses at the secondary and university levels. In 1856, he began a decade-long research pursuit involving inheritance patterns in honeybees and plants, ultimately settling on pea plants as his primary model system (a system with convenient characteristics that is used to study a specific biological phenomenon to gain understanding to be applied to other systems). In 1865, Mendel presented the results of his experiments with nearly 30,000 pea plants to the local natural history society. He demonstrated that traits are transmitted faithfully from parents to offspring in specific patterns. In 1866, he published his work, Experiments in Plant Hybridization,1 in the proceedings of the Natural History Society of Brünn.

Mendel’s work went virtually unnoticed by the scientific community, which incorrectly believed that the process of inheritance involved a blending of parental traits that produced an intermediate physical appearance in offspring. This hypothetical process appeared to be correct because of what we know now as continuous variation. Continuous variation is the range of small differences we see among individuals in a characteristic like human height. It does appear that offspring are a “blend” of their parents’ traits when we look at characteristics that exhibit continuous variation. Mendel worked instead with traits that show discontinuous variation. Discontinuous variation is the variation seen among individuals when each individual shows one of two—or a very few—easily distinguishable traits, such as violet or white flowers. Mendel’s choice of these kinds of traits allowed him to see experimentally that the traits were not blended in the offspring as would have been expected at the time, but that they were inherited as distinct traits. In 1868, Mendel became abbot of the monastery and exchanged his scientific pursuits for his pastoral duties. He was not recognized for his extraordinary scientific contributions during his lifetime; in fact, it was not until 1900 that his work was rediscovered, reproduced, and revitalized by scientists on the brink of discovering the chromosomal basis of heredity.
