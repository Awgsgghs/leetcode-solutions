class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        que=[(grid[0][0],0,0)]
        visited=set((0,0))
        directions=[(-1,0),(1,0),(0,1),(0,-1)]
        while que:
            time,r,c=heapq.heappop(que)
            if r==len(grid)-1 and c==len(grid[0])-1:
                return time
            for dr,dc in directions:
                nr=r+dr
                nc=c+dc
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and (nr,nc) not in visited:
                    visited.add((nr,nc))
                    maxheight=max(time,grid[nr][nc])
                    heapq.heappush(que,(maxheight,nr,nc))
        return -1