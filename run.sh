#!/bin/bash
touch solutions.txt
M2 --script solve_all.m2 $1 > solutions.txt;
python3 solve_singularities.py;
python3 solve_multiplicities.py;
cat sings_solution.txt >> solutions.txt;
M2 --script solve_all2.m2 >> solutions.txt;
# delete warnings
sed -i '/--/d' solutions.txt;
