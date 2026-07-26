class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left=0
        res=[]
        deq=deque()
        for right in range(len(nums)):
            if deq and deq[0]==right-k:
                deq.popleft()
            while deq and nums[deq[-1]]<nums[right]:
                deq.pop()
            deq.append(right)
            if right>=k-1:
                res.append(nums[deq[0]])
        return res