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


