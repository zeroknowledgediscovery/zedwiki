# **ZCoR: Local Installation Steps**

[[Back to zbldev|development/zbldev]]


## **1. Install the codebase**

```
git clone https://github.com/zeroknowledgediscovery/zcor.git
cd zcor
git checkout dev
```

## **2. Extract the conda environment file**

Run the `zcor/examples/local_zcor_run/EXTRACT_ENV_FILE.ipynb`, which will save the environment file to `midway_environment.yml`

## **3. Create the conda environment**

```
conda env create -f midway_environment.yml
conda activate zcor
```

## **4. Add the environment to the list of jupyter kernels**

```
conda install ipykernel
python -m ipykernel install --user --name=zcor --display-name="ZCOR env"
```

## **5. Install jupyterlab**

`conda install -c conda-forge jupyterlab`

## **6. Install zedstat (TODO ADD zedstat to conda)**
```
pip install zedstat
```

## **7. Run the sample run of loaded ZCoR object**

Run the `zcor/examples/local_zcor_run/RUN_LOADED_ZCOR.ipynb`

