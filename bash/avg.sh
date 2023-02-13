#!/bin/bash
read -p "Enter valuse for N: " n 

sum=0
for ((a=0;a<n;a++)); do 
    read -p "Enter $((a+1)) : " num
    sum=$((sum + num))
done



result=$(echo "$sum/$n" | bc -l)

printf "%.3f" $result