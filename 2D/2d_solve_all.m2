-- Setup
S = QQ[x,y];
f = value scriptCommandLine#1;
partials = jacobian f;

-- Degree
print ("Degree:");
print (degree f)#0;

-- Milnor
singularities = ideal partials;
pd = primaryDecomposition singularities;
onTheCurve = i -> ((i+ideal f) != promote(ideal 1, S));
print("Milnor:");

-- use fundamental theorem of algebra to avoid solving
for i from 0 to #apply(pd, degree) - 1 do 
    if (onTheCurve (pd#i)) then 
        for j from 0 to degree (apply(pd, radical))#i - 1 do
               print ((apply(pd, degree))#i, (apply(pd, radical))#i);

-- Tjurina
singularities = ideal partials + ideal f;
print("Tjurina:");
pd = primaryDecomposition singularities;
for i from 0 to #apply(pd, degree) - 1 do 
    print ((apply(pd, degree))#i, (apply(pd, radical))#i);

-- Singular Points
T = QQ[x,y,z];
f = substitute(f, T);
F = homogenize(f, z);
p = sub(F, x=>1);
q = sub(F, y=>1);
r = sub(F, z=>1);

file = openOut "2d_to_solve.txt";
file << toString(F) << endl;

singularities = ideal jacobian p + ideal p;
pd = primaryDecomposition(singularities);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;
pd = primaryDecomposition radical ((ideal jacobian p) + ideal p);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;

singularities = ideal jacobian q + ideal q;
pd = primaryDecomposition(singularities);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;
pd = primaryDecomposition radical ((ideal jacobian q) + ideal q);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;

singularities = ideal jacobian r + ideal r;
pd = primaryDecomposition(singularities);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;
pd = primaryDecomposition radical ((ideal jacobian r) + ideal r);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;
file << close;

