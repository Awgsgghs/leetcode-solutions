class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[v].append((u, w))
            adj[u].append((v, w))

        def deikstra(i):
            que = [(0, i)]
            res = 0
            visited = set()
            while que:
                cost, node = heapq.heappop(que)
                if node in visited:
                    continue
                visited.add(node)
                if node != i:
                    res += 1
                for neighbor, price in adj[node]:
                    if neighbor not in visited and cost + price <= distanceThreshold:
                        heapq.heappush(que, (cost + price, neighbor))
            return res

        result = 0
        min_count = float('inf')
        for i in range(n):
            new_count = deikstra(i)
            if new_count <= min_count:
                min_count = new_count
                result = i
        return result

