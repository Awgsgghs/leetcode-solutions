class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlength=len(nums)+1
        left=0
        total=0
        for right in range(len(nums)):
            total+=nums[right]
            while total>=target:
                minlength=min(minlength,right-left+1)
                total-=nums[left]
                left+=1
        return minlength if minlength<len(nums)+1 else 0