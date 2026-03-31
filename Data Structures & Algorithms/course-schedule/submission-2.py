class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #adjacency list
        al = collections.defaultdict(list)
        for x,y in prerequisites:
            al[x].append(y)
        
        #visit - all courses along current dfs
        visit = set()

        def dfs(crs):
            if crs in visit:
                return False
            
            if al[crs] == []:
                return True
            
            visit.add(crs)

            for pre in al[crs]:
                if not dfs(pre): return False
            
            visit.remove(crs)
            #al[crs] = []
            return True

        for cr in range(numCourses):
            if not dfs(cr): return False
        return True