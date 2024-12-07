from pathlib import Path 
from math import log10

def parse_line(input):

    target_value, nums = input.split(': ') 

    nums_list  = list(map(int, nums.split(' ')))
    
    return int(target_value), nums_list


def digits(n):
    return int(log10(n)) + 1

def endswith(a, b):
    return (a - b) % 10 ** digits(b) == 0


def test_combinations(target_value, numbers, check_concat=True):
    if type(numbers) == int:
        n = numbers
        head = None
    else:
        n = numbers[-1]
        head = numbers[:-1]

    if not head:
        return target_value == n 
    # Check if the target is divisible by the current target
    q, r = divmod(target_value, n)
    if r == 0 and test_combinations(q, head, check_concat):
        return True
    
    if check_concat and endswith(target_value, n) and test_combinations(target_value// (10**digits(n)), head, check_concat):
        return True

    # If not divisble check subtractiobn
    return test_combinations(target_value - n, head, check_concat)

def solve(data):
    result_1 = 0
    result_2 = 0
    for line in data:

        test_value, numbers = parse_line(line)
        if test_combinations(test_value, numbers, False):
            result_1 += test_value
            result_2 += test_value 
        elif test_combinations(test_value, numbers, True):
            result_2 += test_value 
    
    return result_1, result_2








def main():
    day07_testcase_path = Path('/home/toomeh/for-fun/aoc-2024/day07/day07_testcase.txt')
    with open(day07_testcase_path, 'r') as file:
        testcase_data = file.read().split('\n')
    testcase_result_1, testcase_result_2 = solve(testcase_data)
    expected_testcase_result_1 = 3749
    expected_testcase_result_2 = 11387

    if testcase_result_1 == expected_testcase_result_1:
        print('Testcase 1 passed')
    else:
        print(f'Testcase 1 failed, Result: {testcase_result_1}')   

    if testcase_result_2 == expected_testcase_result_2:
        print('Testcase 2 passed')
    else:
        print(f'Testcase 2 failed, Result: {testcase_result_2}')  

    day07_data_path = Path('/home/toomeh/for-fun/aoc-2024/day07/day07_data.txt')
    with open(day07_data_path, 'r') as file:
        data = file.read().split('\n')
    result_1, result_2 = solve(data)
    print(f'Part 1 Result: {result_1}')
    print(f'Part 2 Result: {result_2}')

if __name__ == '__main__':
    main()