class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, sum):
            if i == len(nums):
                if sum == target:
                    return 1
                return 0
            
            #two choices - add or minus
            add = dfs(i+1, sum+nums[i])
            sub = dfs(i+1, sum-nums[i])

            return add + sub
        
        return dfs(0,0)
        