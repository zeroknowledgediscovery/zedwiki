# commentary on article

Associations Between Natural Language Processing Enriched Social Determinants of Health and Suicide Death among US Veterans

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

