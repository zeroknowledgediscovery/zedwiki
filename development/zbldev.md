# Existing Model

+ IPF model

# Local Model "installation"
[[Installation Guide|development/zbldev/zcor_setup]]

# Epic APP

Lets worry about this a bit later. Lets focus on making a SAAS model dployed for our ZCOR models firts

# PreSAAS ZCoR Applioation

We want to make sure we can task the developer correctky.
Lets make sure our current code is a pure python application that can run in a different place other than midway

Also we need to address the following points:

+ what is the "rawest" data input we can have (maybe from Epic data pull?)
+ make an example that reads data for a single patient and returns
    - zcor score
    - decision (at a tunable value of specificity or LR+)
    - some shap values
+ have option for calibration (we would need a small dataset for this, this is dersirable, but can we do without?)
    - test what happens to our performance if we do not calibrate? **
  

