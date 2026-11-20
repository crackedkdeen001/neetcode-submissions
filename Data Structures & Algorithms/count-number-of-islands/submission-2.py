class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, columns = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
        islands = 0
        
        def dfs(x, y):
            stack = [(x, y)]

            while stack:
                cur_row, cur_col = stack.pop()
                for r, c in directions:
                    row = cur_row + r
                    column = cur_col + c

                    # while we're in bounds
                    if (row < rows
                        and column < columns
                        and row > -1
                        and column > -1) :
                        if grid[row][column] == "1":
                            stack.append((row, column))
            
                grid[cur_row][cur_col] = 0 

        for row in range(rows):
            for column in range(columns):
                box = grid[row][column]
                if box == "1":
                    dfs(row, column)
                    islands += 1

        return islands