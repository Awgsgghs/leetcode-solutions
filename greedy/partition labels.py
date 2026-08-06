class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp={}
        for i in range(len(s)):
            mp[s[i]]=i
        end=0
        start=0
        res=[]
        for i in range(len(s)):
            end=max(end,mp[s[i]])
            if i==end:
                res.append(end-start+1)
                start=i+1
        return res