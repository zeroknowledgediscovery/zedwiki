# Generating Data from PFSA


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

# Algebra with PFSA


1. Two PFSA specifying files: A.pfsa, B.pfsa

```
%------------------ example A.pfsa
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
2. run psolve in repo structural_algebra_

```
./bin/psolve -x " 0.8 * A.pfsa + 0.6 * B.pfsa " -o out.pfsa
./bin/psolve -x " 0.8 * A.pfsa - 0.6 * B.pfsa " -o out.pfsa
```

Operations supported by psolve

```
+ (sum of pfsas)
- (difference of pfsas)
! (inverse)
|| (synchronous composition)
|> (projective composition)
* (scalar multiplication)
```


