class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for c,v in enumerate(nums):
            diff = target - v
            if diff in s:
                return [s[diff], c]
            s[v] = c



                