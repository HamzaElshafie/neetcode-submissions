# Approach
# We will do an MxN loop over the grid
# If cell is "X", we just leave as it is
# If cell is O, we need to start a search process that will search through its entire connected O-region, if we never reach a cell within its "O" region thats at the boundary, then we need to change the whole region cells that were visited to "X"
# Maybe that could be done by each cell doing recursive calls and if they all return False than we captured a region
# But if one call reached a boundary tit will basically propogate back the recursive calls to return a true and so we would visit all the cell positions in a `visited` set that would change them to "X"

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        visited = set()

        def explore_region(i, j):
            stack = [(i,j)]
            visited.add((i,j))

            region_cells = []
            touches_edge = False

            while stack:
                r, c = stack.pop()
                region_cells.append((r,c))
            
                # if cell is at boundary
                if r == 0 or r == rows - 1 or c == 0 or c == cols - 1:
                    touches_edge = True
                
                for row_change, col_change in (
                        (-1, 0),
                        (0, 1),
                        (0, -1),
                        (1, 0),
                ):
                    new_r = r + row_change
                    new_c = c + col_change

                    if (
                        0 <= new_r < rows
                        and 0 <= new_c < cols
                        and board[new_r][new_c] == "O"
                        and (new_r, new_c) not in visited
                    ):
                        visited.add((new_r, new_c))
                        stack.append((new_r, new_c))

            return region_cells, touches_edge
        
        # main body
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in visited:
                    region_cells, touches_edge = explore_region(i,j)

                    if not touches_edge:
                        for r,c in region_cells:
                            board[r][c] = "X"


