-- Setup
S = QQ[x,y];
f = value scriptCommandLine#1;
partials = jacobian f;

-- Degree
print (degree f)#0;

-- Milnor
singularities = ideal partials;
pd = primaryDecomposition singularities;
onTheCurve = i -> ((i+ideal f) != promote(ideal 1, S));
L = []
-- use fundamental theorem of algebra to avoid solving
for i from 0 to #apply(pd, degree) - 1 do 
    if (onTheCurve (pd#i)) then 
        for j from 0 to degree (apply(pd, radical))#i - 1 do
            L = append(L, (apply(pd, degree))#i);
print(L)

-- Tjurina
singularities = ideal partials + ideal f;
-- print("Tjurina:");
pd = primaryDecomposition singularities;
L = [];
for i from 0 to #apply(pd, degree) - 1 do 
    L = append(L, (apply(pd, degree))#i);
print(L);

-- Singular Points
T = QQ[x,y,z];
f = substitute(f, T);
F = homogenize(f, z);
p = sub(F, x=>1);
q = sub(F, y=>1);
r = sub(F, z=>1);
s = sub(F, z=>0);

print(toString(F));

L = []

singularities = ideal jacobian p + ideal p;
pd = primaryDecomposition(singularities);
for i from 0 to #pd - 1 do
    -- pd#i take's the ith element of pd
    -- _* turns the ideal into a list
    -- new Array from turns list into array (better for python)
    L = append(L, toString (new Array from (pd#i)_*));
pd = primaryDecomposition radical ((ideal jacobian p) + ideal p);
for i from 0 to #pd - 1 do
    L = append(L, toString (new Array from (pd#i)_*));

singularities = ideal jacobian q + ideal q;
pd = primaryDecomposition(singularities);
for i from 0 to #pd - 1 do
    L = append(L, toString (new Array from (pd#i)_*));
pd = primaryDecomposition radical ((ideal jacobian q) + ideal q);
for i from 0 to #pd - 1 do
    L = append(L, toString (new Array from (pd#i)_*));

singularities = ideal jacobian r + ideal r;
pd = primaryDecomposition(singularities);
for i from 0 to #pd - 1 do
    L = append(L, toString (new Array from (pd#i)_*));
pd = primaryDecomposition radical ((ideal jacobian r) + ideal r);
for i from 0 to #pd - 1 do
    L = append(L, toString (new Array from (pd#i)_*));

print(L);
