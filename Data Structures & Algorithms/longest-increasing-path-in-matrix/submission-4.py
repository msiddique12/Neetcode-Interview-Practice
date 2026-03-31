class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])

        dp = {} # (r,c):LIP

        def dfs(r, c, pv):
            if r < 0 or c < 0 or r == ROWS or c == COLS or matrix[r][c] <= pv:
                return 0

            if (r,c) in dp:
                return dp[(r,c)]
            
            res = 1
            dir = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in dir:
                res = max(res, 1 + dfs(r+dr, c+dc, matrix[r][c]))
            dp[(r,c)] = res
            return dp[(r,c)]

        
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,-1)
        return max(dp.values())



        