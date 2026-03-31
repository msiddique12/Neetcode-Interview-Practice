class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = {i:[] for i in range(N)} #list of [cost, node]

        for i in range(N):
            x1, y1 = points[i]
            for j in range(i+1, N):
                x2, y2 = points[j]
                md = abs(x1 - x2) + abs(y1 - y2)
                adj[i].append([md, j])
                adj[j].append([md, i])

        
        # Prims
        res = 0
        visit = set()
        minHeap = [[0, 0]]
        while len(visit) < N:
            cost, i = heapq.heappop(minHeap)
            if i in visit: continue
            res += cost
            visit.add(i)

            for nc, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(minHeap, [nc, nei])
        return res
            


