class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if (i, j) in visited:
                return 0
            
            if  i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return 1

            if grid[i][j] == 0:
                return 1

            visited.add((i,j))

            return (
                dfs(i-1, j) + # up
                dfs(i+1, j) + # down
                dfs(i, j-1) + # left
                dfs(i, j+1) # right
            )

        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)
        return 0
             

