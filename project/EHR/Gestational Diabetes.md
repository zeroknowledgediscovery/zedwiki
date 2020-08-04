# [**Readymag Page**](https://readymag.com/zed/gestational-diabetes/)

# Exclusion Criteria

1. All patients must have the ICD9 code for the observation of pregnancy (`V22.0, V22.1`)
2. All patients must have EHR records for 52 weeks ( + 12 weeks (~4 months) to account for various time offsets used in the paper) before the first V22 code recorded.
3. Patients are separated into two cohorts: Positive, and Negative.
4. Positive patients are determined by having any of the target codes (recorded in `PUBLISHER/phenotypes/TARGET.dat`) within 32 weeks after the first V22 code recorded.
5. Negative patients are determined by not having any of the target codes. To ascertain the negativity, Negative patients must have target_code-free EHR records available for 32 weeks after the first V22 code recorded.

# Discussion

<img alt='nn comparison' src="http://34.66.189.202:4567/uploads/gd_spectrum.png" width="600px">
