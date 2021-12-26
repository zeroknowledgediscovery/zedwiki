# Filename conventions

+ **SEX_database_model_subset_attrib0_attrib1_...**
    - databse: TRUVEN, UCM or any other  <<Note(all caps,"bell")>>
    - model: ZBL, NN, CNN etc <<Note(no underscores,"bell")>>
    - subset: <<Note(use BASIC for no subset,"bell")>>

+ Tabular Files of size > 200MB have extension '.dat'


# Columnname conventions

+ No capitalization
+ varnames: **auc, poslr, neglr, fpr, tpr, sensitivity, specificity**
+ `zbl_risk` is the column name of our estimated risk
+ Other column names:
    - `age` <<Warn((not age_at_screening)>>
+ vartype_attrib
    - auc_pfsa (correct)
    - p_final_cb (correct)
    - neg_lr_ (correct) <<Warn(NOT neg_LR or  LR_neg or anything else)>>
    
# Output files 

+ AUC stats
+ Patient_id
+ importance files
+ spectrum data
