from pathlib import Path
import re 
def determinant(a, b, c, d):
    return a*d - b*c

def parse_input(lines):
    # Remove every 4th entry
    filtered_lines = [line for i, line in enumerate(lines) if (i + 1) % 4 != 0]

    # Group remaining entries into groups of three
    grouped_lines = [filtered_lines[i:i+3] for i in range(0, len(filtered_lines), 3)]
    
    extracted_numbers = [
    [[int(num) for num in re.findall(r'\d+', line)] for line in group] 
    for group in grouped_lines]
    return extracted_numbers


def solve_game(extracted_numbers, part_2=False):
    x1, y1 = extracted_numbers[0]
    x2, y2 = extracted_numbers[1]
    c, d = extracted_numbers[2]
    if part_2:
        c += 10000000000000
        d += 10000000000000 
    result = 0
    a = (c*y2 - d*x2) / (x1*y2 - y1*x2)
    b = (d*x1 - c*y1) / (x1*y2 - y1*x2)
    if a == int(a) and b == int(b):
        result = int(3 * a + b)    
    
    return result




def main():
    testcase_path = Path('/home/toomeh/for-fun/aoc-2024/day13/day13_testcase.txt')
    with open(testcase_path, 'r') as file:
        testcase_lines = file.read().split('\n')

    testcase_result = 0

    testcase_extracted_numbers = parse_input(testcase_lines)
    for game in testcase_extracted_numbers:
        testcase_result += solve_game(game)

    data_path = Path('/home/toomeh/for-fun/aoc-2024/day13/day13_data.txt')
    with open(data_path, 'r') as file:
        lines = file.read().split('\n')
    result_1 = 0 
    extracted_numbers = parse_input(lines)
    for game in extracted_numbers:
        result_1 += solve_game(game)

    print(f'Part 1 result: {result_1}')
    result_2 = 0
    for game in extracted_numbers:
        result_2 += solve_game(game, part_2=True)

    print(f'Part 2 result: {result_2}')

if __name__ == '__main__':
    main()