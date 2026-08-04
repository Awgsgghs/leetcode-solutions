class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp=[[False for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i]=True
        max_length=0
        max_substr=""
        for length in range(2,len(s)):
            for i in range(len(s)-length+1):
                j=i+length-1
                if s[i]==s[j]:
                    if length==2 or dp[i+1][j-1]:
                        dp[i][j]=True
                        if length>max_length:
                            max_length=length
                            max_substr=s[i:j+1]
        return max_substr