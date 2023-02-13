#!/bin/bash

# Function to generate a fractal tree
generate_tree() {
  local depth=$1
  local size=$2
  local i
  local j

  # Base case
  if [ "$depth" -eq 0 ]; then
    return
  fi

  # Draw the horizontal line
  for i in $(seq $size); do
    echo -n "_"
  done

  # Draw the two slanting lines
  for i in $(seq $depth); do
    for j in $(seq $((size - i))); do
      echo -n " "
    done
    echo -n "/"
    for j in $(seq $((2 * i - 2))); do
      echo -n "_"
    done
    echo "\\"
  done

  # Recursively call the function for the two branches
  generate_tree $((depth - 1)) $((size / 2))

  for i in $(seq $depth); do
    for j in $(seq $((size - i))); do
      echo -n " "
    done
    echo -n "\\"
    for j in $(seq $((2 * i - 2))); do
      echo -n "_"
    done
    echo "/"
  done

  # Draw the horizontal line
  for i in $(seq $size); do
    echo -n "_"
  done
  echo
}

# Get the number of iterations from the user
read -p "Enter the number of iterations: " iterations

# Call the function to generate the fractal tree
generate_tree $iterations 16