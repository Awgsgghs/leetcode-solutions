class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp=set()
        left=0
        maxlength=0
        for right in range(len(s)):
            while s[right] in mp:
                mp.remove(s[left])
                left+=1
            mp.add(s[right])
            maxlength=max(maxlength, right-left+1)
        return maxlength