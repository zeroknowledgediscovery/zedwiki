# Cook County Commision on Social Innovation

Thanbk you for this opportunity to talk to the Cook County Commission on Social Innovation.
A big thanks to Marc for making this happen.
I am Ishanu Chattopadhyay, and that was a very nice introduction.
What I plan to talk about today is how I feel
AI , machine learning and data science can inform polcy makers, and help choose between
competing decisions, maybe where before one had to simply follow their gut, we can 
bring in some data-driven insight. How we can leverage data and all these facncy algorithms that we are 
coming up with, to make lives better. 

Now crime is a problem, no just in Chicago, or Us. It is one of the leading causes of death in 
younger people all over the world. And teh sdtatistics in Cook County is not great. 

Can algorithms, artificial Intelligence, and access to vast amounts of data help?

ANytime we talk about crime, enforcement and prediction, we are reminded that this has been tried before,with
less than stellar results. Has not worked weell, has propgated biases, and has has pushback from communities everywhere.
Is what I am talking about any different?

Yes

First, the paper which atsrted this conversation, is not about simply predicting crime
It is about creating a digital twin of the social system of crime and enforcement.







# Q&A

**Links**

+ https://rdcu.be/cQJwi
+ https://www.nature.com/articles/s41562-022-01372-0/metrics
+ https://zed.uchicago.edu/data/pub_drafts_//PAI/crime_chattopadhyay.pdf
+ https://zed.uchicago.edu/data/pub_drafts_//PAI/fractal_net.pdf

--

## How does your approach differs from earlier attempts at crime prediction?
Existing approaches often attempt to model the dynamics of crime as being driven by hotposts. It's like assuming that crime spreads across an environment like a drop of ink in water, slowly diffusing out from places that experience elevated event rates (the hotspots). This has not proven very successful. Other approaches have tried to find similarities to earthquakes -- how one typically expects a series of “aftershocks” after, and “foreshocks” preceding a big event. Still others have thrown the kitchen-sink of standard machine learning models (deep learning etc) to the problem, using features that range from weather information to the presence of graffiti on nearby walls. While some of these approaches have better-than-random predictive performance, they are often not actionable (the events not predicted sufficiently early or the predicted location not small enough to be of any practical use). 

Our approach is fundamentally different. We came up with a new learning architecture that does NOT assume that crime diffuses out like ink in water, and recognizes that there is an underlying connectivity in a social environment that implies that events occurring in different parts of the city may be constraining and influencing each other. We back out these hidden dependencies from purely historical event logs (what happened, where it happened, when it happened), and use this structure to predict future events. We LEARN patterns from history that have been associated with elevated crime, and project these patterns into the future to make precise predictions.

## Can you explain what AUC means, and what an AUC of, say, 90 percent means?
The AUC or the Area under the Receiver Operator Characteristic curve is the area under the curve described by plotting the trade-off between the false positive rate (1 - specificity) and the true positive rate, also known as sensitivity or recall. That might be hard to understand. Another interpretation of the AUC is that it is the probability that a location that actually experiences an event is evaluated to have a higher risk compared to a location that does not experience a crime. An AUC of close to 90% implies that we can simultaneously have a high sensitivity and a high specificity, i.e. we can have very low false alarms and a small number of missed alarms. 

## You write "our approach is free from manual encoding and thus resistant to the implicit biases of the modelers themselves". Can you explain what this means? But the tool could still be abused?
Often machine learning algorithms need “features” as inputs, which are determined by data science or domain experts -- humans. For example, in the Chicago PD’s attempt to put together a list of potential victims or perpetrators of gun violence, they used an equation to evaluate if an individual should be on the list. The inputs to the equation (the features) were age, arrest history etc. But this is problematic, since many of these variables overlap with demographic characteristics due complex socio-economics of the urban social structure. And such a manual determination of “what is important” biases the inputs and hence ultimately the outputs. We need no such manual curation or a priori determination of features; our algorithm processes the raw event logs directly. Noone is sitting down to determine what is or is not important, it is all inferred from the emergent patterns.

However, that does not mean we have eliminated potential bias. The data (the event logs) might have bias built in, e.g., over-policing disadvantaged communities will falsely elevate relative crime rate, and the inference algorithm will not be able to  tell. So we have to be careful how this, and such similar tools, are used. We must leverage this technology to help communities, to recognize biases where they exist, and move towards a better society; not flood disadvantaged communities with more enforcement.

## Your tool isn't just a way to predict crime, but can also be used to evaluate police response, correct? Do you worry that it will just be used for the first, and not the second purpose?
Indeed there is that risk. And we do worry about that, which is why we have been very clear and vocal that using these tools simply to further state surveillance is not appropriate. However, the inescapable reality is that AI is here to stay, and its impact on our daily lives is only going to increase. We must ensure that this technological revolution does not lead us to dystopia. Democratizing this incredible power, so that it works for and not against the people is key. And this approach is a small step in this direction.

## Of course, something that's top of mind at the moment is mass shootings in the US. Can tools like these help prevent those?
Maybe, but probably not. Although note that this is a statistical tool, and more importantly it still does not predict event severity. So it cannot distinguish between a mass shooting and a random case of gang violence. Also, the algorithm derives its predictive power from historical patterns of event logs, and it is nearly impossible to predict actions that are truly random.

## What is AI or ML?
Artificial intelligence and machine learning, in the current context, refers to a collection of mathematical models and statistical inference tools to discover patterns in data, to make automated decisions, or prediction or forecasts. AI can also refer to that what aims to mimic human intelligence, but it might be more useful to have capability that is complementary to or even surpasses humans. 

## How does the algorithm work?
We discover patterns in event logs, and apply  these patterns  to calculate risk of an event in future at specific locations. It is like if you see dark clouds, you conclude that it is going to rain soon; just here the patterns (the dark clouds) are much more subtle, and harder to recognize and reason with.


## How close or far they are from actually impacting our readers. With that in mind, I wondered if you might have a little advice for how I can position your story? 

This is a very good question. In recent coverage, some articles have likened our work, perhaps in jest, to real-life minority report. I would suggest not taking that position, since we do not focus on predicting individual behavior, and do not suggest that anyone be charged with a crime that they didn't commit, or be incarcerated for that. Our model learns from, and then predicts,  event patterns in the urban space, e.g., predicting that within a two block radius around the intersection of 67th st and SW avenue, there is a high risk of a homicide a week from now. It does not indicate who is going to be the victim or the perpetrator. The predictions also have quantified uncertainties (Chicago: accuracy 93%, area under ROC curve 87% etc.), but are precise enough to be actionable.

This capability is then used to probe into how this complex social system responds to different kinds of perturbations, such as increasing or decreasing crime rates in different parts of a city. We found that when stressed, the law enforcement response is seemingly different in high socio-economic-status areas compared to their more disadvantaged neighboring communities. It is suggested in the paper, that when crime rates spike, the higher SES neighborhoods tend to get more attention at the cost of resources drawn away from poorer neighborhoods. This ability to recognize bias can be used as a new tool for policy making, and optimizing resource allocation decisions. We also suggest that we must be careful as to what unintended consequences of such predictive technologies might be if deployed as merely a “predictive policing” tool. 


## Where will your work go next, and could it be used at any point to understand and even prevent crimes? Is this technology so new that it will be decades before it is refined, or could we see benefits in the next few years?

This technology is new, but police departments particularly in the US have been trying to use AI based tools for some time. However, we are being cautious on deployment given the many many unintended consequences that such technology might have. But the tool itself is pretty complete and can be deployed quickly. We are putting together the best avenue for that, but we might see some deployments of this tool within a year.

## Predictive policing algorithms often provoke concerns about profiling – particularly racial profiling. Although you highlight bias issues in the paper, I see the research has already prompted some concerns on social media and elsewhere – can you explain simply how this risk has been accounted for and mitigated? Why do you think the algorithm is less risky than previous examples we have seen?

A very detailed comparison and exposition of this point is done here: https://link.medium.com/oiImwzZ1irb 
Note, machine learning algorithms often need “features” as inputs, which are determined by data science or domain experts -- humans. For example, in the Chicago PD’s attempt to put together a list of potential victims or perpetrators of gun violence, they used an equation to evaluate if an individual should be on the list. The inputs to the equation (the features) were age, arrest history etc. But this is problematic, since many of these variables overlap with demographic characteristics due complex socio-economics of the urban social structure. And such a manual determination of “what is important” biases the inputs and hence ultimately the outputs. We need no such manual curation or a priori determination of features; our algorithm processes the raw event logs directly. Noone is sitting down to determine what is or is not important, it is all inferred from the emergent patterns.

However, that does not mean we have eliminated potential bias. The data (the event logs) might have bias built in, e.g., over-policing disadvantaged communities will falsely elevate relative crime rate, and the inference algorithm will not be able to  tell. So we have to be careful how this, and such similar tools, are used. We must leverage this technology to help communities, to recognize biases where they exist, and move towards a better society; not flood disadvantaged communities with more enforcement.


## How soon would cities/police forces potentially be able to use such an algorithm?

See before 

## Is there anything else you’d like to get across to city leaders about your research?

Using AI to empower optimal decision/policy making is the future, particularly where we need to balance compassionate enforcement, greater engagement with communities, and optimal and equitable access to justice and societal resources.

## Can we prevent mass shootings

Good question. It is much harder to predict events that are truly random, in the sense that past violent crimes do not modulate risk of future events, which might be the case for these mass shooting incidents. One popular theory for such incidents seem to be mental health issues coupled with access to firearms. 

## There are concerns that such application can deepen biases between people, push the police to make false decisions. Do you agree with those concerns?
It is true that predictive policing approaches in the past have has less than stellar performance, and have been accused of perpetuating systemic biases. A very detailed comparison and exposition of this point is done here: https://link.medium.com/oiImwzZ1irb 
Note, machine learning algorithms often need “features” as inputs, which are determined by data science or domain experts -- humans. For example, in the Chicago PD’s attempt to put together a list of potential victims or perpetrators of gun violence, they used an equation to evaluate if an individual should be on the list. The inputs to the equation (the features) were age, arrest history etc. But this is problematic, since many of these variables overlap with demographic characteristics due complex socio-economics of the urban social structure. And such a manual determination of “what is important” biases the inputs and hence ultimately the outputs. We need no such manual curation or a priori determination of features; our algorithm processes the raw event logs directly. Noone is sitting down to determine what is or is not important, it is all inferred from the emergent patterns. Additionally, the algorithm does NOT predict or suggest individuals as potential perpetrators or victims -- the predictions are made for spatial locations (approx 2 city blocks), and thus cannot be used to preemptively inacrecrate people or anything like that. 

However, that does not mean we have eliminated potential bias. The data (the event logs) might have bias built in, e.g., over-policing disadvantaged communities will falsely elevate relative crime rate, and the inference algorithm will not be able to  tell. So we have to be careful how this, and such similar tools, are used. We must leverage this technology to help communities, to recognize biases where they exist, and move towards a better society; not flood disadvantaged communities with more enforcement.
 
## What should be done to make the algorhitm safe, not to be used in unproper way, not to hurt or misjudge any group of people?
 
The algorithm does not make predictions on people, it makes predictions on event dynamics. This is a key difference. It is conceivable that even such predictions can be used to over-police certain communities, but that is not the intent of the study, and our goal is not to realize the tool as yet another mere predictive policing approach.
 
## I wonder what else can such algorithms predict, for example in medicine or other aspects of our lives in the future?
This is a general algorithm for predicting rare event dynamics, in systems with thousands to tens of thousands of co-evolving variables, where the variables have non-trivial emergent cross-dependencies. Thus, extreme weather events, seismic phenomena, or geo-political events are examples which may be predictable in this framework, and we are continuing to work in those directions.

## How do you think, in what ways will such algorithms change our life, our society? Could you give any examples so we can imagine what else could AI applications predict in the future besides hurricanes or earthquakes?
AI/Machine learning is emerging as a pervasive tool that is redefining how we do science, and is and will continue to shape all aspects of human life. We expect dramatic improvements in healthcare, and how we interact with the environment and each other. Done right, AI can help us solve some of the defining challenges of our time - optimizing agriculture to address the looming food crisis, help realize the next generation of energy sources and optimize energy management to mitigate climate change, find cures for complex diseases, and preempt pandemics. However, with the promise of a lot of potential good, there is also the risk of erosion of individual freedoms, and the ability of states to wield unprecedented power and control over its citizens. Democratizing this incredible power, so that it works for and not against the people is key. And this approach is a small step in this direction. 
 
## Tell us about you and the team who found the AI 

This study is based on research conducted at the University of Chicago, by myself as the 
Principal investigator, and my collaborator Professor James Evans, who is a computational social scientist. My background  is in AI, machine learning and data science. The data used in learning the models is in the public domain. Other co-authors in the study (V. Rotaru, Y. Wen and T. Li) are my former students and postdoctoral associates, who helped design and implement the software, as well as work out some of the mathematical structure of the underlying architecture.

## How did you come up with the idea and why?

This tool is an application of my work in the broader area of predicting and modeling rare and extreme event dynamics in complex systems. This is one of the core areas of research in my group. 


##  Please describe it in a simple way for our readers.
We discover patterns in event logs, and apply  these patterns  to calculate risk of an event in future at specific locations. It is like if you see dark clouds, you conclude that it is going to rain soon; just here the patterns (the dark clouds) are much more subtle, and harder to recognize and reason with.

In particular, we analyzed historical event logs going back 3 to 5 years, distilled predictive patterns, and assembled these patterns into a model that can then make predictions about future events. 

We do not focus on predicting individual behavior, and do not suggest that anyone be charged with a crime that they didn't commit, or be incarcerated for that. Our model learns from, and then predicts,  event patterns in the urban space, e.g., predicting that within a two block radius around the intersection of 67th st and SW avenue, there is a high risk of a homicide a week from now. It does not indicate who is going to be the victim or the perpetrator. The predictions also have quantified uncertainties (Chicago: accuracy 93%, area under ROC curve 87% etc.), but are precise enough to be actionable.

This capability is then used to probe into how this complex social system responds to different kinds of perturbations, such as increasing or decreasing crime rates in different parts of a city. We found that when stressed, the law enforcement response is seemingly different in high socio-economic-status areas compared to their more disadvantaged neighboring communities. It is suggested in the paper, that when crime rates spike, the higher SES neighborhoods tend to get more attention at the cost of resources drawn away from poorer neighborhoods. This ability to recognize bias can be used as a new tool for policy making, and optimizing resource allocation decisions. We also suggest that we must be careful as to what unintended consequences of such predictive technologies might be if deployed as merely a “predictive policing” tool. 



## Is there a chance you would share your discovery in the Middle East? 

The algorithm is open source, so yes, one of my goal is to see maximum impact, and would be happy to share with interested parties.
