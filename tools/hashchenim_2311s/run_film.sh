#!/bin/bash
# tourne les 5 plans (2 en parallèle)
N=/root/three3/node_modules; R=/root/w2; F=/home/claude/hsh/tools/hashchenim_2311s/film.py; export DSF=${DSF:-1.4}
mkdir -p $R
python3 $F $N $R/wide wide 3.53 10 &
python3 $F $N $R/lift lift 5.75 10 &
wait
python3 $F $N $R/reveal reveal 1.5 10 &
T0=1.79 T1=3.1 T2=4.4 BT=5.22,5.57,5.92 python3 $F $N $R/top top 6.95 10 &
wait
python3 $F $N $R/end end 2.0 10
