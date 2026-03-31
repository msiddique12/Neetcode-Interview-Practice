class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums) + 1)]

        dp[0][0] = 1 # 0 elems availbale, sum is 0, 1 way to have that

        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i+1][cur_sum + nums[i]] += count
                dp[i+1][cur_sum - nums[i]] += count
        
        return dp[len(nums)][target]



        # dp = {}
        # def dfs(i, sum):
        #     if i == len(nums):
        #         if sum == target:
        #             return 1
        #         return 0

        #     if (i, sum) in dp:
        #         return dp[(i, sum)]
            
        #     #two choices - add or minus
        #     add = dfs(i+1, sum+nums[i])
        #     sub = dfs(i+1, sum-nums[i])

        #     dp[(i, sum)] = add + sub
        #     return dp[(i, sum)]
        
        # return dfs(0,0)
        