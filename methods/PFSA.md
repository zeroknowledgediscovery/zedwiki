# Generating Data from PFSA

Requirements:
Step 1. Need A PFSA specificying file
```
%------------------
#CONNX
1 0
1 0

#PITILDE
0.85 .15
.25 .75
%--------------------
```
Step 2. Run prun in zutil_ repo
```
~/zutil_/bin/prun cfg/test.pfsa 10000 out.pfsa
```
Note 10000 is the length of the sequence generated


# Scalar Multiplication of PFSA

Requirements:

1. PFSA specifying file


```
%------------------ comment line
% connection
#CONNX
1 0
1 0

% transition probability
#PITILDE
0.85 .15
.25 .75

%---------------------
```


2. Run psolve in repo structural_algebra_

```
./bin/psolve -x " 0.8 * test.pfsa " -o out.pfsa

```
Note nice examples of non-trivial machines are in 

```
~/zutil_/testsuite
```




