# **ZCoR: Local Installation Steps**

[[Back to zbldev|development/zbldev]]



## **1. Install the codebase**

```
git clone https://github.com/zeroknowledgediscovery/zcor.git
cd zcor
git checkout dev
```

## **2. Extract the conda environment file**

Run the `zcor/examples/local_zcor_run/RUN_LOADED_ZCOR.ipynb`, which will save the environment file to `midway_environment.yml`

# **3. Create the conda environment**
```
conda env create -f midway_environment.yml
conda activate zcor
```

# **4. Install zedstat (TODO ADD zedstat to conda)**
```
pip install zedstat
```

# **Then can do the ZCoR things**


