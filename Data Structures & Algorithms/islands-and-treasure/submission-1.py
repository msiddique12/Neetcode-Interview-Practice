class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addRoom(r, c):
            if (r < 0 or c < 0 or r >= R or 
            c >= C or (r,c) in visit or grid[r][c] == -1):
                return
            visit.add((r,c))
            q.append([r,c])



        
        

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
            
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()

                grid[r][c] = dist
                addRoom(r-1,c)
                addRoom(r+1,c)
                addRoom(r,c-1)
                addRoom(r,c+1)
            dist += 1

