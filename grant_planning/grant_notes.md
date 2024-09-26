[Grants Planned](../grant.md)

# AI BTO DARPA

https://www.darpa.mil/news-events/2024-09-13

DARPA funds the research and development of technologies with the potential for transformational impact, central to delivering on the agency’s mission to create and prevent strategic surprise for national security. The agency’s Biological Technologies Office focuses on the natural world to derive revolutionary capabilities centered on:

Foundational technologies that promote simulation and prediction of biological systems and outcomes, like simulation, foundational models, and data generation.

## Time
DEADLINE: Wednesday, October 9, 2024 by 4:00PM EDT. 

+ [RFP pdf](uploads/DARPA-SCA-24-01.pdf)
+ [submission portal](https://usg.valideval.com/teams/aibto_2024/signup)
+ [white paper template](uploads/Attachment_A_-_White_Paper_Template_BTO.docx)



---

# ARPA-H PRECISE-AI

https://arpa-h.gov/research-and-funding/programs/precise-ai

Performance and Reliability Evaluation for Continuous Modifications and Useability of Artificial Intelligence

[RFP LINK](uploads/ARPA-H-SOL-25-113_DRAFT.pdf)



### Objectives of TA1, TA2, and TA3 in ARPA-H's PRECISE-AI Program with Focus on EHR Data

Here is an in-depth exploration of the objectives and expectations for **Technical Area 1 (TA1)**, **Technical Area 2 (TA2)**, and **Technical Area 3 (TA3)** within ARPA-H's PRECISE-AI program, specifically focusing on **Electronic Health Records (EHR)** data. It includes guidelines on **ground truth labeling**, key examples of **use cases**, as well as details on the required scope of work, page limits, and deadlines for proposal submissions.


#### Technical Area 1 (TA1): **Automated Surrogate Ground Truth Label Extraction**

TA1 focuses on automating the extraction of **surrogate ground truth labels** from healthcare data, particularly from EHR systems. The aim is to develop scalable, generalizable methods to continuously generate these labels across various clinical scenarios. Ground truth labels represent the best estimate of the clinical state of a patient based on available evidence, serving as a benchmark for evaluating AI models.

##### Key Components:
1. **Data Extraction**:
   - TA1 proposals should develop innovative methods for extracting **structured** (e.g., ICD-10 codes, lab results) and **unstructured** data (e.g., clinical notes, radiology reports) from EHRs to generate surrogate ground truth labels.
   - **Multimodal Data Integration**: Multiple data sources (e.g., radiology reports, laboratory results, medications) must be combined to create a robust estimate of the patient's condition.
   
2. **Validation**:
   - The extracted surrogate ground truth labels should be validated by comparing them to traditional methods, such as manual review or expert panels, which are typically resource-intensive and not scalable. The goal is to approximate traditional ground truth labeling as closely as possible.

##### Example Use Case:
For a pneumonia diagnosis using chest X-ray images, TA1 performers might extract related information from EHRs, such as ICD-10 codes, notes about infection symptoms, and lab results like blood counts, to create the surrogate ground truth label. This can then be compared with the AI model's predictions to evaluate performance.

##### Scope:
- **Not Developing New AI Models**: The focus is on developing methods to extract labels that can be used to evaluate existing AI systems, not creating new AI decision-support tools (AI-DSTs).
  

#### Technical Area 2 (TA2): **Degradation Detection and Self-Correction**

TA2 aims to develop tools for **continuous monitoring** of AI models used in clinical settings, specifically identifying when model performance degrades over time. This area is focused on maintaining model accuracy by diagnosing issues and implementing corrective actions based on EHR data and other healthcare sources.

##### Key Components:
1. **Continuous Monitoring** (TA2.1):
   - TA2 focuses on building systems to continuously monitor AI performance across **different clinical sites** and **patient populations** using the surrogate ground truth labels generated in TA1.
   - Proposals should address both **local performance monitoring** (e.g., within a specific healthcare facility) and **global performance monitoring** (e.g., across multiple sites) to quickly identify drops in model performance, particularly for subpopulations that may be underrepresented.

2. **Root-Cause Analysis** (TA2.2):
   - When a performance degradation is detected, tools must be able to analyze the underlying **root cause** (e.g., data shifts due to demographic changes or EHR updates).
   - Proposals should include methods for analyzing **data distribution shifts** and identifying whether the model's inputs or outputs are affected.

3. **Self-Correction** (TA2.3):
   - The system should have the ability to suggest or automatically implement **corrective actions** to restore the AI system's performance. This may involve retraining the AI model based on updated data or adjusting model parameters to adapt to the new context.

##### Example Use Case:
An AI model that predicts sepsis may see performance degradation as the hospital updates its clinical protocols, leading to changes in the patterns of vital signs in the EHR. TA2 tools would detect the drop in accuracy, identify that the changes are due to shifts in the EHR input data, and suggest corrective actions like updating the model with more recent data.

#### Technical Area 3 (TA3): **Quantifying Uncertainty and Improving Clinician Performance**

TA3 is designed to enhance clinician trust in AI predictions by quantifying and effectively communicating **uncertainty** in model outputs. This ensures that clinicians can make informed decisions based on AI recommendations.

##### Key Components:
1. **Uncertainty Quantification**:
   - Proposals should focus on methods to **quantify uncertainty** in AI predictions (e.g., confidence intervals or probabilistic outputs) and communicate this uncertainty in a manner that clinicians can understand and use effectively.
   
2. **Improving Clinical Decision-Making**:
   - Proposals should provide innovative ways to **present model outputs and uncertainty** to clinicians, ensuring that they can interpret when a model's prediction might be less reliable.
   - Tools should be designed for seamless integration into existing clinical workflows, improving clinician performance in decision-making without increasing cognitive burden.

##### Example Use Case:
In a clinical setting where AI predicts the need for ICU admission, the system should provide not only the prediction but also the associated uncertainty (e.g., a 90% confidence in the need for ICU care). If the uncertainty is high, clinicians might opt for more careful monitoring or further tests.


### Application Focus and Guidance

1. **Development of New Algorithms vs. Application of Existing Tools**:
   - The RFP emphasizes **developing new methodologies** for label extraction, performance monitoring, and degradation correction rather than simply applying existing AI tools.
   - Innovation should be focused on creating **scalable solutions** for continuous monitoring and self-correction of AI models.

2. **Use Case Examples**:
   - The RFP mentions specific use cases such as **diagnosis through X-ray imaging, CT imaging, and clinical insights derived from EHR data**.
   - Proposers can also submit alternative use cases for the combination of TA1, TA2, and TA3, as long as they align with the program's goals.

3. **Application Context**:
   - ARPA-H expects the work to be highly applied, with a focus on **real-world clinical settings**. Proposals should include plans for testing solutions across **multiple clinical sites** with diverse patient populations.

### Submission Guidelines

#### Page Limits:
- **50 pages**: Proposals that address all three technical areas (TA1, TA2, and TA3).
- **40 pages**: Proposals that address two areas among TA1, TA2, and TA3.
- **25 to 30 pages**: Proposals addressing only one of TA1, TA2, or TA3.

#### Formatting:
- Use at least **12-point font** for the main text.
- Proposals must be submitted in **PDF format** through the designated submission portal.


The ARPA-H PRECISE-AI program aims to build **robust, scalable systems** that can continuously extract surrogate ground truth labels, detect AI model performance degradation, and implement corrective actions. With a focus on leveraging EHR data across diverse clinical settings, the program seeks to improve the reliability of AI decision-support tools in healthcare, ensuring they remain effective and trustworthy over time. Proposals should emphasize **innovation in new algorithms**, **real-world applicability**, and **scalability** across healthcare systems.

---

# VBUSH

[RFP Link]( /uploads/N0001424SF007 FY25 VBFF.pdf)

Deadline: 27 September 2024 (Friday) at 05:00 PM Eastern Time 

Format: Individual PIs must submit a Cover Page, Abstract, Basic Research Statement, White Paper, and
Curriculum Vitae (CV). All documents must be submitted in PDF format in compliance with the
guidelines below. When submitting the documents, the PI must upload the Cover Page, Abstract, Basic
Research Statement, White Paper and CV as one PDF file.
i.
Format
Paper size – 8.5x11-inch
Margins – 1 inch
Spacing – single-spaced
Font – Times New Roman, 12-point

+ (a) Cover page: Include the PI’s name and university. Include a protective legend for proprietary
information, if applicable.
+ (b) Abstract (not to exceed 300 words): Describe the research objective, technical approaches,
and anticipated outcome of the specific research. A non-proprietary version of the abstract must
be submitted without other restrictions. The non- proprietary abstract must be a version that is
releasable to the public under the Freedom of Information Act without changes.
+ (c) Basic Research Statement (one (1) page limit, single-sided): Describe how the proposed
research meets the DoD definition of basic research provided Section II. A. Program Description
of this announcement. Describe the extraordinary outcomes that may be achieved as a result of
the proposed project.
+ (d) Subject Research: Identify anticipated human or animal subject research (where applicable).
+ (e) White paper (four (4) page limit, single-sided): Describe the basic scientific or technical
research to be undertaken. Describe the technical approach. Summarize the state of the field and
describe what is innovative about the proposed approach. Assuming a successful completion of
the course of investigation, what results, new knowledge, or insights might it afford compared to
alternate approaches other researchers in this field have taken. Include approximate yearly costs
for the project in a brief statement. Reference citations are not required but may be included
within the four-page limit, and can be inserted as footnotes. If used, figures are also part of the
page limit.

+ (f) PI’s Curriculum Vitae (CV) (no page limit) -The CV should include relevant experience,
publications, and funding received in the area of interest, and any previous involvement and
experiences with the DoD. List all previous DoD funding including project titles within the last
eight years.

It is anticipated that awards will be made in the form of grants to U.S. institutions of higher education
(IHE) (universities). It is anticipated an individual maximum award value will be $3 million for five (5)
years, with the actual amount contingent on availability of funds.
There is no guarantee that any of the proposals submitted in a particular scientific area will be
recommended for funding, and more than one proposal may be recommended for funding for a particular
area. The Government reserves the right to select for negotiation some, one, or none of the proposals
received in response to this announcement.
- Total Amount of Funding Available: \$24 million to \$30 million
- Anticipated Number of Awards: 8 to 10
- Anticipated Range of Individual Award Amounts: $3 million
- Previous Year(s) Average Individual Award Amounts: $3 million 
