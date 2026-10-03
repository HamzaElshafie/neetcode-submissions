class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def search(row, col, idx, visited):
            # Invalid path
            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or (row, col) in visited
                or board[row][col] != word[idx]
            ):
                return False

            # This cell matched the final character
            if idx == len(word) - 1:
                return True

            # Use this cell for the current path
            visited.add((row, col))

            found = (
                search(row - 1, col, idx + 1, visited)
                or search(row + 1, col, idx + 1, visited)
                or search(row, col - 1, idx + 1, visited)
                or search(row, col + 1, idx + 1, visited)
            )

            # Undo this choice before trying another path
            visited.remove((row, col))

            return found

        for row in range(rows):
            for col in range(cols):
                if search(row, col, 0, set()):
                    return True

        return False



# So what we can do is do an (MxN) loop over the grid asking if the entry matches the first char in word. If yes, we start the search process, otherwise we skip. 

# The search will be recursive, looking left, right, up, down. During each search process, we start with a visited set() to keep track of which cells have been previously visited.

