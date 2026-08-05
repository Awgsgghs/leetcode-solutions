class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        A=[1]+nums+[1]
        n=len(A)
        dp=[[0]*n for _ in range(n)]
        for length in range(2,n):
            for i in range(n-length):
                j=i+length
                for k in range(i+1,j):
                    coins=A[i]*A[k]*A[j]
                    total=dp[i][k]+dp[k][j]+coins
                    dp[i][j]=max(dp[i][j],total)
        return dp[0][n-1]