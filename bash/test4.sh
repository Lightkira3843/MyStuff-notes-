#!/bin/bash



beautyfy(){
	rest_colore="\033[0m"
	echo -e "\033[0;38;5;$1m$2$rest_colore" # put 5 at the place of 0 for making text blinking 
}



for x in {0..256};do
	beautyfy $x "this colore is at { $x }"
done
 