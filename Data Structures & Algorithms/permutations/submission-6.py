class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans, sol = [], []
        used = [False] * n
        def dfs():
            if len(sol) == n:
                ans.append(sol[:])
                return
            
            for i,x in enumerate(nums):
                if used[i] == False:
                    used[i] = True
                    sol.append(x)
                    dfs()
                    sol.pop()
                    used[i] = False

            
        dfs()
        return ans
                


        #NEETCODE SOLUTION - NEED TO UNDERSTAND
        # #t: n! * n^2
        # #s: n! * n
        # if len(nums) == 0:
        #     return [[]]

        # perms = self.permute(nums[1:])
        # res = []
        # for p in perms:
        #     for i in range(len(p) + 1):
        #         pcopy = p.copy()
        #         pcopy.insert(i, nums[0])
        #         res.append(pcopy)

        # return res