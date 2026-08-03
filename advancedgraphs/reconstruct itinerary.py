class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj=defaultdict(list)
        for src,dst in tickets:
            adj[src].append(dst)
        for srt in adj:
            adj[srt].sort(reverse=True)
        route=[]
        def dfs(airport):
            while adj[airport]:
                nextel=adj[airport].pop()
                dfs(nextel)
            route.append(airport)
        dfs("JFK")
        return route[::-1]
