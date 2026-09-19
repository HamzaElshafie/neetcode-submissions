from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()

        # find all treasure cells
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    queue.append((i,j))

        # BFS from every treasure at once
        while queue:
            row, col = queue.popleft()

            for row_change, col_change in [
                (-1,0), # up
                (0,1), # right
                (0,-1), # left
                (1,0) # down
            ]:
                new_row = row + row_change
                new_col = col + col_change

                if (
                    0 <= new_row < len(grid)
                    and 0 <= new_col < len(grid[0])
                ):
                    if grid[new_row][new_col] == 2147483647:
                        grid[new_row][new_col] = grid[row][col] + 1
                        queue.append((new_row, new_col))
    
            

        


            
