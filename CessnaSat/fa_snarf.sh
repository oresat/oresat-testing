#!/bin/bash

tail=$1
curl -s 'https://flightaware.com/live/flight/${tail}/history/20220501/2233Z/tracklog' |
    hxnormalize -x |
    hxselect -c 'span.show-for-medium-up:first-child' -s '\n' |
    grep -v img | tail -4 | grep -v : | xargs echo |
    while read lat lon alt; do
	./plane_oneshot.py $lat $lon ${alt/,/}
    done
