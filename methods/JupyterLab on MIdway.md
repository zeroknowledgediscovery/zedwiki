`ssh $USERNAME@midway2.rcc.uchicago.edu`

`sinteractive --exclusive --nodes=1 --time=35:00:00 --partition=gpu2 --gres=gpu:1`

`sinteractive --exclusive --nodes=1 --time=35:00:00 --partition=bigmem2`

`module load Anaconda3/2019.03 && conda activate $CONDAENV && cd $WORKDIR && /sbin/ip route get 8.8.8.8 | awk '{print $NF;exit}' // yields $IP`

`jupyter lab --no-browser --ip=$IP --port 8888`