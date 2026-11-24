#!/bin/bash
N=/root/three3/node_modules; R=/root/w3; F=$(dirname $0)/film.py; export DSF=1.2
python3 $F $N $R/wide wide 2.7 10 &
python3 $F $N $R/stair stair 9.5 10 &
wait
BT=2.3,2.65,3.0,3.35,3.7 python3 $F $N $R/top top 5.0 10 &
python3 $F $N $R/end end 2.6 10 &
wait; echo DONE
