class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = [[] for _ in range(len(points))]
        dist = [float('inf')] * len(points)

        def manhattan(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def alldist(idx, que):
            for ix in range(len(points)):
                if points[ix] != points[idx]:
                    heapq.heappush(que, (manhattan(points[idx], points[ix]), ix))

        visited = set()
        que = []
        alldist(0, que)
        visited.add(0)
        ans = 0
        while len(visited) < len(points):
            dis, node = heapq.heappop(que)
            if node in visited:
                continue
            ans += dis
            visited.add(node)
            alldist(node, que)
        return ans

