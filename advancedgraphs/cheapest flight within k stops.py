class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float('inf')] * n
        prices[src] = 0
        for _ in range(k + 1):
            temp = prices.copy()
            for u, v, w in flights:
                if prices[u] == float('inf'):
                    continue
                if w + prices[u] < temp[v]:
                    temp[v] = w + prices[u]
            prices = temp
        return prices[dst] if prices[dst] != float('inf') else -1

