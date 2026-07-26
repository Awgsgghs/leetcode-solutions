class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        maxlength=0
        total=0
        for right in range(len(nums)):
            total+=nums[right]
            while right-left+1-total>k:
                total-=nums[left]
                left+=1
            maxlength=max(maxlength, right-left+1)
        return maxlength