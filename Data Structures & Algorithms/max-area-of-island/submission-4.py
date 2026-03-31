class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # do a dfs for each pos in the grid, should return size of island
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r,c):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or grid[r][c] == 0:
                return 0
            
            grid[r][c] = 0
            
            return 1 + dfs(r+1,c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)


        # We want to run a dfs from each position
        for i in range(ROWS):
            for j in range(COLS):
                size = dfs(i,j) #DFS would return size of island
                maxArea = max(maxArea, size)
        return maxArea

