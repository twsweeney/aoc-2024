
from pathlib import Path

day05_data_path = Path('/home/toomeh/for-fun/aoc-2024/day05/day05_data.txt')

with open(day05_data_path, 'r') as file:
    data = file.read().strip().split('\n')



def nums(l, char):
    return list(map(int, l.strip().split(char)))

def wrong(p,x,y):
    return x in p and y in p and p.index(x) > p.index(y)

def fix(p):
    for x,y in rules:
        if wrong(p,x,y):
            p[p.index(x)], p[p.index(y)] = y, x 
            return fix(p)
    return p

def get_middles(pages):
    return [p[len(p)//2] for p in pages]

lines = [line.strip() for line in data]

rules = [nums(l, "|") for l in lines if "|" in l]
pages = [nums(l, ",") for l in lines if "," in l]

correct = [p for p in pages if not any([wrong(p,x,y) for x,y in rules])]
fixed = [fix(p) for p in pages if p not in correct]
        
print("part1:",sum(get_middles(correct)))
print("part2:",sum(get_middles(fixed)))