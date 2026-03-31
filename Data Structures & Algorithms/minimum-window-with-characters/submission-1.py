from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        #create counter for t
        ct = Counter(t)
        #hashmap for counting s
        cs = {}

        have = 0
        need = len(ct)

        #sliding window with active counter
        l = 0
        res = [-1, -1]
        minLen = float("inf")

        #go through 
        for r in range(len(s)):
            char = s[r]
            cs[char] = cs.get(char, 0) + 1

            if char in ct and cs[char] == ct[char]:
                have += 1
            
            while have == need:
                # Update result
                if (r - l + 1) < minLen:
                    res = [l, r]
                    minLen = r - l + 1
                
                # Shrink window
                cs[s[l]] -= 1
                if s[l] in ct and cs[s[l]] < ct[s[l]]:
                    have -= 1
                
                l += 1
            
        l, r = res
        return s[l:r+1] if minLen != float("inf") else ""
