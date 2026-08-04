class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        def rob(numso):
            if len(numso) == 1:
                return numso[0]
            n=len(numso)
            dp=[0]*n
            dp[0]=numso[0]
            dp[1]=max(numso[0],numso[1])
            for i in range(2,n):
                dp[i]=max(numso[i]+dp[i-2],dp[i-1])
            return dp[n-1]
        return max(rob(nums[:-1]),rob(nums[1:]))