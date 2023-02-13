#!/bin/bash


clear

echo -e "\033[5;38;5;6m HERE IS MY FIRST BASH COMMAND COMMAND !!\033[0m"

beautify(){
	rest_colore="\033[0m"
	echo -e "\033[0;38;5;$1m$2$rest_colore"
}

my_func(){
	
	echo """
		Enter 1 for -> for saprating files with size 
		Enter 2 for ->
		Enter 3 for ->
		Enter 4 for ->
		"""

	read -p "Enter ur opt: " opt

#first condition

	if [[ $opt == 1 ]]; then
		echo "ur choise is 1"
		read -p "Enter Extentions saprated by , : " ext
		echo -e "\033[5;38;5;1m \t NOTE: default size is 1MB and just Enter A Number A for a size it will take it in MBs!!\033[0m "
		read -p "Enter size in mbs  : " size
		find . -name "*.${ext:-*}" -size +${size:-1}M > lst.txt
		file="lst.txt"
		cat lst.txt
		mkdir ./here 
		c=1
		x=1
		while read -r line; do
			beautify $c " $line             file -> $x"
			cp $line ./here
			((c+=3))
			((x++))
		done <$file
		echo -e  "\033[5;38;5;7m The OPERATION HAS SUCCESSFULLY COMPLETED BABY !! \033[0m ;)"






	elif [[ $opt == 2 ]]; then
		echo "your choise is 2"
	elif [[ $opt == 3 ]]; then
		echo "your choise is 3"
	elif [[ $opt == 4 ]]; then
		echo "your choise is 4"
	else
		echo "INVALID INPUT !! " >&2
		exit 1
	fi
}

my_func

