# commentary on article

Associations Between Natural Language Processing Enriched Social Determinants of Health and Suicide Death among US Veterans


## structure data?

structured data (using ICD codes,
206and VHA stop codes, details in Appendix 2).

## point

SDOH are risk factors for suicide among the US Veterans and NLP can be leveraged to extract
56SDOH information from unstructured data.

6,122,785 Veterans who received care in the US VHA between October 1, 2010, and
September 30, 2015.

Nested case-control study. Data was analyzed in May 2022

EHR data from 1,185 healthcare facilities under the US Veterans Health Administration (VHA)

Occurrence of SDOH over a maximum span of two years compared with no occurrence of
SDOH.


Cases of suicide deaths were matched with 4 controls on birth year,
cohort entry date, sex, and duration of follow-up. Suicide was ascertained by National Death Index and
patients were followed-up up to 2 years after cohort entry with a study end date of September 30, 2015.


Of 6,122,785 Veterans, 8,821 committed suicide during 23,725,382 person-years of follow-up
(incidence rate 37.18 per 100,000 person-years). Our cohort was mostly male (92.23%) and white
(76.99%). Across the six common SDOH as covariates, NLP-extracted SDOH, on average, retained 48.26%
of structured SDOH and covered 84.38% of all SDOH occurrences. All SDOH occurrences, measured by
structured data and NLP, were significantly associated with increased risk of suicide. The three SDOH
with the largest effects were ‘legal problems’ (aOR=2.67, 95% CI=2.46-2.89), ‘violence’ (aOR=2.26, 95%
CI=2.11-2.43) and ‘non-specific psychosocial needs’ (aOR=2.07, 95% CI=1.92-2.23). NLP-extracted and
structured SDOH were also associated with suicide.


To formulate policies addressing suicide prevention, one must go beyond identifying
predictors by determining the magnitude of the effects of SDOH on suicide. A key impediment to this
has been the lack of comprehensive and reliably available SDOH information in large population-based
databases, where investigators have traditionally relied on structured data. Structured data often lack completeness regarding SDOH information, specifically, when they are designed for billing purposes. A recent study showed that unstructured data contain about 90 times more SDOH information than structured data13.




## abstract 
Are social determinants of health (SDOH), extracted from both structured and unstructured
clinical data, associated with an increased risk of suicide death among US Veterans? In this nested case-control study, SDOH from both structured data and unstructured data (extracted using a natural language processing [NLP] system) were associated with an increased risk of suicide death among US Veterans. SDOH are risk factors for suicide among the US Veterans and NLP can be leveraged to extract SDOH information from unstructured data.


# Insight

Social determinants of health (SDOH) are known to be associated with increased risk of suicidal behaviors, but few studies utilized SDOH from unstructured electronic health record (EHR) notes. Cases of suicide deaths were matched with 4 controls on birth year, cohort entry date, sex, and duration of follow-up. Suicide was ascertained by National Death Index and patients were followed-up up to 2 years after cohort entry with a study end date of September 30, 2015.
We developed an NLP system to extract SDOH from unstructured clinical notes. Structured data yielded
seven SDOH (social or familial problems, employment or financial problems, housing instability, legal
problems, lack of access to care or transportation, violence, and non-specific psychosocial needs), NLP
on unstructured data eight SDOH (social isolation, job or financial insecurity, housing instability, legal
problems, barriers to care, violence, transition of care, and food insecurity), and combining them yielded
nine SDOH. Adjusted odds ratios (aORs) and 95% confidence intervals (CIs) were estimated using
conditional logistic regression.


NLP-extracted SDOH, with and without structured SDOH, were significantly
associated with increased risk of suicide among Veterans, suggesting the potential of NLP in public
health studies.


> what does "combining" mean?

# EHR data

EHR data is generally assumed to be noisy, often with dubious predictive value, if restricted to administrative codes.
There are limitatiuons to NLP processing, although progress in ML/AI is rapidly changing that.

Authors correctly note: 
A recent study showed that unstructured data contain about 90 times more SDOH information than
structured data.

# what do NLP bring new to the table?

showing that SDOH matches when extrcated from notes.

# Why is better that structured SDOH?

Structured sdoh is expensive

# What are the limitations?

tokenization is never perfect

As for parsing negation, our NLP system was specifically trained to simultaneously detect
SDOH mentions and two of their attributes - presence and period. The presence attribute tells
us whether the mention of an SDOH detected by the NLP system is a negative occurrence or
not (e.g., “no housing issue” will have the presence attribute ‘no’). 

