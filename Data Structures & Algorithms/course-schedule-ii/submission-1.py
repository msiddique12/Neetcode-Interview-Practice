class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        pre = defaultdict(list)

        for course, prereq in prerequisites:
            pre[course].append(prereq)
        
        # Course has 3 possible states: visited, visiting, unvisited
        output = []
        visit, cycle = set(), set()
        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in visit:
                return True
            
            cycle.add(crs)
            for p in pre[crs]:
                if not dfs(p):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return []
        return output
            

