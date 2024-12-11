from pathlib import Path
from collections import defaultdict

def parse_input_brute(input):
    str_list = input.split(' ')
    return [int(num) for num in str_list]




def update_stone_brute(stone:int):
    stone_string = str(stone)
    if stone == 0:
        return [1]
    elif len(stone_string) % 2 == 0:
        middle_index = len(stone_string) // 2 
        stone_1, stone_2 = int(stone_string[:middle_index]), int(stone_string[middle_index:])
        return [stone_1, stone_2]
        
    else:
        return [stone * 2024]
    
def blink_brute(stones):
    result = []
    for stone in stones:
        updated_stones = update_stone_brute(stone)
        for updated in updated_stones:
            result.append(updated)

    return result 

def parse_input(input):
    str_list = input.split(' ')

    stones = defaultdict(int)
    for stone in str_list:
        stones[int(stone)] += 1 
    return stones

def blink(stones):
    stonework = dict(stones)
    for stone, count in stonework.items():
        if count == 0: continue
        if stone == 0:
            stones[1] += count
            stones[0] -= count
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            new_len = int(len(stone_str) / 2)
            stone_1 = int(stone_str[:new_len])
            stone_2 = int(stone_str[new_len:])
            stones[stone_1] += count
            stones[stone_2] += count
            stones[stone] -= count
        else:
            stones[stone * 2024] += count
            stones[stone] -= count
    return    

def blink_times(blinks, stones):
    for i in range(blinks):
        blink(stones)
        # print(i, len(stones))
    return 



def main():


    data_path = Path('/home/toomeh/for-fun/aoc-2024/day11/day11_data.txt')
    with open(data_path, 'r') as file:
        data = file.read()

    stones = parse_input(data)
    blink_times(75, stones)

    print(sum(stones.values()))



if __name__ == '__main__':
    main()