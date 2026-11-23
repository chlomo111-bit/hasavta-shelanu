#!/bin/bash
cd /home/claude/hasavta-shelanu/tools/ruche_2311
R=/root/r2311; mkdir -p $R
export DSF=1.5
( python3 film.py $R/wide wide 4.5; python3 film.py $R/end end 4; for w in cool:t_cool romantic:t_romantic; do n=${w%%:*}; h=${w##*:}; SHX="{\"who\":\"$h\"}" python3 film.py $R/$n cu 3; done ) > $R/log1.txt 2>&1 &
( python3 film.py $R/demo demo 5.5; for w in smart:t_smart party:t_party queen:t_queen; do n=${w%%:*}; h=${w##*:}; SHX="{\"who\":\"$h\"}" python3 film.py $R/$n cu 3; done ) > $R/log2.txt 2>&1 &
