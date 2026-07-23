class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp={}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in mp:
                mp[ss]=[s]
            else:
                mp[ss].append(s)
        res=[]
        for i in mp.values():
            res.append(i)
        return res
