class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        left=0
        right=len(grid)**2-1
        result=0
        def bfs(mid):
            if grid[0][0]>mid:
                return False
            que=deque([(0,0)])
            visited=set((0,0))
            directions=[(-1,0),(1,0),(0,1),(0,-1)]
            while que:
                r,c=que.popleft()
                if r==len(grid)-1 and c==len(grid[0])-1:
                    return True
                for dr,dc in directions:
                    nr=r+dr
                    nc=c+dc
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and (nr,nc) not in visited and grid[nr][nc]<=mid:
                        visited.add((nr,nc))
                        que.append((nr,nc))
            return False
        while left<=right:
            mid=(left+right)//2
            if not bfs(mid):
                left=mid+1
            else:
                result=mid
                right=mid-1
        return result