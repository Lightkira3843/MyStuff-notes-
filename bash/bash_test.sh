#!/bin/bash

filename="words.txt"
declare -a words

while read -r line; do
  words+=($line)
done < "$filename"

echo "Words in the file:"
for word in "${words[@]}"; do
  echo "$word"
done




# # i need to explain it to myself !!!

# read n
# arr=($(cat))

# echo "${arr[@]}" | tr ' ' '\n' |sort | uniq -u | tr '\n' ' '