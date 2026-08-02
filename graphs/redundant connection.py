class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        mp={}
        visited=set()
        def dfs(i,j,visited):
            if i==j:
                return True
            visited.add(i)
            if i in mp:
                for neighbor in mp[i]:
                    if neighbor not in visited:
                        if dfs(neighbor,j,visited):
                            return True
            return False
        for u,v in edges:
            if u in mp and v in mp and dfs(u,v,set()):
                return [u,v]
            if u not in mp:
                mp[u]=[]
            if v not in mp:
                mp[v]=[]
            mp[u].append(v)
            mp[v].append(u)