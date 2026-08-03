class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in flights:
            adj[u].append((v, w))
        que = [(0, src, 0)]
        stops = [float('inf')] * (n)
        while que:
            price, node, stop = heapq.heappop(que)
            if node == dst:
                return price
            if stop > stops[node]:
                continue
            if stop > k:
                continue
            stops[node] = stop
            for neighbor, pr in adj[node]:
                heapq.heappush(que, (price + pr, neighbor, stop + 1))
        return -1

