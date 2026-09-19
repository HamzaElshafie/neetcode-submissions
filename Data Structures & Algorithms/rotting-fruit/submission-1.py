# Aproach
# 1) Traverse the grid to find and record the positions of the cells that contain a rotten fruit in a queue
# 2) Start a BFS from the rotten cells with `min=0`
# We pop from the front of the queue
# we try up, right, left, down (if indices within boundaries)
# if cell is empty, we leave as is
# if cell is rotten, we add to queue
# if cell is fresh, we change its value to min+1 (of its parent caller) and add to queue

# once the queue is empty i think even tho there are probably other ways to do it but a first simple once could be to do an mxn loop over the grid and return either -1 if we ever still find a fresh fruit or return the maximum number in the grid


# example run

# Queue
# [
# (2,1) -> 1
# ]

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()

        # 1) find position of the cells that contain a rotten fruit (i, j, minute)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                   queue.append((i,j,0)) 

        minutes_elapsed = 0

        while queue:
            r, c, minute = queue.popleft()
            minutes_elapsed = max(minutes_elapsed, minute)

            for row_change, col_change in (
                [-1, 0], # up
                [0, 1], # right
                [0, -1], # left
                [1, 0] # down
            ):
                new_r = r + row_change
                new_c = c + col_change
                if new_r >= 0 and new_r < len(grid) and new_c >= 0 and new_c < len(grid[0]):
                    if grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        queue.append((new_r, new_c, minute+1))
        
        # final search for output
        out = -999999
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minutes_elapsed





