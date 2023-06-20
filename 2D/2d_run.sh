#!/bin/bash
touch 2d_solutions.txt;
M2 --script 2d_solve_all.m2 $1 > 2d_solutions.txt;
python3 2d_solve.py;
