-- Setup
S = QQ[w,x,y,z];

f = value scriptCommandLine#1;

F = homogenize(f, w);
partials = jacobian F;
-- Degree
print (degree f)#0;

-- Singular Points
p = sub(F, x=>1);
q = sub(F, y=>1);
r = sub(F, z=>1);
s = sub(F, w=>1);

print(toString(F));

L = []

singularities = ideal jacobian p + ideal p;
pd = primaryDecomposition(singularities);

for i in pd do (
    L = append(L, toString new Array from i_*);
)

pd = primaryDecomposition radical ((ideal jacobian p) + ideal p);

for i in pd do (
    L = append(L, toString new Array from i_*);
)

singularities = ideal jacobian q + ideal q;
pd = primaryDecomposition(singularities);

for i in pd do (
    L = append(L, toString new Array from i_*);
)

pd = primaryDecomposition radical ((ideal jacobian q) + ideal q);

for i in pd do (
    L = append(L, toString new Array from i_*);
)

singularities = ideal jacobian r + ideal r;
pd = primaryDecomposition(singularities);

for i in pd do (
    L = append(L, toString new Array from i_*);
)

pd = primaryDecomposition radical ((ideal jacobian r) + ideal r);

for i in pd do (
    L = append(L, toString new Array from i_*);
)

singularities = ideal jacobian s + ideal s;
pd = primaryDecomposition(singularities);

for i in pd do (
    L = append(L, toString new Array from i_*);
)

pd = primaryDecomposition radical ((ideal jacobian s) + ideal s);

for i in pd do (
    L = append(L, toString new Array from i_*);
)

print(L)

-- Milnor / Tjurina
-- x, y, z
-- partial derivative corresponding to x
-- a = partials_(1, 0);
-- a = sub(a, w=> 1);

-- -- -- partial derivative corresponding to y
-- b = partials_(2, 0);
-- b = sub(b, w=> 1);

-- -- -- partial derivative corresponding to z
-- c = partials_(3, 0);
-- c = sub(c, w=> 1);



-- pd = primaryDecomposition ideal (a, b, c);

-- degs_m = new Array from pd/degree;
-- milnor = [];
-- for i in pd do
-- (
--     r = radical i;
--     milnor = append(milnor, toString new Array from r_*);
-- )

-- pd = primaryDecomposition ideal (a, b, c, sub(F, w=>1));

-- degs_t = new Array from pd/degree;
-- tjurina = [];
-- for i in pd do
-- (
--     r = radical i;
--     tjurina = append(tjurina, toString new Array from r_*);
-- )



-- -- w, y, z
-- a = partials_(0, 0);
-- a = sub(a, x=>1);

-- b = partials_(2, 0);
-- b = sub(b, x=>1);

-- c = partials_(3, 0);
-- c = sub(c, x=>1);

-- pd = primaryDecomposition ideal (a, b, c);

-- for i in pd do
-- (
--     r = radical i;
--     if isSubset(ideal w, r) then (
--         milnor = append(milnor, toString new Array from r_*);
--         degs_m = append(degs_m, degree i);
--     )
-- )

-- pd = primaryDecomposition ideal (a, b, c, sub(F, x=>1));

-- for i in pd do
-- (
--     r = radical i;
--     if isSubset(ideal w, r) then (
--         tjurina = append(tjurina, toString new Array from r_*);
--         degs_t = append(degs_t, degree i);

--     )
-- )

-- -- w, x, z
-- a = partials_(0, 0);
-- a = sub(a, y=>1);

-- b = partials_(1, 0);
-- b = sub(b, y=>1);

-- c = partials_(3, 0);
-- c = sub(c, y=>1);

-- pd = primaryDecomposition ideal (a, b, c);

-- for i in pd do
-- (
--     r = radical i;
--     if isSubset(ideal w, r) and isSubset(ideal x, r) then (
--         milnor = append(milnor, toString new Array from r_*);
--         degs_m = append(degs_m, degree i);
--     )
-- )

-- pd = primaryDecomposition ideal (a, b, c, sub(F, y=>1));

-- for i in pd do
-- (
--     r = radical i;
--     if isSubset(ideal w, r) and isSubset(ideal x, r) then (
--         tjurina = append(tjurina, toString new Array from r_*);
--         degs_t = append(degs_t, degree i);
--     )
-- )

-- -- w, x, y
-- a = partials_(0, 0);
-- a = sub(a, z=>1);

-- b = partials_(1, 0);
-- b = sub(b, z=>1);

-- c = partials_(2, 0);
-- c = sub(c, z=>1);

-- pd = primaryDecomposition ideal (a, b, c);

-- for i in pd do
-- (
--     r = radical i;
--     if isSubset(ideal w, r) and isSubset(ideal x, r) and isSubset(ideal y, r) then (
--         milnor = append(milnor, toString new Array from r_*);
--         degs_m = append(degs_m, degree i);
--     )
-- )

-- pd = primaryDecomposition ideal (a, b, c, sub(F, z=>1));

-- for i in pd do
-- (
--     r = radical i;
--     if isSubset(ideal w, r) and isSubset(ideal x, r) and isSubset(ideal y, r)then (
--         tjurina = append(tjurina, toString new Array from r_*);
--         degs_t = append(degs_t, degree i);
--     )
-- )

-- Milnor / Tjurina
-- x, y, z
-- partial derivative corresponding to x
a = partials_(1, 0);
a = sub(a, w=> 1);

-- partial derivative corresponding to y
b = partials_(2, 0);
b = sub(b, w=> 1);

-- partial derivative corresponding to z
c = partials_(3, 0);
c = sub(c, w=> 1);



pd = primaryDecomposition ideal (a, b, c);

degs_m = new Array from pd/degree;
milnor = [];
for i in pd do
(
    r = radical i;
    milnor = append(milnor, toString new Array from r_*);
)

pd = primaryDecomposition ideal (a, b, c, sub(F, w=>1));

degs_t = new Array from pd/degree;
tjurina = [];
for i in pd do
(
    r = radical i;
    tjurina = append(tjurina, toString new Array from r_*);
)



-- w, y, z
a = partials_(0, 0);
a = sub(a, x=>1);

b = partials_(2, 0);
b = sub(b, x=>1);

c = partials_(3, 0);
c = sub(c, x=>1);

pd = primaryDecomposition ideal (a, b, c);

for i in pd do
(
    r = radical i;
    milnor = append(milnor, toString new Array from r_*);
    degs_m = append(degs_m, degree i);
)

pd = primaryDecomposition ideal (a, b, c, sub(F, x=>1));

for i in pd do
(
    r = radical i;
    tjurina = append(tjurina, toString new Array from r_*);
    degs_t = append(degs_t, degree i);
)

-- w, x, z
a = partials_(0, 0);
a = sub(a, y=>1);

b = partials_(1, 0);
b = sub(b, y=>1);

c = partials_(3, 0);
c = sub(c, y=>1);

pd = primaryDecomposition ideal (a, b, c);

for i in pd do
(
    r = radical i;
    milnor = append(milnor, toString new Array from r_*);
    degs_m = append(degs_m, degree i);
)

pd = primaryDecomposition ideal (a, b, c, sub(F, y=>1));

for i in pd do
(
    r = radical i;
    tjurina = append(tjurina, toString new Array from r_*);
    degs_t = append(degs_t, degree i);
)

-- w, x, y
a = partials_(0, 0);
a = sub(a, z=>1);

b = partials_(1, 0);
b = sub(b, z=>1);

c = partials_(2, 0);
c = sub(c, z=>1);

pd = primaryDecomposition ideal (a, b, c);

for i in pd do
(
    r = radical i;
    milnor = append(milnor, toString new Array from r_*);
    degs_m = append(degs_m, degree i);
)

pd = primaryDecomposition ideal (a, b, c, sub(F, z=>1));

for i in pd do
(
    r = radical i;
    tjurina = append(tjurina, toString new Array from r_*);
    degs_t = append(degs_t, degree i);
)
print(degs_m);
print(milnor);
print(degs_t);
print(tjurina);
