# **ZCoR: Local Installation Steps**

[[Back to zbldev|development/zbldev]]

## **1. Install the codebase**

`git clone https://github.com/zeroknowledgediscovery/zcor.git
cd zcor
git checkout dev`

## **2. Extract the conda environment file**

Use the following code to extract the environment file from the saved ZCoR object:

`import sys
ZCOR_ROOT = "PATH TO ZCOR REPO"
sys.path.insert(0, ZCOR_ROOT)
from zcor.environment import extract_env_info

CLASSIFIER_PATH = "PATH_TO_SAVED_ZCOR_OBJECT"
extract_env_info(CLASSIFIER_PATH, "midway_environment.yml")
`

# **3. Create the conda environment**
`conda env create -f midway_environment.yml
conda activate zcor`

# **4. Then can do the ZCoR things**


