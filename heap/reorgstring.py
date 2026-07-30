class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        heap = []
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        for i in freq.keys():
            heapq.heappush(heap, [-freq[i], i])
        while len(heap) >= 2:
            freq1, first = heapq.heappop(heap)
            freq2, second = heapq.heappop(heap)
            res.append(first)
            res.append(second)
            freq1 += 1
            freq2 += 1
            if freq1 < 0:
                heapq.heappush(heap, [freq1, first])
            if freq2 < 0:
                heapq.heappush(heap, [freq2, second])
        if len(heap) != 0:
            finalfreq = heap[0][0]
            if finalfreq < -1:
                return ""
            res.append(heap[0][1])
        return "".join(res)
