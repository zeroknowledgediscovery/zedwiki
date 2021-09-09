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

If you would rather use the RCC midway as a remote desktop, you can do so via the thinlinc client, as demonstrated by the short webm:

[Using Thinlinc]( /uploads/thinlinc.webm)

# Launching Jobs on Compute Nodes

Running resource intensive jobs on teh compute node will get you booted.
You have to either use the slurm job scheduler to launch jobs on teh compute nodes, or 
use an interactive session. 

## Interactive Sessions

Link to more info on intecative sessions is [here](https://rcc.uchicago.edu/docs/using-midway/index.html#id11)
Quickstart:

```
 sinteractive --exclusive --nodes=2 --time=08:00:00
```

or even simpler:
```
 sinteractive --exclusive  --time=08:00:00
```

Reserving inetractive nodes for long times (8 hrs is a long time) will not get you allocated quickly. For quick stuff, you can use a *debug* allocation:

```
sinteractive --qos=debug --time=00:15:00 --ntasks=4
```

## Slurm Batch Jobs

The basic command to run to schedule a batch job:

```
sbatch example.sbatch
```
 where `example.batch` is a *batch* file, which is a text file with specification on how and what to run as follows:
 
 ```
 #!/bin/bash
#SBATCH --job-name=example_sbatch
#SBATCH --output=example_sbatch.out
#SBATCH --error=example_sbatch.err
#SBATCH --time=00:05:00
#SBATCH --partition=broadwl
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=14
#SBATCH --mem-per-cpu=2000

module load openmpi
./hello-world
 
 ```

We have a special launcher we use at ZedLab to streamline this, and write our batch files, located at  `/project2/ishanu/ZED_RESOURCES`, the *launcher_s.sh*

```
./launcher_s.sh -h
===> SLURM LAUNCHER <=== copyright ishanu@uchicago.edu 2017
OPTIONS:
-P : program string: use single or quoates
-F : interpret program as file
-X : log dependency graphviz style in filename jobid.depx
-p : partition to target
-J : jobname
-C : number of cores on 1 node
-T : time in hours
-N : Number of nodes
-M : memory gb allocated
-D : string of job dependecies: ids sep by space: use single or double quotes
-A : string of afterany job dependecies: ids sep by space: use single or double quotes
-d : dry-run
-Y : forward dep string sep by space
============================
```









# Running Jobs on Login Nodes

# Modules

# Which Python To Use

# Installing Your Own Python Modules

# Visualization and Plots

# Monitoring the Queue

# Cancelling Jobs

# Using The Screen Command 
