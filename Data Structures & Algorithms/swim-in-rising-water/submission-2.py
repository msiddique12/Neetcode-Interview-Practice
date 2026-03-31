class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()

        minHeap = [[grid[0][0], 0, 0]]
        directions = [[0,1], [0,-1], [1,0], [-1,0 ]]

        while minHeap:
            mh, r, c = heapq.heappop(minHeap)
            visit.add((r,c))

            if r == N-1 and c == N-1:
                return mh

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 0 or nc < 0 or nr >= N or nc >= N or (nr,nc) in visit:
                    continue
                visit.add((nr,nc))
                heapq.heappush(minHeap, [max(mh, grid[nr][nc]), nr, nc])

        


            