#!/bin/bash
cd /home/claude/hasavta-shelanu/tools/savta_2311
for sh in "$@"; do n=${sh%%:*}; r=${sh#*:}; RANGE=$r NOTEXT=1 DSF=1.2 NOSH=1 python3 film.py /root/three3/node_modules /root/sv/h/$n 1 > /root/sv/h/$n.log 2>&1; done
