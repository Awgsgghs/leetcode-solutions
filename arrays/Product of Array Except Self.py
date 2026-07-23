class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        leftpr=1
        rightpr=1
        for i in range(len(nums)):
            res[i]=leftpr
            leftpr*=nums[i]
        for i in range(len(nums)-1,-1,-1):
            res[i]*=rightpr
            rightpr*=nums[i]
        return res