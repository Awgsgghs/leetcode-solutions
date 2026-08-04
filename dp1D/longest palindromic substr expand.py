class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left,right):
            while left>=0 and right<len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return right-left-1,s[left+1:right]
        maxlength=0
        maxsubstr=""
        for i in range(len(s)):
            length1,substr1=expand(i,i)
            length2,substr2=expand(i,i+1)
            if length1>maxlength:
                maxlength=length1
                maxsubstr=substr1
            if length2>maxlength:
                maxsubstr=substr2
                maxlength=length2
        return maxsubstr