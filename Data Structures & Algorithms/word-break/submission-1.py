class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #bottom up dp approach
        dp = [False for _ in range(len(s) + 1)]
        dp[-1] = True


        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                lenWord = len(w)
                if i + lenWord > len(s):
                    continue
                
                if w == s[i:i+lenWord] and dp[i+lenWord]:
                    dp[i] = True
                
        return dp[0]