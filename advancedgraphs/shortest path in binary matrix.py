class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[len(grid) - 1][len(grid[0]) - 1] == 1:
            return -1
        if len(grid) == 1 and len(grid[0]) == 1:
            if grid[0][0] == 0:
                return 1
            else:
                return -1
        que = deque([(1, (0, 0))])
        grid[0][0] = 1
        directions = [(-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (0, 1), (1, 0), (-1, -1)]
        while que:
            steps, node = que.popleft()
            if node == (len(grid) - 1, len(grid[0]) - 1):
                return steps
            for rd, cd in directions:
                nr = node[0] + rd
                nc = node[1] + cd
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 0:
                    que.append([steps + 1, (nr, nc)])
                    grid[nr][nc] = 1
        return -1



