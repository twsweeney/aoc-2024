#!/bin/bash

# Loop through numbers 1 to 25
for n in {1..25}; do

# Zero-pad the number to ensure two digits
  dir_name=$(printf "day%02d" $n)
  
  # Create the directory
  mkdir "$dir_name"

 
  
  # Create the three files inside the directory
  touch "$dir_name/${dir_name}_puzzle.txt" "$dir_name/${dir_name}_data.txt" "$dir_name/${dir_name}_solution.py"
done

echo "Directories and files created successfully!"
