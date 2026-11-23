#!/bin/bash
cd /home/claude/hasavta-shelanu/tools/ruche_2311
R=/root/r2311; export DSF=1.5
( for w in cool:t_cool romantic:t_romantic smart:t_smart; do n=${w%%:*}; h=${w##*:}; rm -rf $R/$n $R/${n}_i30; SHX="{\"who\":\"$h\"}" python3 film.py $R/$n cu 3.4; done ) > $R/logc1.txt 2>&1 &
( for w in party:t_party queen:t_queen; do n=${w%%:*}; h=${w##*:}; rm -rf $R/$n $R/${n}_i30; SHX="{\"who\":\"$h\"}" python3 film.py $R/$n cu 3.4; done ) > $R/logc2.txt 2>&1 &
wait
