class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def dfs(i, sum):
            if i == len(nums):
                if sum == target:
                    return 1
                return 0

            if (i, sum) in dp:
                return dp[(i, sum)]
            
            #two choices - add or minus
            add = dfs(i+1, sum+nums[i])
            sub = dfs(i+1, sum-nums[i])

            dp[(i, sum)] = add + sub
            return dp[(i, sum)]
        
        return dfs(0,0)
        