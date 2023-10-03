# **ZCoR: Local Installation Steps**

[[Back to zbldev|development/zbldev]]


## **1. Install the codebase**

```
git clone https://github.com/zeroknowledgediscovery/zcor.git
cd zcor
git checkout dev
```

## **2. Extract the conda environment file**
In current folder, run:
```
python3 extract_env_file.py -p PREDICTORS/ASD.pickle -s zcor_environment.yml
```

## **3. Create the conda environment**

```
conda env create -f midway_environment.yml
conda activate zcor
```

## **4. Install zedstat (TODO ADD zedstat to conda)**
```
pip install zedstat
```

## **5. Run the sample run of loaded ZCoR object**
In current folder, run:
```
python3 run_zcor_model.py -p PREDICTORS/ASD.pickle -d DATA/OMNI_PEDIATRIC -n SCRIPT_RUN -s PREDICTIONS -b BYPRODUCTS -v True    
```

