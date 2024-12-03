#!/bin/bash

# Loop through numbers 1 to 25
for n in {1..25}; do
  # Create the directory
  mkdir "day$n"
  
  # Create the three files inside the directory
  touch "day$n/day${n}_puzzle.txt" "day$n/day${n}_data.txt" "day$n/day${n}_solution.py"
done

echo "Directories and files created successfully!"
