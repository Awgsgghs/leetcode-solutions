class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum=sum(nums)
        if (total_sum+target)%2!=0 or abs(target) > total_sum:
            return 0
        K=(total_sum+target)//2
        dp=[0]*(K+1)
        dp[0]=1
        for num in nums:
            for i in range(K,num-1,-1):
                dp[i]=dp[i]+dp[i-num]
        return dp[K]