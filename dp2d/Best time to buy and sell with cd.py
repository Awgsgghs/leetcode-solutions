class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp=[[0 for _ in range(len(prices)+1)] for _ in range(3)]
        dp[0][0]=-prices[0]
        dp[1][0]=0
        dp[2][0]=0
        for i in range(3):
            for j in range(1,len(prices)+1):
                if i==0:
                    dp[0][j]=max(dp[0][j-1],dp[2][j-1]-prices[j-1])
                dp[1][j]=dp[0][j-1]+prices[j-1]
                dp[2][j]=max(dp[1][j-1],dp[2][j-1])
        return max(dp[2][len(prices)],dp[1][len(prices)])