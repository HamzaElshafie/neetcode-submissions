# we need to have a set to keep track of visited indices in the current path
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        # recursive function
        def island_search(i, j, visited):
            # base case
            if grid[i][j] == "0" or (i, j) in visited:
                return

            visited.add((i, j))

            # check left
            if j > 0:
                island_search(i, j-1, visited)
            # check right
            if j < len(grid[0]) - 1:
                island_search(i, j+1, visited)
            # check up 
            if i > 0:
                island_search(i-1, j, visited)
            # check down
            if i < len(grid) - 1 :
                island_search(i+1, j, visited)

        # iterate over each element in grid
        # if position is water "0" skip
        # if position is land "1", start search recursively
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (grid[i][j] == "0") or ((i, j) in visited):
                    continue
                else:
                    island_search(i, j, visited)
                    num_islands += 1

        return num_islands 
