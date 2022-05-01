#!/bin/bash

beacons() {
    rtl_fm -f 436.5M -s 22050 -p 38 |
	~/multimon-ng/build/multimon-ng -q -a FSK9600 -t raw -m --timestamp /dev/stdin |
	tee -a beacon.log
}

get_byte() {
    local offset=$((0x$2 * 2))
    echo ${1:offset:2}
}

get_word() {
    local offset=$((0x$2 * 2))
    local word=${1:offset:8}
    echo ${word:6:2}${word:4:2}${word:2:2}${word:0:2}
}

get_half() {
    local offset=$((0x$2 * 2))
    local word=${1:offset:4}
    echo ${word:2:2}${word:0:2}
}

twos() {
    echo "-$(((0x$1 - 1) ^ 0xFF))"
}

hex2dec() {
    echo $((0x$1))
}

parse() {
    echo $(date '+%F %T') \
	'L_valid:'$(hex2dec $(get_word $1 25)) \
	'L_rssi:'$(twos $(get_byte $1 29)) \
	'U_valid:'$(hex2dec $(get_word $1 2e)) \
	'U_rssi:'$(twos $(get_byte $1 32)) \
	'P1VBatt:'$(hex2dec $(get_half $1 3c))
}

beacons |
    while read d t beacon j; do
	[ "$beacon" = "FSK9600:" ] && continue
	parse $beacon
    done
