class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dists = [[float('inf') for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dists[i][i] = 0
        for u, v, w in edges:
            dists[u][v] = w
            dists[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])
        min_neighbors, result_city = float('inf'), -1
        for i in range(n):
            count = sum(1 for j in range(n) if i != j and dists[i][j] <= distanceThreshold)
            if count <= min_neighbors:
                min_neighbors = count
                result_city = i
        return result_city

