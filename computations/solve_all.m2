-- Setup
S = QQ[x,y,z,w];
f = value scriptCommandLine#1;
partials = jacobian f;

-- Degree
-- print("Degree:");
print (degree f)#0;

-- Milnor
singularities = ideal partials;
pd = primaryDecomposition singularities;
onTheCurve = i -> ((i+ideal f) == promote(ideal 1, S));
-- print("Milnor:");
for i from 0 to #apply(pd, degree) - 1 do 
    if (onTheCurve (pd#i)) then print ((apply(pd, degree))#i, (apply(pd, radical))#i);

-- Tjurina
singularities = ideal partials + ideal f;
-- print("Tjurina:");
print degree singularities;

-- Singular Points
singularities = ideal partials + ideal f;
file = openOut "sings.txt";
pd = primaryDecomposition(singularities);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;

pd = primaryDecomposition radical ((ideal jacobian f) + ideal f);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;
file << close;

-- Multiplicities
F = homogenize(f, w);
p = sub(F, x=>1);
q = sub(F, y=>1);
r = sub(F, z=>1);
s = sub(F, w=>1);

file = openOut "mults.txt";
file << toString F << endl;
pd = primaryDecomposition(ideal jacobian p + p);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;
pd = primaryDecomposition(ideal jacobian q + q);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;
pd = primaryDecomposition(ideal jacobian r + r);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;
pd = primaryDecomposition(ideal jacobian s + s);
for i from 0 to #pd - 1 do
    file << toString (pd#i)_* << endl;
file << close;


