class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp={}
        for i in nums:
            mp[i]=mp.get(i,0)+1
        sd=sorted(mp.items(), key=lambda x:x[1], reverse=True)
        res=[]
        for i in range(k):
            res.append(sd[i][0])
        return res
