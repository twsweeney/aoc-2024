from pathlib import Path 

day02_data_path = Path('/home/toomeh/for-fun/aoc-2024/day02/day02_data.txt')
day02_testcase_path = Path('/home/toomeh/for-fun/aoc-2024/day02/day02_testcase.txt')



def is_safe(report):
        differs = [a - b for a, b in zip(report, report[1:])]
        is_monotonic = all(i > 0 for i in differs) or all(i < 0 for i in differs)
        is_in_range = all(0 < abs(i) <= 3 for i in differs)
        if is_monotonic and is_in_range:
            return True
        return False






#######################################################################
# Part 1 
#######################################################################
part_1_result = 0

with open(day02_data_path, 'r') as data:
    for line in data:
        string_list = line.strip().split(' ')
        report = list(map(int, string_list))
        if is_safe(report):
            part_1_result += 1 

         
print(f' The part 1 result is: {part_1_result}')


        

#######################################################################
# Part 2 
#######################################################################

part_2_result = 0


with open(day02_data_path, 'r') as data:
    for line in data:
        string_list = line.strip().split(' ')
        report = list(map(int, string_list))
        if is_safe(report):
            part_2_result += 1 
        else:
             # check all combinations of the report excluding each element and check
             for i in range(len(report)):
                  report_excluding_i = report[:i] + report[i+1:]
                  if is_safe(report_excluding_i):
                       part_2_result +=1 
                       break
        


print(f' The part 2 result is: {part_2_result}')