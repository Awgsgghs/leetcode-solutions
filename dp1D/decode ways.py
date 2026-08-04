class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0]=="0":
            return 0
        dp=[0]*(len(s)+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,len(s)+1):
            num1=int(s[i-1])
            if 1<=num1<=9:
                dp[i]+=dp[i-1]
            num2=int(s[i-2:i])
            if 10<=num2<=26:
                dp[i]+=dp[i-2]
        return dp[len(s)]
