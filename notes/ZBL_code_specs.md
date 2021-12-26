# DSPL

+ https://www.google.com/publicdata/directory
+ Convert AUC STATS into DSPL (Dataset Publishing Language)
+ https://developers.google.com/public-data/docs/dsplgen
+ https://github.com/google/dspl

# Filename conventions

+ SEX_database_model_subset_attrib0_attrib1_
    - databse: TRUVEN, UCM or any other **(all caps)**
    - model: ZBL, NN, CNN etc **(no underscores)**
    - subset: **use BASIC for no subset**
    
+ Tabular Files of size > 200MB have extension '.dat'


# Columnname conventions

+ No capitalization
+ varnames: **auc, poslr, neglr, fpr, tpr, sensitivity, specificity**
+ report sensitivity and specificity not tpr, fpr
+ `zbl_risk` is the column name of our estimated risk
+ Other column names:
    - `age` (not age_at_screening)
+ vartype_attrib
    - auc_pfsa (correct)
    - p_final_cb (correct)
    - neg_lr_ (correct) NOT neg_LR or  LR_neg or anything else
    
# Output files 

+ AUC stats
+ Patient_id
+ importance files
