class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
            
        def h1(nums):
            r1, r2 = 0, 0

            for n in nums:
                temp = max(n+r1, r2)
                r1 = r2
                r2 = temp
            return r2
        
        return max(h1(nums[:-1]), h1(nums[1:]))
            

                
