class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0

        l, r = 0, len(heights) - 1

        while l < r:
            #had a mistake here where I used max originally, should always be min
            cur = min(heights[l], heights[r]) * (r - l) 
            maxWater = max(cur, maxWater)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater
