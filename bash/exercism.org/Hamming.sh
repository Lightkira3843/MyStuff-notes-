#!/bin/bash

  main () {
    if [[ "$#" -ne 2 ]]; then
        echo "Usage: hamming.sh <string1> <string2>" >&2
        exit 1
fi
	strand1=$1
	strand2=$2

	diff=0
    if [[ ${#strand1} == ${#strand2} ]]; then
    	for ((i=0;i<${#strand1};i++)); do
    	  if [ "${strand1:$i:1}" != "${strand2:$i:1}" ]; then
    	    ((diff++))
          fi
	    done
        echo "$diff"
    else
        echo "strands must be of equal length" >&2
        exit 1
    fi

}


  main 'gkkjjkjkjjdsf' 'ttsdf'
