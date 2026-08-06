class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        pairs = [(cap, prof) for cap, prof in zip(capital, profits)]
        sort_pairs = sorted(pairs, key=lambda x: x[0])
        que = []
        i = 0
        for _ in range(k):
            while i < len(profits) and sort_pairs[i][0] <= w:
                heapq.heappush(que, -sort_pairs[i][1])
                i += 1
            if not que:
                break
            w -= heapq.heappop(que)
        return w

