#!/bin/bash
for sh in "$@"; do n=${sh%%:*}; r=${sh#*:}; RANGE=$r NOTEXT=1 DSF=1.2 NOSH=1 python3 film.py /root/three3/node_modules /root/sv/$n 3 > /root/sv/$n.log 2>&1; done
