class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #do a sliding window, maintain count of chars

        maxLen = 0
        letterCounts = {}
        maxFreq = 0
        l = 0

        for r in range(len(s)):
            #keep track of the length of the window
            #keep track of the most frequent char in the window
            letterCounts[s[r]] = letterCounts.get(s[r], 0) + 1
            maxFreq = max(maxFreq, letterCounts.get(s[r], 0))

            #shrink window
            if (r-l+1) - maxFreq > k:
                letterCounts[s[l]] -= 1
                l += 1
            
            maxLen = max(maxLen, r - l + 1)
        return maxLen




