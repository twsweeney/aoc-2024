from pathlib import Path
def expand(data):
    n = len(data)
    result = []

    for i in range(n):
        if i % 2 == 0:
            result.extend([i//2] * int(data[i]))
        else: 
            result.extend([None] * int(data[i]))
    return result

def fill(data):
    
    for i in range(len(data)-1, -1, -1):
        if data[i] is None:
            continue
        for j in range(i):
            if data[j] is None:
                data[j], data[i] = data[i], None
                break
    return data

def verify_fill(data):

    for i, char in enumerate(data):
        if char != '.':
            continue
        else:
            empty_index = i
            break
    
    empty = set(data[empty_index:])
    return len(empty) == 1





def solve_1(data):
    result = 0
    for i in range(len(data)):
        if data[i] is not None:
            result += i * data[i]

    return result


def main():

    testcase = '2333133121414131402' 
    data_path = Path('/home/toomeh/for-fun/aoc-2024/day09/day09_data.txt')

    
    testcase_expanded = expand(testcase)
    testcase_filled_result = fill(testcase_expanded)
    testcase_result_1 = solve_1(testcase_filled_result)
    expected_testcase_result_1 = 1928
    if testcase_result_1 == expected_testcase_result_1:

        print('Testcase Passed!')
    else:
        print(f'Testcase failed, result = {testcase_result_1}')



    with open(data_path, 'r') as file:
        data = file.read()

    
    expanded_data = expand(data)
    filled_result = fill(expanded_data)


    result_1 = solve_1(filled_result)
    print(f'Part 1 Result: {result_1}')
    
    

if __name__ == '__main__':
    main()