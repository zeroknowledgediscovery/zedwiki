# Next Steps @Lynn

* Replicate the 29 biomes for data2 that we have for data1
* Time series forecasting for all biomes for data1 and data2
* Keep track of which biomes have more/less data
* Check if qnet for data2 is generated at higher p-value
* Next levels of microbiome organization: **Genus**

---

# Organize Pipeline @Alice


@startuml

(*) --> "Data Formatting"
-->[You can put also labels] "Quantization"
-->[You can put also labels] "Qnet generation"
If  "masking check" then
--> "Forecaster"
else
--> "hypothesis generator"
--> (*)

@enduml

Write python classes for the following: 

1. Data formatting  
2. Quantization
3. Qnet generation
4. Masking check
5. Forecast generation

The objective here is to go from a dataset like here:
https://raw.githubusercontent.com/zeroknowledgediscovery/course_notes/master/datasets/MuBIOME_/data_1/SamplesByMetadata_otuDADA2_DIABIMMUNE_RSRC_TaxaRelativeAbundance.csv

```
import zbiome as zb
zb.getdata(filepath,tax='phylum')
zb.quantize(numlevels=5)
zb.qnet()
df=zb.masked_runs(biomes='all')
ef=zb.forecast(biomes='all',sampleid='all',observation_periods=4)
zb.generate_hypothesis(time,causality_window)
```

