from pathlib import Path 

class Map:
    def __init__(self, map_data) -> None:
        self.map = [list(line) for line in map_data.strip().split('\n')]
        self.n_rows = len(self.map)
        self.n_columns = len(self.map[0])
        self.visited = set()
        self.direction_map = {'up':(-1,0), 'down':(1,0), 'left':(0, -1), 'right':(0,1)}
        self.turn_map = {'up':'right', 'right':'down', 'down':'left', 'left':'up'}
        self.get_starting()



    
    def get_starting(self):
        guard_map = {'^':'up', '<':'left', '>':'right', 'v':'down'}

        for i in range(self.n_rows):
            for j in range(self.n_columns):
                if self.map[i][j] in guard_map.keys():
                    self.i_starting, self.j_starting = i, j
                    self.direction_starting = guard_map[self.map[i][j]]

    def step(self, i, j, direction):
        direction_step = self.direction_map[direction]
        if 0 <= i+direction_step[0] < self.n_rows and 0 <= j+direction_step[1] < self.n_columns:

            step_forward = self.map[i+direction_step[0]][j+direction_step[1]]
            if step_forward == '#':
                direction = self.turn_map[direction]
                return self.step(i, j, direction)
            else:
                return i+direction_step[0], j+direction_step[1], direction
        else:
            return i+direction_step[0], j+direction_step[1], direction
            
    
    def simulate(self):
        i, j, direction = self.i_starting, self.j_starting, self.direction_starting

        while 0 <= i < self.n_rows and 0 <= j < self.n_columns:
            self.visited.add((i, j))
            i, j, direction = self.step(i, j, direction)

    def fast_slow_simulate(self):
        # Fast slow pointer to detect a cycle. If fast and slow meet then there is a cycle

        i_fast, j_fast, direction_fast = self.i_starting, self.j_starting, self.direction_starting
        i_slow, j_slow, direction_slow = self.i_starting, self.j_starting, self.direction_starting

        while 0 <= i_fast < self.n_rows and 0 <= j_fast < self.n_columns:
            i_slow, j_slow, direction_slow = self.step(i_slow, j_slow, direction_slow)
            for _ in range(2):
                i_fast, j_fast, direction_fast = self.step(i_fast, j_fast, direction_fast)

            if i_slow == i_fast and j_slow == j_fast and direction_slow == direction_fast:
                return True 
        return False

    def part_2(self):
        # check all previously visited locations and see if putting an obsticle there creates a loop 
        result = 0
        for i_obsticle, j_obsticle in self.visited:
            if self.map[i_obsticle][j_obsticle] == '#' or (i_obsticle == self.i_starting and j_obsticle == self.j_starting):
                continue
            self.map[i_obsticle][j_obsticle] = '#'
            result += self.fast_slow_simulate()
            self.map[i_obsticle][j_obsticle] = '.'
        return result

def main():
    day06_testcase_path = Path('/home/toomeh/for-fun/aoc-2024/day06/day06_testcase.txt')
    day06_data_path = Path('/home/toomeh/for-fun/aoc-2024/day06/day06_data.txt')
    with open(day06_testcase_path, 'r') as file:
        testcase = file.read()
    # Test case
    test_map = Map(testcase)
    test_map.simulate()
    test_result_1 = len(test_map.visited)
    expected_test_result_1 = 41

    if test_result_1 == expected_test_result_1:
        print("Part 1 Testcase passed")
    else:
        print(f"Part 1 Testcase failed. Result is: {test_result_1}")

    with open(day06_data_path, 'r') as file:
        data = file.read()
    data_map = Map(data)

    data_map.simulate()
    result_1 = len(data_map.visited)
    print(f'Part 1 Result: {result_1}')

    
    expected_test_result_2 = 6 
    test_result_2 = test_map.part_2()

    if test_result_2 == expected_test_result_2:
        print("Part 2 Testcase passed")
    else:
        print(f"Part 2 Testcase failed. Result is: {test_result_2}")

    result_2 = data_map.part_2()
    print(f'Part 2 Result: {result_2}')
    

if __name__ == '__main__':
    main()