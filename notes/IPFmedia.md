# Matt Hunninghake meeting

## dec 9 900 am

David Bateds cheikf of medical brigham

allergies | adam right | conditions in EHR | 

* Ann K award
* pubmed papers | IPF is teh most common ILD | connective tissue disses | scleroderma most common 
* all pulmonary fibrsos may be common syndrom  | scleroderma | How connected is it?
* K award ? Would be to see if she can test your algorithm in scleroderma patients
* techniques learn

---


# Bhavika Kaul meeting 

## Nov 16 3.00 PM


ILD  .. early dx in VA

only pulmologist in the VA. 
VA population age?

10 M vets a year nationally, largest integrated system backing to 1990

---

ILD.  

## VA Corporate Data warehouse

+ case definitions doen precisely
+ agent orange exposure
+ Biden signed 200B ILD service connected disorder

+ integerate the VA better
+ imaging data

----

disease severity
PFT, oxygen use, CT scan, percentage of fibrosis

disease would be caught.





















# NIH IPF Stakeholder Summit





+ Anna podolanczuk
+ David Schwartz
+ Ivan Rosas: Moderator
+ PFF Ambassador Mark McCormick

* identifying oatients before ILD helps to find a cure or prevent IPF development
* start using new diagnostic definitions might be very useful to identify patients and better charecrize the disease
* david schwartz.. screening can be better
* mark also pointed out the gaps in diagnostic workflows
* there are treatments for early IPF
* pre-clinical IPF 25% prevalence (david schwatrz)
* psychological impact might not be that important
* minimally complex genetic disease

-----
Morning everyone. Let me begin by saying I am excited to be part of this summit, and it has been an aboslutely fascinating learning experience. A huge thanks to Fernando and Sydney for inviting me, and alos to the 3 lakes foundation and PFF and NHLBI for making this happen. 

So what I am going to talk about is our recent results on the possibility of accelerating the diagnostic odessey for patients to reach a aignosis, and may maybe avoid or at least the odds of the delays that patients like Mark sometimes encounter. IPF is of course is very bad disease to have with interventions that well, as we have heard, are increasingly promising, but not perfect. And we have heard that it can be hard to diagnose the disorder, symptoms are non-specific, shortness of breath, dry cough, unless you can hear the crackles. And it is sort of rare, ILD about 10 of 10,000, ipf 5 of 10,000, But over 200,000 people are living now with IPF, and postDX survival is about 4-5 years. 

55% get at least one misdiagnoses, more than 38% two or more misdiagnoses, and often confused with age.  often confused with asthma, pnenomia, bronchitis, allergies , COPD, and simple CXR might not be conclusive. And on top of that, particualrly due to the workload of teh PCPs, signs are missed, leading to delayed and missed diagnosis

What we were able to do is look at EHR records and potentially faise a flag for a predicted future diagnosis by 4 years  before diagnosis in current practice. It is retrospective data. We are saying that we can raise a reliable flag that a patient will be diagnosed with ILD and even more precisely IPF 4 years before the point where one currentlyu gets a diagnosis.

And we are able to do this by lookinhg at comorbidity footprints. It was increadibly interesting to listen to David Shwartz talk about yesteday how IPF is a minimally complex diease from genomic perspective, which is unchracrestic of a complex disease, Nevertheless, what we found that is that there are indeeed subtle comorbidtiu, patterns in past medical encounter data that signals a future diagnosis. Impportantly this is a characteristic of  a compelx disease, it leasves footprints in how seemengly unrelated disorders occur in teh past, including cardiovascular issues, infections, immunoilogical disoders and so on. And we do not know a priori about all these patterns, and presently teh only way to leverag them is to learm them from giant datasets. Thats what we did.

A couple of points here. Most AI that are used in general in mediccal dx, and particualrly in IPF/ILD context, uses ML to analyze imaging data. So basically look at the same information that a physician or radiologist would loo at, and hope to do better. At that point, you are modeling the physician and not teh disease. Whenw we look at comordbidities, particulalrly only through how different medical counters happen in individual medical history of patients, we are looking at an underutilized diagnostic modality... complementary to what physicians focus on. 

The other important point is how we setup the problem. We only raise these flags with data that a pteints has, when he/she walks in to the primary care clinic in their files.../ no new tests, no imaging, no pulmonary function tests, no genomic tests... so basically teh question, what can we say when the PCP has not yet suspected any ILD or IPF. 

We set up a case control scenario where we identify the cases using adminsitrative records.. ICD9/10 codes . We look at 2 years of past data, and atempt to make a diagnosis one to 4 years in future. We define the control cohort as one that have no idication of ILD or IPFs at least upto 2 years in future from where the ZCOR evaluation is being done. Most results I am going to present refers to when we make predictions 1 year in the future, ie our prediction are being made 1 year before teh current medical diagnosis.

We use the standard codes for IPF and broadly ILD. We analyze the two scenarios separate;y.. can we raise flags for ILD, and and can we raise flags for IPF. Now there are objections often to using admin coides for idemtifuying cases,And we also investigate what happends if we do a cmore comolex case identifcation approacg.. maybe use the two drusg perfinidone or ofab along with admin codes corresponding to PF, or look for the diganostic fingerprint that typically would be there before an IPF dx. And our results remain unchanged for each of those categoriers.

Here is the data: Teh marketscan data have over 100M patients, and some mmdicare data. We also use dat afrom UCm and Optumlabs.. total 2.9M patienst with over 50K cases

Results. For one yaer in future predictions, we get close to 90% auc, which was urprising to us and pretty incredicble. VAnd the performnce not only is high in teh general population, but reamins comparable when we look ta subcohosrst, People who have COPD, or heart condition, or asthma, have no identifibale high risk factors and acros the three independent databases.

And we get likelihood ratios that go over 30 or 40 at 99% specificity. And as we tary to predict or raise flags earlier than 1 year, we do a bit worse, but our predictions hold up pretty well.

More detailed results. Noet that ILD has twice the prevalence of IPF, and the PPV remains pretty much the same, but the likelihood ratio roughly doubles. Wjhat this means is that we pretty much are equally cabale of picjking up ILDs and IPFs.

All the diagnoss that contributes to risk. This howveer is only teh tip of teh iceberg, the patterns we find arte not representable at simpley risk factors. But nevrtheless, we can ask how different dx on average modulayte teh risk. And we find Resporatory circulatory, ill-defined ysmptoms.

Is it agood idea to screen? David Schartwz already made teh case. Yes. What about false positives, we get about 1 positive for everu 2-30 flags. Questions on Healthcare capacity, and risk for imaging which minimal. There is also teh ethics question of 
notifying pataients years earlier. But what we showe that we can perhaps offer a different cheaper fastyer apprach to identify the Precliniucal IPF or ILD patienst that David Schawartz was ytlajking about.

Deplaoy as an epic app, to sealmelessly work with epic. Measure outcomes when deployed. ANd maybe add other modlaities and get top ZCOR 2.0 so maybe become useful at teh secondary centers as well.



---

# One line:

Predictive screening of IPF upto 4 years before diagnosis by current medical practice

## abstract lay

Using nearly 3 million patients from three independent patient databases, we uncovered
predictive comorbidity signatures in past 2 years of individual history of medical encounters to reliably flag  patients who go on to get a clinical diagnosis for IPF in future. The algorithm is demonstrated to make clinically useful predictions upto 4 years in future, and when applied 1 year before diagnosis we achieve out-of-sample positive likelihood ratios exceeding 30 at 99% specificity.  IPF, being a relatively rare disease (< 5 in 10,000), poses challenges to statistical characterization, and we developed new EHR processing tools to distill the subtle predictive signatures. We showed that longitudinal signals are important, and off-the-shelf deep learning tools tend to be less robust, especially when we move from one database to another without retraining. These results demonstrate the crucial role machine learning/AI can play in diagnosis of rare diseases, and that patterns buried in the medical histories can be effectively exploited to substantially improve patient outcomes.



## Point of care deployment:

ZCoR-IPF works noninvasively, inexpensively and almost instantaneously, relying only on diagnostic data already in the participant’s electronic medical record, and thus can run on existing information technology infrastructure.  ZCoR-IPF supplements information currently used to diagnose IPF, namely, respiratory signs and symptoms, pulmonary function and the radiographic and histologic appearance of the lung, reflecting a sophisticated, highly detailed automated analysis of comorbidities, considering more than 667 features related to the incidence and timing of individual diagnostic codes.


Our central claim in this study is the potential utility of ZCoR-IPF as a screening tool in the primary care setting, one that is deployable with little or no additional resources, thus improving delayed and missed diagnosis rates. Importantly, the goal of ZCoR-IPF in this setting is to flag participants for detailed diagnostic evaluation, and not to deliver a final diagnosis by itself.


Thus, ZCoR-IPF can aid primary care physicians to more selectively flag participants for referral for HRCT or to a pulmonologist. Presently, only high-risk participants are flagged, that is, participants with one or more of chronic dyspnea, chronic cough and/or chronic ‘Velcro crackles’ on auscultation, restrictive ventilatory patterns on pulmonary function tests or incidental ILAs or ILD on chest or abdominal CT.


Additionally, ZCoR-IPF can serve as a diagnostic aid for pulmonologists, radiologists, pathologists or multidisciplinary teams in cases showing abnormalities suggestive of, or associated with IPF, but not UIP on HRCT or histopathology.


## abstract results:

1. ZCoR-IPF was trained on a national insurance claims database and validated on three independent databases (Marketscan, UChicago Medicine hospital, Mayo Clinic), comprising a total of 2,983,215 participants, with 54,247 positive cases. The algorithm achieved positive likelihood ratios greater than 30 at a specificity of 0.99 across different cohorts, for both sexes, and for participants with different risk states and history of confounding diseases. The area under the receiver-operating characteristic curve for ZCoR-IPF in predicting IPF exceeded 0.88 and was approximately 0.84 at 1 and 4 years before a conventional diagnosis, respectively. 

2. ZCoR-IPF is demonstrated to have robust out-of-sample performance, allowing (1) accurate out-of-sample predictions for a future IPF diagnosis via leveraging subtle comorbidity patterns recorded in individual histories, (2) maintenance of high predictive performance for diagnosis further out, up to 4 years in future, and (3) common confounders to have little or no effect, such as a preexisting diagnosis of COPD, asthma or heart disease or the absence of any indication of dyspnea in the past. 

3. ZCoR-IPF outperforms baseline predictors and state-of-the-art neural network (NN) or deep learning architectures trained in the same manner as ZCoR-IPF

4. We concluded that past respiratory disorders maximally contribute to the risk, followed by suspected IPF comorbidities, metabolic diseases, cardiovascular abnormalities and diseases of the eye. Infections also featured in the top 20 comorbidities. Importantly, despite some differences, the overall pattern of the importance ranking remained substantially invariant across the sexes.



# Reddit:

ZCoR-IPF: Predictive screening of Idiopathic Pulmonary Fibrosis (IPF) upto 4 years before diagnosis by current medical practice

Using nearly 3 million patients from three independent patient databases, we uncovered
predictive comorbidity signatures in past 2 years of individual history of medical encounters to reliably flag  patients who go on to get a clinical diagnosis for IPF in future. The algorithm is demonstrated to make clinically useful predictions upto 4 years in future, and when applied 1 year before diagnosis we achieve out-of-sample positive likelihood ratios exceeding 30 at 99% specificity.  IPF, being a relatively rare disease (< 5 in 10,000), poses challenges to statistical characterization, and we developed new EHR processing tools to distill the subtle predictive signatures. We showed that longitudinal signals are important, and off-the-shelf deep learning tools tend to be less robust, especially when we move from one database to another without retraining. These results demonstrate the crucial role machine learning/AI can play in diagnosis of rare diseases, and that patterns buried in the medical histories can be effectively exploited to substantially improve patient outcomes.

ZCoR-IPF works noninvasively, inexpensively and almost instantaneously, relying only on diagnostic data already in the participant’s electronic medical record, and thus can run on existing information technology infrastructure.  ZCoR-IPF supplements information currently used to diagnose IPF, namely, respiratory signs and symptoms, pulmonary function and the radiographic and histologic appearance of the lung, reflecting a sophisticated, highly detailed automated analysis of comorbidities, considering more than 667 features related to the incidence and timing of individual diagnostic codes.

Our central claim in this study is the potential utility of ZCoR-IPF as a screening tool in the primary care setting, one that is deployable with little or no additional resources, thus improving delayed and missed diagnosis rates. Importantly, the goal of ZCoR-IPF in this setting is to flag participants for detailed diagnostic evaluation, and not to deliver a final diagnosis by itself. Thus, ZCoR-IPF can aid primary care physicians to more selectively flag participants for referral for HRCT or to a pulmonologist. Presently, only high-risk participants are flagged, that is, participants with one or more of chronic dyspnea, chronic cough and/or chronic ‘Velcro crackles’ on auscultation, restrictive ventilatory patterns on pulmonary function tests or incidental ILAs or ILD on chest or abdominal CT.

Additionally, ZCoR-IPF can serve as a diagnostic aid for pulmonologists, radiologists, pathologists or multidisciplinary teams in cases showing abnormalities suggestive of, or associated with IPF, but not UIP on HRCT or histopathology.

https://www.nature.com/articles/s41591-022-02010-y


# Linkedin:

ZCoR-IPF: Predictive screening of IPF upto 4 years before diagnosis by current medical practice

Using nearly 3 million patients from three independent patient databases, we uncovered
predictive comorbidity signatures in past 2 years of individual history of medical encounters to reliably flag  patients who go on to get a clinical diagnosis for IPF in future. The algorithm is demonstrated to make clinically useful predictions upto 4 years in future, and when applied 1 year before diagnosis we achieve out-of-sample positive likelihood ratios exceeding 30 at 99% specificity.  IPF, being a relatively rare disease (< 5 in 10,000), poses challenges to statistical characterization, and we developed new EHR processing tools to distill the subtle predictive signatures. We showed that longitudinal signals are important, and off-the-shelf deep learning tools tend to be less robust, especially when we move from one database to another without retraining. These results demonstrate the crucial role machine learning/AI can play in diagnosis of rare diseases, and that patterns buried in the medical histories can be effectively exploited to substantially improve patient outcomes.

ZCoR-IPF works noninvasively, inexpensively and almost instantaneously, relying only on diagnostic data already in the participant’s electronic medical record, and thus can run on existing information technology infrastructure.  ZCoR-IPF supplements information currently used to diagnose IPF, namely, respiratory signs and symptoms, pulmonary function and the radiographic and histologic appearance of the lung, reflecting a sophisticated, highly detailed automated analysis of comorbidities, considering more than 667 features related to the incidence and timing of individual diagnostic codes.

Our central claim in this study is the potential utility of ZCoR-IPF as a screening tool in the primary care setting, one that is deployable with little or no additional resources, thus improving delayed and missed diagnosis rates. Importantly, the goal of ZCoR-IPF in this setting is to flag participants for detailed diagnostic evaluation, and not to deliver a final diagnosis by itself. Thus, ZCoR-IPF can aid primary care physicians to more selectively flag participants for referral for HRCT or to a pulmonologist. Presently, only high-risk participants are flagged, that is, participants with one or more of chronic dyspnea, chronic cough and/or chronic ‘Velcro crackles’ on auscultation, restrictive ventilatory patterns on pulmonary function tests or incidental ILAs or ILD on chest or abdominal CT.

Additionally, ZCoR-IPF can serve as a diagnostic aid for pulmonologists, radiologists, pathologists or multidisciplinary teams in cases showing abnormalities suggestive of, or associated with IPF, but not UIP on HRCT or histopathology.

Results:

ZCoR-IPF was trained on a national insurance claims database and validated on three independent databases (Marketscan, UChicago Medicine hospital, Mayo Clinic), comprising a total of 2,983,215 participants, with 54,247 positive cases. The algorithm achieved positive likelihood ratios greater than 30 at a specificity of 0.99 across different cohorts, for both sexes, and for participants with different risk states and history of confounding diseases. The area under the receiver-operating characteristic curve for ZCoR-IPF in predicting IPF exceeded 0.88 and was approximately 0.84 at 1 and 4 years before a conventional diagnosis, respectively. 

ZCoR-IPF is demonstrated to have robust out-of-sample performance, allowing (1) accurate out-of-sample predictions for a future IPF diagnosis via leveraging subtle comorbidity patterns recorded in individual histories, (2) maintenance of high predictive performance for diagnosis further out, up to 4 years in future, and (3) common confounders to have little or no effect, such as a preexisting diagnosis of COPD, asthma or heart disease or the absence of any indication of dyspnea in the past. 

ZCoR-IPF outperforms baseline predictors and state-of-the-art neural network (NN) or deep learning architectures trained in the same manner as ZCoR-IPF

We concluded that past respiratory disorders maximally contribute to the risk, followed by suspected IPF comorbidities, metabolic diseases, cardiovascular abnormalities and diseases of the eye. Infections also featured in the top 20 comorbidities. Importantly, despite some differences, the overall pattern of the importance ranking remained substantially invariant across the sexes.


https://www.nature.com/articles/s41591-022-02010-y


![f1](../uploads/infographic.png)

--- 

![f1](../uploads/f1.webp)

--- 

![f1](../uploads/f2.webp)

--- 

![f1](../uploads/f3.webp)

--- 
![f1](../uploads/f4.webp)











