class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[False]*(n+1)
        dp[0]=True
        wordSet = set(wordDict)
        for i in range(len(s)):
            for j in range(i+1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1]=True
                    break
        return dp[n]