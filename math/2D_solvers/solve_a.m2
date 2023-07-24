-- Setup
S = QQ[x,y,z];

f = value scriptCommandLine#1;

F = homogenize(f, z);
partials = jacobian F;

-- Degree
print (degree f)#0;

-- Singular Points
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

-- Milnor / Tjurina
-- x, y
-- partial derivative corresponding to x
a = partials_(0, 0);
a = sub(a, z=> 1);

-- partial derivative corresponding to y
b = partials_(1, 0);
b = sub(b, z=> 1);

pd = primaryDecomposition ideal (a, b);

degs_m = new Array from pd/degree;
milnor = [];
-- print(pd/degree, pd/radical);
for i in pd do
(
    r = radical i;
    milnor = append(milnor, toString new Array from r_*);
)

pd = primaryDecomposition ideal (a, b, sub(F, z=>1));

degs_t = new Array from pd/degree;
tjurina = [];
for i in pd do
(
    r = radical i;
    tjurina = append(tjurina, toString new Array from r_*);
)



-- x, z
a = partials_(0, 0);
a = sub(a, y=>1);

b = partials_(2, 0);
b = sub(b, y=>1);

pd = primaryDecomposition ideal (a, b);
-- print(pd/degree, pd/radical);

for i in pd do
(
    r = radical i;
    if isSubset(ideal z, r) then (
        milnor = append(milnor, toString new Array from r_*);
        degs_m = append(degs_m, degree i);
    )
)

pd = primaryDecomposition ideal (a, b, sub(F, y=>1));

for i in pd do
(
    r = radical i;
    if isSubset(ideal z, r) then (
        tjurina = append(tjurina, toString new Array from r_*);
        degs_t = append(degs_t, degree i);

    )

)

-- y, z
a = partials_(1, 0);
a = sub(a, x=>1);

b = partials_(2, 0);
b = sub(b, x=>1);

pd = primaryDecomposition ideal (a, b);
-- print(pd/degree, pd/radical);

for i in pd do
(
    r = radical i;
    if isSubset(ideal z, r) and isSubset(ideal y, r) then (
        milnor = append(milnor, toString new Array from r_*);
        degs_m = append(degs_m, degree i);
    )
)

pd = primaryDecomposition ideal (a, b, sub(F, x=>1));

for i in pd do
(
    r = radical i;
    if isSubset(ideal z, r) and isSubset(ideal y, r) then (
        tjurina = append(tjurina, toString new Array from r_*);
        degs_t = append(degs_t, degree i);
    )

)
print(degs_m);
print(milnor);
print(degs_t);
print(tjurina);

