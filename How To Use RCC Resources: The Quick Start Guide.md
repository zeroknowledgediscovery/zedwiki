# Official Documentation

Detailed documentation on how to use RCC is [here](https://rcc.uchicago.edu/docs/using-midway/index.html).
What follows is to be used as a *quick start*, along with some specific details on 
how the ZedLab applications are often run on RCC nodes.

# Running Jupyter Notebooks Remotely

The general approach is to run an instance of a Jupyter notebook without a browser
on a login or compute node, and communicate with that notebook
from your local machine *over VPN*

Thus, if you execute the following script from 
`/project2/ishanu/ZED_RESOURCES`, then 
it starts a notebook instance using the correct ip.
Then you need to use the path to the notebook, along with the
key it produces to talk to the instance from your local machine.

```
#!/bin/bash
module load python
a=`/sbin/ip route get 8.8.8.8 | awk '{print $NF;exit}'`
jupyter-notebook --no-browser --ip="$a"
```
Thus, the steps are:

+ run `screen`
+ run `/project2/ishanu/run_jupyter.sh | grep token`
+ copy the string with the external ip: will look something like: `http://128.135.112.68:8888/?token=a4e6d5911b5a5628390061c7a9ff2b5bf82d21f6d277695c`
+ Use the whole string in the browser window on your local machine on VPN
+ Detach screen is `CNTRL-D`, and you can exit RCC node

# Using Ineractive Sessions

[Using Thinlinc]( /uploads/thinlinc.webm)

# Launching Jobs on Compute Nodes

# Running Jobs on Login Nodes

# Modules

# Which Python To Use

# Installing Your Own Python Modules

# Visualization and Plots

# Monitoring the Queue

# Cancelling Jobs

# Using The Screen Command 
