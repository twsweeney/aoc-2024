from pathlib import Path 

class RobotMap:
    def __init__(self, map_data, n_seconds, testcase=False) -> None:
        self.n_seconds = n_seconds
        self.positions = {}
        self.velocities = {}
        for index, line in enumerate(map_data.strip().split('\n')):
            pos_str, velocity_str = line.split(' ')
            x, y = pos_str.split('=')[1].split(',')
            v_x, v_y = velocity_str.split('=')[1].split(',')
            self.positions[index] = (int(x), int(y))
            self.velocities[index] = (int(v_x), int(v_y))
        self.n_robots = len(self.positions)
        if testcase:
            self.n_rows = 7
            self.n_columns = 11
        else:
            self.n_rows = 103
            self.n_columns = 101


    def step(self) -> None:
        for robot in range(self.n_robots):
            x_final = self.positions[robot][0] + self.velocities[robot][0] 
            x_wrapped_final = x_final % self.n_columns
            y_final = self.positions[robot][1] + self.velocities[robot][1] 
            y_wrapped_final = y_final % self.n_rows
            self.positions[robot] = (x_wrapped_final, y_wrapped_final)

    def simulate_1(self):
        for _ in range(self.n_seconds):
            self.step()
        
    def solve_1(self):
        q1, q2, q3, q4 = 0,0,0,0
        center_column = self.n_columns // 2
        center_row = self.n_rows // 2
        for robot in range(self.n_robots):
            x, y = self.positions[robot]
            if x < center_column and y < center_row:
                q1 += 1 
            if x < center_column and y > center_row:
                q2 += 1  

            if x > center_column and y < center_row:
                q3 += 1 

            if x > center_column and y > center_row:
                q4 += 1 
        return q1 * q2 * q3 * q4
        


    def simulate_2(self):
        t = 0 
        while True:
            self.step()
            t += 1 
            values = self.positions.values()
            unique_values = set(values)
            
            # print(len(unique_values))
            if self.n_robots == len(unique_values):
                # print(len(unique_values))
                return t
            




def main():
    testcase_path = Path('/home/toomeh/for-fun/aoc-2024/day14/day14_testcase.txt')
    data_path = Path('/home/toomeh/for-fun/aoc-2024/day14/day14_data.txt')
    with open(testcase_path, 'r') as file:
        testcase = file.read()
    # Test case
    n_seconds = 100 
    test_map = RobotMap(testcase, n_seconds, testcase=True)
    test_map.simulate_1()
    test_result_1 = test_map.solve_1()
    expected_test_result_1 = 12

    if test_result_1 == expected_test_result_1:
        print("Part 1 Testcase passed")
    else:
        print(f"Part 1 Testcase failed. Result is: {test_result_1}")

    with open(data_path, 'r') as file:
        data = file.read()
    data_map = RobotMap(data, n_seconds)

    # data_map.simulate()
    # result_1 = data_map.solve()
    # print(f'Part 1 Result: {result_1}')
    result_2 = data_map.simulate_2()
    print(result_2)
    
    # expected_test_result_2 = 6 
    # test_result_2 = test_map.part_2()

    # if test_result_2 == expected_test_result_2:
    #     print("Part 2 Testcase passed")
    # else:
    #     print(f"Part 2 Testcase failed. Result is: {test_result_2}")

    # result_2 = data_map.part_2()
    # print(f'Part 2 Result: {result_2}')
    

if __name__ == '__main__':
    main()