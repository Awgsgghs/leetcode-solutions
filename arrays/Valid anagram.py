class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp1={}
        mp2={}
        for c in s:
            mp1[c]=mp1.get(c,0)+1
        for c in t:
            mp2[c]=mp2.get(c,0)+1
        return mp1==mp2