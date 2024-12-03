from pathlib import Path 
import re

day03_data_path = Path('/home/toomeh/for-fun/aoc-2024/day03/day03_data.txt')


testcase = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'




#######################################################################
# Part 1 
#######################################################################

pattern_1 = r"mul\((-?\d+),(-?\d+)\)"

# Regex explanation 
# mul\( matches "mul(" 
# (-?\d+) "-?" captures the character "-" zero or one times, this allows us to catch a negative if it is there. Then "d+" recursively captures digits
# , captures ","
# capture digits with optional minus sign as before 
# "\)" matches a closing parentheses

part_1_result = 0

with open(day03_data_path, 'r') as file:
    data = file.read()



# Find all matches using the pattern
matches = re.findall(pattern_1, data)

# Print the matches
for match in matches:
    part_1_result += (int(match[0]) * int(match[1]))


print(f'The result for part 1 is: {part_1_result}')


#######################################################################
# Part 2 
#######################################################################

pattern_2 = r"mul\((\d+),(\d+)\)|(do\(\))|(don't\(\))"
testcase_2 = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

flag = True

part_2_result = 0

for a, b, do, dont in re.findall(pattern_2, data):

    if do or dont:
        flag = bool(do)
    else:
        part_2_result += int(a)*int(b) * flag

print(f'The result of part 2 is: {part_2_result}')