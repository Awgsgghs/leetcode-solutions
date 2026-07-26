class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left=0
        maxlength=0
        maxfreq=0
        maxfreqs={}
        for right in range(len(s)):
            maxfreqs[s[right]]=maxfreqs.get(s[right],0)+1
            maxfreq=max(maxfreq,maxfreqs[s[right]])
            while right+1-left-maxfreq>k:
                maxfreqs[s[left]]-=1
                left+=1
            maxlength=max(maxlength,right-left+1)
        return maxlength
