from pathlib import Path 
class XmasGrid:
    def __init__(self, grid_data:str):
        self.grid = grid_data.strip().split('\n')
        self.n_rows = len(self.grid)
        self.n_columns = len(self.grid[0])




    def is_valid_1(self, i:int, j:int, i_step:int, j_step:int) -> bool:

        row_check = i + 3 * i_step
        column_check = j + 3 * j_step

        if not (0<=row_check<self.n_rows and 0<=column_check<self.n_columns):
            return False

        m = self.grid[i+i_step][j+j_step] == 'M'
        a = self.grid[i+2*i_step][j+2*j_step] == 'A'
        s = self.grid[i+3*i_step][j+3*j_step] == 'S'

        if m and a and s:
            return True 

    def search_1(self, i:int, j:int):
        result = 0 
        for i_step in range(-1, 2, 1):
            for j_step in range(-1, 2, 1):
                if self.is_valid_1(i, j, i_step, j_step):
                    result += 1 
        return result 



    
    def count_1(self) -> int:
        result = 0
        for i in range(self.n_rows):
            for j in range(self.n_columns):
                if self.grid[i][j] == 'X':
                    result += self.search_1(i, j)
        return result 






    #######################################################################
    # Part 2 
    #######################################################################

    def is_valid_2(self, i:int, j:int) -> bool:
        if not (0<=i+1<self.n_rows and 0<=i-1<self.n_rows and 0<=j+1<self.n_columns and 0<=j-1<self.n_columns):
            return False
        diagonals = [[(1, 1), (-1, -1)], [(1, -1), (-1, 1)]]
        diagonal_result = []
        for  diagonal in diagonals:
            step_1, step_2 = diagonal
            char_1 = self.grid[i+step_1[0]][j+step_1[1]]
            char_2 = self.grid[i+step_2[0]][j+step_2[1]]
            diagonal_result.append((char_1=='M' and char_2=='S') or (char_1=='S' and char_2=='M'))
        return all(diagonal_result)
    
    def count_2(self):
        result = 0 
        for i in range(self.n_rows):
            for j in range(self.n_columns):
                if self.grid[i][j] == 'A':
                    result += self.is_valid_2(i, j)
        return result  
        




def main():
    day04_testcase_path = Path('/home/toomeh/for-fun/aoc-2024/day04/day04_testcase.txt')
    day04_data_path = Path('/home/toomeh/for-fun/aoc-2024/day04/day04_data.txt')


    with open(day04_testcase_path, 'r') as file:
        testcase = file.read()
    # Test case
    test_grid = XmasGrid(testcase)
    test_result_1 = test_grid.count_1()
    expected_test_result_1 = 18

    if test_result_1 == expected_test_result_1:
        print("Part 1 Testcase passed")
    else:
        print(f"Part 1 Testcase failed. Result is: {test_result_1}")


    with open(day04_data_path, 'r') as file:
            main_data = file.read()
    main_grid = XmasGrid(main_data)
    main_result_1 = main_grid.count_1()
    print(f"Part 1 Main data result: {main_result_1}")


    # part 2 

    test_result_2 = test_grid.count_2()
    expected_test_result_2 = 9

    if test_result_2 == expected_test_result_2:
        print("Part 2 Testcase passed")
    else:
        print(f"Part 2 Testcase failed. Result is: {test_result_2}")

    main_result_2 = main_grid.count_2()
    print(f"Part 2 Main data result: {main_result_2}")



if __name__ == '__main__':
    main()