class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #t: n! * n^2
        #s: n! * n
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1:])
        res = []
        for p in perms:
            for i in range(len(p) + 1):
                pcopy = p.copy()
                pcopy.insert(i, nums[0])
                res.append(pcopy)

        return res