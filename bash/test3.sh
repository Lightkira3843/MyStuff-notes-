#!/bin/bash

while [[ $1 =~ ^- ]];do
	case $1 in 
	-v)
		echo "Version 0.0.1"
		exit
		;;
	-f)
	shift; f_name=$1
	;;
	-m)
	shift; m_name=$1
	;;
	-l)
	shift; l_name=$1
	;;
	* | -h)
	echo "Useage: $0 [vhfl]"
	echo "Example: $0 [-f first_name -l last_name]"
	exit
	;;
	esac;shift;done

if [[ -z $f_name ]]; then
	echo "Error: enter you name 0 $0 1 $1 "

else
	echo "hii , $f_name $m_name $l_name 0 $0 1 $1 2 $2"
fi