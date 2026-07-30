def addNum(self, num: int) -> None:
    if not len(self.maxheap) or num < -self.maxheap[0]:
        heapq.heappush(self.maxheap, -num)
    else:
        heapq.heappush(self.minheap, num)
    if len(self.minheap) > len(self.maxheap):
        heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
    if len(self.maxheap) == len(self.minheap) + 2:
        heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))


def findMedian(self) -> float:
    if len(self.maxheap) == len(self.minheap):
        return (self.minheap[0] - self.maxheap[0]) / 2.0
    return -self.maxheap[0]