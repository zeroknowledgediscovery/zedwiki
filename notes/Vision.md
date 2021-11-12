Thank you for being here, and participating in this process. I have broad research intersts, which is  challneging to talk  about in 15 minutes. Hence I will stick to my broad vision, what I set out to achieve, where I am  in that path (results), and where I intend to go in future. 

# Vision

3. I am interested in getting actionable knowledge from data, particularly in domains where the underlying physics, biology or pathlobiology might not be completely understood yet. Examples might be: predicting case counts in a pandemic, or predicting future mutations and emergence of new pathogens, forecasting when and where for crime in cities, estimating future risk fo complex diseases.

6. I am interested in getting actionable insights in complex systems, that help clinical decisions, accelerate science and distill new theory.

# Journey 

7. In the journey so far, I have identified/developed **three** core ideas or building blocks or algorithmic principles, that then spawn solutions to diverse problems. With significant funding I have procured, I have an dma pursuing these diurection that I am going to talk about in a moment. 

8. Briefly these three distinct building bloack s are a new approach to EHR analytics, the Q-Net framework, and fundamentally new approaches to stochastic time series modeling.

# People 

10. These are all the associates an dstudents I have worked with. Yi and Nick are my postdocs (Yi just left for BNL, both are math PhDs), and teh rest are graduate or UG students in CS and math. 
11. Here are my collaborators across the campus and beyond. And showing the diversity of applications and problems I have worked on, here are all the home departments of my collaborators outside medicine. psychiatry, pediatrics, cardiology,  pulomonary care, statistics, PME, social sciences. 

# EHR

13. Lets talk about the first category of problems: diagnosis and screening of complex diseases with electronics health records. I designed a new approach to leverage comorbidities effectively and accurately estimate the future risk of a disease, I call these deisease specific estimates xCoR, where x specifies the disease. 

14. 15. Universality. The dieases we have considered so far incluse; These are with teh exception of ASDD are fatal diseases with no good screening tool that may be administerd in primary care, leading to missed and late diagnoses. All serious dieases have co-morbidities, they generate fingerprints in our medical histories. Can we use teh vast patianet history data that we have access now, to find and use these patterns?

16. Conventional ML -- which aims to mimic the physician -- will not do. For these diseases we dont not know enough of the pathobiology to pre-specifiy all risk factors, instead we leverage underutilized diagnostic moadlities -- complex historical patterns -- to complement the physician's experinece.
17. ASD: problem is delayed diagnosis which delays interventions
18. We know children with autism have higher rates of many diseases. But the hetergenity of autism makes it non-trivial to naively use these patterns. 
19. Our approach cuts down teh false posituves by half
20. And here is teh ROC, and this is the state of teh art screening.
21. And we get to close to 90% AUC at 4 years.
22. This is the inferred comorbidity spectra..  showing how individual diagnoses module autism risk. 
23. How does this work? we infer generative models of stochastic proceses that drive the diagnostic histories, making possible to leverage longitudinal effects beyond just binary presensce/absense of risk factors.
24. here is an example of PFSA
25. The algorithm uses 100s of such models pairs to intrenally respresent how the diagnosis patterns differe between the control and the treatment sets. 
26. BP, we aim to predict if a patient with depression will experience a manic switch. 
30. IPF. 3-5 years survival post-diagnosis. We get AUCs approaching 88%, and can boost survival from ~100 weeks to >200 weeks on average, due to earlier diagnosis. Disease modifying drugs exist now, so this can be a big deal.
31. ADRD. 67% to 87%. And we can predict AD diagnosis upto a decade in future. 
36. Teh list if disorders we can target are expanding every week, e.g. cardiac risk in perioperative HK surgery, we estimate the adoption of our tool can save ~10K lives over teh next 20 years.
37. prospective trails under way right now
38. new approach to univreal screening across teh human diease soectrum

# QNET 


39. QNet Architecture: originally developed to predict evolutionary trajectories of emerging viruses. But is actually a general framework to model complex multi-variate systems.
40. How do we compute distance between strains.. edit distance or the number of mutations they are apart do not refelect biology. The Qnet allows us to infere dependencies between mutations, and induces a biology aware distance metric the qdistance, which adapts to teh organism, the evolutionary processes, the selection pressures etc. Using the qdistanec we can estimate if two sequences are close: in teh sense if one is likely to jump to another in teh wild. 
41. example of qnet construction
43. example that we can indeed predict fututre muations. We outperform WHO in 98% of next-flu-season strain prediction over the past 20 years.
44. And it works in experiment as well (Aaron's lab)
45. Future: NORAD for Biological/pandemic threats
46. As I said Qnets are applicable to any complexc multi-varauate systems, and the othetr application I am looking into wit Erika Claud is gut microbiome modeling .
47. Model ecosystem evolution, and forecast in individual infants how their microbiome evolves, and matures.
48. And we are immesely successful, as you can see.
49. Future, map to disease states, and optimize interventions for microbiome tuning.
50. Application to belief shifts
51. examples
52. Renditon of opinions in society over time, each dot is an opinion vectyor, and closer dots can change (jump) to one another, far apart dots are mch less likely to.
53. Predict responses to unaswered questions from patial data. 
54. Social experiment (collab with James Evans) to validate
55. Also since we can predict responses, this opens up other possibilioties.. an algoithmic lie detector. We can tell if someone;s responses are consistent with their past responses using the complex inferred models, and is impossible to cheat. 

# Time Series 


56. New approach to modeling stochastic phenomena. One application is using past flu incidence data to predeict COVID case count.
58. And in teh CDC backed forecast hub, we beat everyone with our algorithm, including stanford, mit, columbia, LANL .
59. SImialr underlying principles allow us to model rare and extreem pehnomnea, which is challenging even for state of teh art ML, including extereme weather evenst, earthqaukes, crime.
60. without going into details, this capability arises from identifying emergent self-simialrities in stoichasti system that produces compact models (order of magnitude smaller that deep learning frameworks, leading to superior predictive performance)
61. In crime, particualrly, we can also use our generative models to look for enforecemnt bias. So the predictive ability both empowres the state, and opens up new ways to audit effect of state policy decisions.
62. We would have won in 119 out of 120 categories.
63. few mathematical insights to diver applications with nontrial impact.

# Future

