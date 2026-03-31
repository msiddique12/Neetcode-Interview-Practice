class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        return False
    
    def sumOfSquares(self, n: int) -> int:
        digits = []
        while n != 0:
            dig = n % 10
            digits.append(dig)
            n //= 10
        
        res = 0
        for n in digits:
            res += n**2
        
        return res


        





        
