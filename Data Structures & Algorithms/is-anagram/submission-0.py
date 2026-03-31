class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS = defaultdict(int)
        countT = defaultdict(int)

        for c in s:
            countS[c] += 1
        for x in t:
            countT[x] += 1
        
        if countS != countT:
            return False
        return True
        
            
        

        
        