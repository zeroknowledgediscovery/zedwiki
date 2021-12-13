# DSPL

+ https://www.google.com/publicdata/directory
+ Convert AUC STATS into DSPL (Dataset Publishing Language)
+ https://developers.google.com/public-data/docs/dsplgen
+ https://github.com/google/dspl


# Filename conventions

+ SEX_attrib0_attrib1_...
+ Tabular Files of size > 200MB have extension '.dat'


# Columnname conventions

+ `zbl_risk` is the column name of our estimated risk
+ Other column names:
    - `age` (not age_at_screening)
+ vartype_attrib
    - auc_pfsa (correct)
    - p_final_cb (correct)
    - neg_LR_ (correct) NOT LR_neg or anything else
    
# Output files 

+ AUC stats
+ Patient_id
+ importance files
