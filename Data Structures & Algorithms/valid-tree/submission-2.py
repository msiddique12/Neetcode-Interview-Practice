class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True

       #create adjacency list
        adj = collections.defaultdict(list)
        for x,y in edges:
            adj[x].append(y)
            adj[y].append(x)

       #basically checking for a cycle(tree vs graph)
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False
            
            visit.add(i)
            for nei in adj[i]:
                if nei == prev:
                    continue
                if not dfs(nei, i): return False
            return True

        return dfs(0,-1) and len(visit) == n