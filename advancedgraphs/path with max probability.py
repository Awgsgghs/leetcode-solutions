class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj=[[] for _ in range(n)]
        for i,(u,v) in enumerate(edges):
            adj[u].append((v,succProb[i]))
            adj[v].append((u,succProb[i]))
        que=[(-1,start_node)]
        visited=set()
        while que:
            prob,node=heapq.heappop(que)
            if node in visited:
                continue
            visited.add(node)
            if node==end_node:
                return -prob
            for neighbor,pr in adj[node]:
                if neighbor not in visited:
                    heapq.heappush(que,(pr*prob,neighbor))
        return 0