class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #compute all combinations that sum to target
        res = []
        #i shows what candidates we have available
        #cur shows current path
        def dfs(i, remaining, path):
            if remaining == 0:
                res.append(path.copy())
                return
            
            if remaining < 0 or i == len(nums):
                return
            
            #include
            path.append(nums[i])
            dfs(i, remaining - nums[i], path)
            #dont include
            path.pop()
            dfs(i+1, remaining, path)
        
        dfs(0, target, [])
        return res
       