class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(curr):
            if len(curr)==len(nums):
                res.append(curr[:])
            for i in range(len(nums)):
                if nums[i] not in curr:
                    backtrack(curr+[nums[i]])
        backtrack([])
        return res