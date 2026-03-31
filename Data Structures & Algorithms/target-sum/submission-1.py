class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        output = 0
        def dfs(i, sum):
            nonlocal output
            if i == len(nums):
                if sum == target:
                    output += 1
                return
            
            #two choices - add or minus
            dfs(i+1, sum+nums[i])
            dfs(i+1, sum-nums[i])
        
        dfs(0,0)
        return output
        