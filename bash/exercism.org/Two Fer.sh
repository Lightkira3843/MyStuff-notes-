#!/bin/bash

main (){
    read -p "Enter name: " name
    echo "One for ${name:-you}, one for me. "
}
main "$@"


