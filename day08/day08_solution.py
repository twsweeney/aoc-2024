from pathlib import Path
class AntennaMap:
    def __init__(self, map_data:str):
        self.map = [list(line) for line in map_data.strip().split('\n')]
        self.n_rows = len(self.map)
        self.n_columns = len(self.map[0])
        self.antenna_locations = {}
        self.valid_antinodes = set()


    def get_antinodes(self, i1, j1, i2, j2):

        dy = abs(i1-i2)
        dx = abs(j1-j2)

        if i1 > i2:
            an_i_1 = i1 + dy
            an_i_2 = i2 - dy
        else:
            an_i_1 = i1 - dy
            an_i_2 = i2 + dy
        if j1 > j2:
            an_j_1 = j1 + dx
            an_j_2 = j2 - dx
        else:
            an_j_1 = j1 - dx
            an_j_2 = j2 + dx

        return (an_i_1, an_j_1), (an_i_2, an_j_2)
    

    def get_antinodes_2(self, i1, j1, i2, j2):
        dy = abs(i1-i2)
        dx = abs(j1-j2)      

        one_plus_dy = i1 > i2
        one_plus_dx = j1 > j2

        antinodes = []

        while True:
            if one_plus_dy:
                new_i = i1 + dy
            else:
                new_i = i1 - dy
            
            if one_plus_dx:
                new_j = j1 + dx 
            
            else: 
                new_j = j1 - dx
            
            if self.in_bounds(new_i, new_j):
                i1 = new_i
                j1 = new_j
                antinodes.append((new_i, new_j))
            else:
                break

        while True:
            if one_plus_dy:
                new_i = i2 - dy
            else:
                new_i = i2 + dy
            
            if one_plus_dx:
                new_j = j2 - dx 
            
            else: 
                new_j = j2 + dx
            
            if self.in_bounds(new_i, new_j):
                i2 = new_i
                j2 = new_j
                antinodes.append((new_i, new_j))
            else:
                break

        return antinodes



    def in_bounds(self, i, j) -> bool:
        return (0<=i<self.n_rows and 0<=j<self.n_columns)
    
    def search(self):
        for i in range(self.n_rows):
            for j in range(self.n_columns):
                current_char = self.map[i][j]
                if current_char == '.':
                    continue


                if current_char not in self.antenna_locations:
                    self.antenna_locations[current_char] = [(i,j)]
                else:
                    for antenna in self.antenna_locations[current_char]:
                        an1, an2 = self.get_antinodes(i, j, antenna[0], antenna[1])

                        if self.in_bounds(an1[0], an1[1]):
                            self.valid_antinodes.add(an1)

                        if self.in_bounds(an2[0], an2[1]):
                            self.valid_antinodes.add(an2)

                    self.antenna_locations[current_char].append((i,j))

        return len(self.valid_antinodes)
    

    def search_2(self):
        for i in range(self.n_rows):
            for j in range(self.n_columns):
                current_char = self.map[i][j]
                if current_char == '.':
                    continue
                


                if current_char not in self.antenna_locations:
                    self.antenna_locations[current_char] = [(i,j)]
                    self.valid_antinodes.add((i,j))
                else:
                    self.valid_antinodes.add((i,j))
                    for antenna in self.antenna_locations[current_char]:
                        antinodes = self.get_antinodes_2(i, j, antenna[0], antenna[1])
                        for antinode in antinodes:
                            self.valid_antinodes.add(antinode)
                        self.valid_antinodes.add(antenna)

                    self.antenna_locations[current_char].append((i,j))
    
        return len(self.valid_antinodes)
    

def main():
    testcase_path = Path('/home/toomeh/for-fun/aoc-2024/day08/day08_testcase.txt')
    with open(testcase_path, 'r') as file:
        testcase_data = file.read()
    data_path = Path('/home/toomeh/for-fun/aoc-2024/day08/day08_data.txt')
    with open(data_path, 'r') as file:
        data = file.read()
    
    # Part 1 Testcase 
    testcase_map = AntennaMap(testcase_data) 
    # testcase_result_1 = testcase_map.search()
    # expected_testcase_result_1 = 14
    # if testcase_result_1 == expected_testcase_result_1:
    #     print('Testcase passed')
    # else:
    #     print(f'Testcase failed, result: {testcase_result_1}')

    # Part 1 

    data_map = AntennaMap(data)
    # result_1 = data_map.search()
    # print(f'part 1 result: {result_1}')


    # Part 2 
    testcase_result_2 = testcase_map.search_2()
    expected_testcase_result_2 = 34
    if testcase_result_2 == expected_testcase_result_2:
        print('Testcase passed')
    else:
        print(f'Testcase failed, result: {testcase_result_2}')


    result_2 = data_map.search_2()
    print(result_2)

if __name__ == '__main__':
    main()




            


