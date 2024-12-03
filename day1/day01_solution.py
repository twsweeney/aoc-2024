from pathlib import Path

data_path = Path('/home/toomeh/for-fun/aoc-2024/day1/day1_data.txt')

list_1 = []
list_2 = []

with open(data_path, 'r') as data:
    for line in data:
        list_1_element, list_2_element = line.strip().split('   ')
        list_1.append(int(list_1_element))
        list_2.append(int(list_2_element))


#######################################################################
# Part 1 
#######################################################################

# python sort is O(nlogn)
list_1_sorted = sorted(list_1)
list_2_sorted = sorted(list_2)

n = len(list_1_sorted)
part_1_result = 0

for i in range(n):
    part_1_result += abs(list_1_sorted[i] - list_2_sorted[i])

print(f'The result of part 1 is: {part_1_result}')
        

#######################################################################
# Part 2 
#######################################################################

from collections import Counter

list_2_counter = Counter(list_2)


part_2_result = 0

for i in range(n):
    part_2_result += (list_1[i] * list_2_counter[list_1[i]])

print(f'The result of part 2 is: {part_2_result}')

