# Table of deletion probability vs. rate 

| citation | deletion probability | rate | comment |
|:--|:--|:--|:--|
| \[2\] | .006 | .7 | The double-layered method (watermark) (30 errors in 5000 long block) | 
| \[2\] | .098 | .214 | The double-layered method (watermark) (450 erros in 4600 long block) |
| \[12\]| .03  |.5 | fixed and psuedo-random mark, 120 errors at sequence length 4000 (the 120 was not stated explicitly in paper, I calculate it from reading a table) |
| \[15\] | .29 | .25 | 2900 errors in 10012 long block, Non-binary channel|
| \[15\] | .08 (or .16) | .7 | read from figure 8 of the paper, block size not listed, and also .08 is for deletion only, but the paper actually considered insertion too, and insertion is assume to have the same probability as deletion in this table | 
| \[7\]| 1- \\\(2^2\\\)|
