class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        nums.sort(reverse=True)
        target = sum(nums) // k
        used = [False] * len(nums)

        def backtrack(i, k, s):
            if k == 0:
                return True
            
            if s == target:
                return backtrack(0,k-1,0)
            
            for j in range(i, len(nums)):
                if used[j] or s + nums[j] > target:
                    continue
                
                used[j] = True
                if backtrack(j+1,k,s+nums[j]):
                    return True
                used[j] = False
            return False
            
            
        return backtrack(0,k,0)





        # nums.sort(reverse=True)
        # n = len(nums)
        # tot = sum(nums)
        # if tot % k != 0:
        #     return False
        # target = tot // k

        # sub = [0] * k
        
        # def backtrack(i):
        #     if i == n:
        #         return True


        #     for j in range(k):
        #         if sub[j] + nums[i] <= target:
        #             sub[j] += nums[i]

        #             if backtrack(i + 1):
        #                 return True

        #             sub[j] -= nums[i]
                
        #     return False
        # return backtrack(0)
                    


