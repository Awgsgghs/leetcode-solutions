class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap=[]
        self.size=k
        for i in range(len(nums)):
            if i<self.size:
                heapq.heappush(self.heap,nums[i])
            else:
                heapq.heappushpop(self.heap,nums[i])

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.size:
            heapq.heappop(self.heap)
        return self.heap[0]