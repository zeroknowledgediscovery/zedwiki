# [**Readymag Page**](https://readymag.com/zed/gestational-diabetes/)

# Exclusion Criteria

1. All patients must have the ICD9 code for the observation of pregnancy (`V22.0, V22.1`)
2. All patients must have EHR records for 52 weeks ( + 12 weeks (~4 months) to account for various time offsets used in the paper) before the first V22 code recorded.
3. Patients are separated into two cohorts: Positive, and Negative.
4. Positive patients are determined by having any of the target codes (recorded in `PUBLISHER/phenotypes/TARGET.dat`) within 32 weeks after the first V22 code recorded.
5. Negative patients are determined by not having any of the target codes. To ascertain the negativity, Negative patients must have target_code-free EHR records available for 32 weeks after the first V22 code recorded.

# Discussion

<img alt='nn comparison' src="http://34.66.189.202:4567/uploads/gd_spectrum.png" width="600px">

## Unspecified disorder of plasma protein metabolism (273.9)

Maternal plasma cfDNA levels and pregnancy outcomes were obtained from non-invasive prenatal testing (NIPT) Screening System and hospitalization records, respectively~\cite{pmid31278894} in a Chinese population of 831 women, and increase in cell free DNA levels were associated with increased risk of GDM, and was dependent on maternal age, which was posited to be an important effect modifier. Evidence also exists that improper metabolism of soluble transferrin receptor (sTfR) might be implicated inincreased risk of GDM~\cite{pmid27511926}, by inceasing plasma concentrations of ferritin. In addition, associations with reduction in levels of maternal pregnancy-associated plasma protein-A (PAPP-A) has been shown to be a predictor of GDM, type 2 diabetes (T2D), or large-for-gestational-age (LGA) births~\cite{pmid842585}.
 
 
## Other specified disorders of adrenal glands (255.8) Other corticoadrenal overactivity (255.3)
Cushing's disease caused by an adrenal adenoma is rare during pregnancy and may be overlooked by obstetricians and physicians, but can lead to hypertension, diabetes mellitus and an increased risk of fetal and maternal morbidity~\cite{pmid30943935,pmid27704478}. Some rare tumors of the adrenal gland have also been reported to mimic gestational hypertension, preeclampsia or eclampsia, and gestational diabetes mellitus~\cite{pmid23527821}. \cite{pmid18209867,pmid26202044,pmid29523633}

## Vitamin B6

There is some evidence of vitamin B6 deficiency implicated in GDM~\cite{pmid842585,sukumar2016prevalence}. The increased association between depression and diabetes mellitus is generally acknowledged. Recent studies suggest that depression leads to diabetes. However, the underlying molecular mechanisms for this association remain unclear. Literature and our data indicate that inflammatory and/or stress factors in depression up-regulate tryptophan (TRP) conversion into kynurenine (KYN), a substrate for nicotinamide adenine dinucleotide (NAD) biosynthesis. Deficiency of vitamin B6, a cofactor of the key enzymes of KYN - NAD pathway, shunts KYN metabolism from formation of NAD towards production of xanthurenic (XA) and kynurenic (KYNA) acids. Human and experimental studies reveal that XA, KYNA and their metabolites interfere with production, release and biological activity of insulin~\cite{pmid25401165}. 

## Dysmetabolic syndrome X (277.7)

Obesity increases the risk for developing gestational diabetes mellitus (GDM) and preeclampsia (PE), which both associate with increased risk for type 2 diabetes mellitus (T2DM) and cardiovascular disease (CVD) in women in later life. In the general population, metabolic syndrome (MetS) associates with T2DM and CVD~\cite{pmid30513077}. Increasing BMI in combination with MetS increased the estimated probability for GDM and decreased the probability of an uncomplicated pregnancy. 


## Other disorders of lipoid metabolism (272.8)
Maternal lipids are strong determinants of fetal fat mass.  During early pregnancy, the increase in maternal fat depots is facilitated by insulin, followed by increased adipose tissue breakdown and subsequent hypertriglyceridemia, mainly as a result of insulin resistance (IR) and estrogen effects. The response to diabetes is variable as a result of greater IR but decreased estrogen levels. The vast majority of fatty acids (FAs) in the maternal circulation are esterified and associated with lipoproteins. These are taken up by the placenta and hydrolyzed by lipases. The released FAs enter various metabolic routes and are released into fetal circulation~\cite{pmid26351960,pmid24720597}. In gestational diabetes mellitus (GDM), maternal TAG and NEFA levels correlate with neonatal anthropometric measures. In GDM, adipocyte fatty acid-binding protein in fetuses correlated with neonatal fat mass; changes in maternal or cord blood leptin, retinol binding protein 4 and adiponectin concentrations have been related to neonatal fat mass or birth weight, although their importance remains to be investigated.

## Unspecified disorder of carbohydrate transport and metabolism (271.9)
 Alterations in organic acid biomarkers from fatty acid and carbohydrate metabolism have been documented in type 2 diabetes patients, and their association with GDM is increasingly becoming clear~\cite{pmid24703806}.  Women with normal glucose tolerance before conception who develop gestational diabetes have significant decreased insulin sensitivity relative to women in a control group, and alterations to carbohydrate meatbolism in gestation in women with normal and abnormal glucose tolerance is suspected~\cite{pmid8194212,pmid24703806}, and might have long-term effects on carbohydrate metabolism after pregnancy~\cite{pmid22385344}. 
 
# Motivation

Gestational diabetes mellitus is a common pregnancy complication associated with significant adverse
health outcomes for both women and infants. Effective screening and early prediction tools as part of
routine clinical care are needed to reduce the impact of the disease on the baby and mother. Using
large-scale electronic health records, Artzi and colleagues developed and evaluated a machine
learning driven tool to identify women at high and low risk of GDM. Their findings showcase how
artificial intelligence approaches can potentially be embedded in clinical care to enable accurate and
rapid risk stratification. 

Gestational diabetes mellitus (GDM), defined as glucose intolerance during
gestation, is a common complication of pregnancy. GDM is associated with an increased risk of short- and long-term complications in both mother and child, including type 2 diabetes and operative
delivery. Identifying women at a higher risk of GDM, as early into the pregnancy
as possible, can potentially enable the implementation of lifestyle intervention strategies, thereby reducing the associated
disease burden. However, GDM diagnostic criteria vary by country, illustrating the lack of consensus around the most effec-
tive way to screen in routine clinical care[1]. Embedding a data-driven prognostic tool within routine care can potentially address these challenges and enable clinicians to identify women at higher or lower risk earlier and with greater accuracy. In a recent work, Artzi et al. [2] present an algorithm constructed using machine learning (ML) and retrospective electronic health records (EHR) to predict GDM.

## Clinical Characterization and Diagnosis of GDM 

Gestational diabetes (GDM) is associated with adverse pregnancy and neonatal outcomes and increased maternal risk for subsequent type 2 diabetes. Offspring of mothers with GDM are prone to adverse health outcomes including fetal macrosomia, respiratory difficulties and metabolic complications in the neonatal period, and carry a higher risk for future obesity and alteration in glucose metabolism. Gestational diabetes mellitus (GDM) is a unique clinical entity that juxtaposes the health interests of mothers, babies, and communities. The American Diabetes Association (ADA) defines gestational diabetes as diabetes first diagnosed in the second or first trimester of pregnancy that is not clearly preexisting type 1 or 2 diabetes [1••]. With dramatic increases in type 2 diabetes and obesity, identification of women with preexisting type 2 diabetes by first trimester screening is important. In the second trimester of pregnancy, screening for GDM should be completed for all women. The foundation of GDM treatment is lifestyle interventions; medications, primarily insulin, are indicated if lifestyle measures are insufficient. Treatment of GDM reduces risk of pregnancy complications and adverse neonatal outcomes including macrosomia and shoulder dystocia [2]. After pregnancy, maternal risk for type 2 diabetes and cardiovascular disease is increased and continued follow-up and early intervention for impaired glucose intolerance are crucial. Health policy initiatives to improve insurance coverage and access to a diabetes prevention program (DPP) are an important step for preventing or delaying the onset of type 2 diabetes in women with a history of GDM. Offspring of women with GDM are at increased risk for obesity and type 2 diabetes and a vicious cycle continues [3].

## Feasibility of Detection Before Symptoms 

According to AMerican Diabetes Association~\cite{american20182}, characterization of the underlying pathophysiology is more developed in type 1 diabetes than in type 2 diabetes. It is now clear from studies of first-degree relatives of patients with type 1 diabetes that the persistent presence of two or more autoantibodies is an almost certain predictor of clinical hyperglycemia and diabetes. The rate of progression is dependent on the age at first detection of antibody, number of antibodies, antibody specificity, and antibody titer. Glucose and A1C levels rise well before the clinical onset of diabetes, making diagnosis feasible well before the onset of DKA. Three distinct stages of type 1 diabetes can be identified (Table 2.1) and serve as a framework for future research and regulatory decision-making (4,5). The paths to β-cell demise and dysfunction are less well defined in type 2 diabetes, but deficient β-cell insulin secretion, frequently in the setting of insulin resistance, appears to be the common denominator. Characterization of subtypes of this heterogeneous disorder have been developed and validated in Scandinavian and Northern European populations but have not been confirmed in other ethnic and racial groups. Type 2 diabetes is primarily associated with insulin secretory defects related to inflammation and metabolic stress among other contributors, including genetic factors. Future classification schemes for diabetes will likely focus on the pathophysiology of the underlying β-cell dysfunction and the stage of disease as indicated by glucose status (normal, impaired, or diabetes) (4).

## Prevalence of GDM
In 2017, it was estimated that 21.3 million births (16.2%) worldwide were affected by hyperglycemia in pregnancy, and of these, 86.4% were due to GDM. There is a notable regional variation with age-adjusted prevalence ranging from 9.5% in Africa to 26.6% in Southeast Asia [4]. In the USA, according to 2016 data from the Centers for Disease Control and Prevention (CDC), the crude national prevalence of GDM was 6.0% and pre-existing diabetes in pregnancy was 0.9%. From 2012 to 2016, standardized prevalence increased for gestational diabetes (5.2 to 5.6%) and was stable for preexisting diabetes (0.8%). Accounting for race/ethnicity, the prevalence of GDM was highest among non-Hispanic Asian women (11.1%). Accounting for BMI, prevalence of gestational diabetes ranged from 3.6% for normal-weight women (pre-pregnancy BMI 18.5–24.9) to 13.9% with class III obesity (BMI ≥ 40.0) [5•]. GDM prevalence also increases with advancing maternal age. The crude and age-adjusted prevalence of GDM and subsequent diabetes were evaluated by sociodemographic and health-related characteristics among women age ≥20 years in the National Health and Nutrition Examination Surveys, 2007–2014 (N=8185). Logistic regression analyzed independent factors associated with GDM and subsequent diabetes, which increased the estimated  prevalence of GDM to 7.6%. Women who were Mexican American (vs. non-Hispanic white), had ≥4 live births (vs. 1), had a family history of diabetes, or were obese (vs. normal weight) had a higher age-standardized prevalence of GDM (each p < 0.04). Among women with GDM, 19.7% had a subsequent diagnosis of diabetes. 

## Costs of GDM

Costs of GDM to society are significant. A 2012 US cost analysis determined that the national cost of gestational dia-
betes was $1.3 billion with an average cost of $5800 per case of GDM. Between 2007 and 2012, the national burden dou-
bled for GDM (103% increase) including a 23% increase in prevalence and 65% increase in cost per case [7]. The rising
prevalence and substantial costs of GDM make this a critical national and international health concern.

## Diet and Exercise May Prevent GDM

Findings from 19 studies (6633 women) showed a possible reduction in GDM in women who received diet and exercise programs compared with women who received standard care. Fourteen studies (6089 women) showed a possible reduction in caesarean birth (14 studies; 6089 women) and 16 studies (5052 women) showed lower weight gain during pregnancy in women who received exercise programs. We found no differences between groups in other health problems for: pre‐eclampsia (8 studies; 5366 women); high blood pressure (6 studies; 3073 women); a large for age baby at birth (11 studies; 5353 babies); and perineal trauma (2 studies; 2733 women). Death of babies around birth (2 studies; 3757 babies), the baby having low blood glucose after birth (2 studies; 3653 babies), and infants being overweight (2 studies; 794 infants) did not differ in the two groups. Effects on depression or type 2 diabetes for mothers, a combined outcome of death or ill‐health for babies, or type 2 diabetes or neurosensory disability for babies as children were not reported. The evidence suggests combined diet and exercise programs may be effective for preventing GDM though the optimum components of these programs are not yet clear~\cite{shepherd2017combined}.

## Pre-pregnancy Biomarkers


Recent research has examined the use of pre-pregnancy biomarkers to identify women at high risk for gestational diabetes. A case control study of 256 GDM cases found that sex hormone binding globulin, glucose, adiponectin, and homeostasis model assessment-estimated insulin resistance (HOMAIR) were independently associated with odds for GDM. Using these biomarkers, a risk score was composed which showed a better predictive value for GDM than traditional risk factors of age, ethnicity, BMI, family history of DM, and personal history of GDM (AUC 0.74 versus 0.67) [13]. These findings require further validation before they can be routinely used in clinical practice.

## Current Diagnosis Tests

The optimal strategy for diagnosis of GDM is debated, as different strategies and thresholds will identify different de-
grees of hyperglycemia and risk for adverse outcomes. The landmark Hyperglycemia and Adverse Pregnancy Outcomes
(HAPO) study included 23,316 pregnant women with blinded glycemic data from 75-g, 2-h oral glucose tolerance test
(OGTT) at 24–28 weeks. This study showed a continuous association between increasing maternal glucose levels and
adverse maternal, fetal, and neonatal outcomes [15]. Based on these results, the International Association of Diabetes
and Pregnancy Study Group (IADPSG), the ADA, and the Endocrine Society recommend the one-step 75-g OGTT for
screening at 24–28 weeks [1••, 16, 17]. Thresholds for GDM diagnosis from the 75-g OGTT were defined by the average
fasting, and 1-h and 2-h glucose values from the HAPO study which were associated with 1.75 times the odds of adverse
outcomes compared to the study population [16].

In contrast, a National Institutes of Health (NIH) consensus group from 2013 and ACOG support a two-step approach for
GDM diagnosis. A 50-g, 1-h non-fasting screen is initially performed and women who screen positive (1-h glucose >
130–140) then undergo a 100-g, 3-h OGTT for definitive diagnosis (see Table 1 for diagnostic cutoffs). The NIH consen-
sus group concludes that this two-step approach is superior because there is a lack of evidence that the one-step strategy
leads to improved maternal or fetal outcomes but is associated with increased healthcare costs, life disruption, and psychosocial burdens [23].

GDM can be managed with lifestyle interventions alone in up to 80–90% of women, depending on diagnostic criteria, can be
managed with lifestyle interventions alone [20, 21].




