-- Setup
S = QQ[x,y,z];

f = value scriptCommandLine#1;

F = homogenize(f, z)
partials = jacobian F;

-- Milnor / Tjurina
-- x, y
-- partial derivative corresponding to x
a = partials_(0, 0);
a = sub(a, z=> 1);

-- partial derivative corresponding to y
b = partials_(1, 0);
b = sub(b, z=> 1);

pd = primaryDecomposition ideal (a, b);

milnor = [new Array from pd/degree]
for i in pd/radical do
    milnor = append(L, toString new Array from i_*)


pd = primaryDecomposition ideal (a, b, sub(F, z=>1));

tjurina = [new Array from pd/degree]
for i in pd/radical do
    tjurina = append(L, toString new Array from i_*)




-- x, z
a = partials_(0, 0)
a = sub(a, y=>1)

b = partials_(2, 0)
b = sub(b, y=>1)

pd = primaryDecomposition ideal (a, b)
milnor = append(milnor#0, new Array from pd/degree)
for i in pd/radical do
    milnor = append(milnor, toString new Array from i_*)


print(L)
pd = primaryDecomposition ideal (a, b, sub(F, y=>1));

L = [new Array from pd/degree]
for i in pd/radical do
    L = append(L, toString new Array from i_*)


print(L)
-- y, z
a = partials_(1, 0)
a = sub(a, x=>1)

b = partials_(2, 0)
b = sub(b, x=>1)

pd = primaryDecomposition ideal (a, b)
L = [new Array from pd/degree]
for i in pd/radical do
    L = append(L, toString new Array from i_*)


print(L)
pd = primaryDecomposition ideal (a, b, sub(F, x=>1));

L = [new Array from pd/degree]
for i in pd/radical do
    L = append(L, toString new Array from i_*)


print(L)
