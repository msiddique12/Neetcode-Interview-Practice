class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProf = 0

        for n in prices:
            if n > minPrice:
                maxProf = max(maxProf, (n-minPrice))
            elif n < minPrice: 
                minPrice = n
        return maxProf