class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        currjumps=0
        for i in range(len(nums)-1):
            if nums[i]>currjumps:
                currjumps=nums[i]
            if currjumps==0:
                return False
            currjumps-=1
        return True