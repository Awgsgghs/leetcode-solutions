class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        for j in range(1,len(nums)):
            while i<j and nums[i]!=0:
                i+=1
            if nums[j]!=0:
                nums[i],nums[j]=nums[j], nums[i]
                i+=1