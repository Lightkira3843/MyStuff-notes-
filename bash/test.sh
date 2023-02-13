#!/usr/bin/bash



name="deekshant kumar" #global variable 

myfunc(){
	if (( $1 > $2 )); then
		echo "$1 is grater then $2." 
	else
		echo "nope $1 isn't grater then $2."
	fi
}

myfunc $1 $2
 

 