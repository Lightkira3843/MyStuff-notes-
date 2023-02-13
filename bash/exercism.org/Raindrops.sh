#!/bin/bash


  main () {

    if [[ $1==1 ]]; then
        echo "$1"
    fi

    if [ $(($1%3 )) -eq 0 ]; then
        if ([ $(($1%5)) -eq 0 ] || [ $((1%7)) -eq 0 ]); then
            echo "PlingPlang"
       
    else
        echo "Pling"
   
        fi
    fi

    if [ $(($1%5)) -eq 0 ]; then
        if ( [ $(($1%3)) -eq 0 ] || [ $(($1%7)) -eq 0 ] ); then
            echo "PlingPlang"
       
    else
        echo "Pling"
   
        fi
    fi

    if [ $(($1%7)) -eq 0 ]; then
        if ( [ $(($1%5)) -eq 0 ] || [ $(($1%3)) -eq 0 ] ); then
            echo "PlingPlang"
       
    else
        echo "Pling"
   
        fi
    fi
}



  main 1