#!/bin/bash


source test.sh  

case $1 in
	10 )
	echo " 10 ? "
		;;
	[A-Z])
	echo "there is only CAPS"
	;;
	*)
	echo "$1 is something else "
	exit
esac

# myfunc $1 $2