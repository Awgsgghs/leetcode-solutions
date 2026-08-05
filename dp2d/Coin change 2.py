class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[0 for _ in range(amount+1)] for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0]=1
        for i in range(len(coins)):
            for j in range(1,amount+1):
                if i>0:
                    dp[i][j]=dp[i-1][j]
                if j-coins[i]>=0:
                    dp[i][j]+=dp[i][j-coins[i]]
        return dp[len(coins)-1][amount]