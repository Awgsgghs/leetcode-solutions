class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp=dict()
        res=[]
        for i in range(len(nums2)):
            while res and res[-1]<nums2[i]:
                mp[res[-1]]=nums2[i]
                res.pop()
            res.append(nums2[i])
        result=[]
        for i in nums1:
            if i in mp.keys():
                result.append(mp[i])
            else:
                result.append(-1)
        return result