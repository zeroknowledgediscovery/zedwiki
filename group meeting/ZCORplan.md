1. Chromosone data download and processing
2. Generate the full Qnet-training-ready dataframe 
    - SISA
    - PTSD 
    - uterine
    - melanona
    
    When we say Qnet-data, we mean the following:
    tabular data, rows are samples, columns are ICD code (3 letters), table entries are teh rest of teh code, with 'H' if value is missing. This dataframe is generated *once* and is same for all problems.
    From this dataset, we generate a POS qnet specific to different problems.
    For a SI/SA POS qnet, we extract the subset of samples for which we have SI/SA upto 3 montsh before the 
    traget event, and construct Qnet

    It is impprtant to specify how we incorporate time.
    Maybe it can be teh following formt:

    + XXX_**age_in_months**
    
    Or we can use:
    
    + XXX_**time_to_end_of_record_in_months**
    
    wher end of record is where we want the record dto end .. say 3 months before target event or 1 year before
    If we do it this way, then the dataframe needs to be different for each problem instance.

3. Incorporate PFSA processing in the ZBL pipline
4. Incorporate SHAP analysis in the zcor pipeline to generate the individual patient shap csvs
5. Need the complete and updated results for the current ZBL targets,  with saved model objects:
    - ASD 
    - ADRD
    - IPF
    - MACE
    - SI/SA
    - PTSD
    - CANCERS: Melanoma (with cpt), pancreatic, uterine, breast, lung, prostate, thyroid
    - BIPOLAR/MANIC


	