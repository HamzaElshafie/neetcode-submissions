class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0

        def dfs(i, j, visited=set()):
            # base case
            if grid[i][j] == 0:
                return 0
            
            if (i, j) in visited:
                return 0                
            
            # Add cell to path
            visited.add((i, j))
            area = 1

            # Check up
            if i > 0:
                area += dfs(i-1, j, visited)
            # Check down
            if i < len(grid) - 1:
                area += dfs(i+1, j, visited)
            # Check left 
            if j > 0:
                area += dfs(i, j-1, visited)
            # Check right
            if j < len(grid[0]) - 1:
                area += dfs(i, j+1, visited)

            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                cur_area = dfs(i, j, set())
                max_area = max(max_area, cur_area)
        return max_area



        