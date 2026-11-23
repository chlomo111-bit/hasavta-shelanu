#!/bin/bash
N=/root/three3/node_modules; R=/root/w2; F=/home/claude/hsh/tools/hashchenim_2311s/film.py; export DSF=1.4
T0=1.79 T1=3.1 T2=4.4 BT=5.22,5.57,5.92 python3 $F $N $R/top top 6.95 10 &
python3 $F $N $R/end end 2.0 10 &
wait; echo DONE
