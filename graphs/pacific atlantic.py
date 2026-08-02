class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        def dfs(i, j, visited, prev_height):
            if (i < 0 or j < 0 or i >= ROWS or j >= COLS or heights[i][j] < prev_height or (i, j) in visited):
                return
            visited.add((i, j))
            dfs(i - 1, j, visited, heights[i][j])
            dfs(i + 1, j, visited, heights[i][j])
            dfs(i, j - 1, visited, heights[i][j])
            dfs(i, j + 1, visited, heights[i][j])

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS - 1, c, atlantic, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS - 1, atlantic, heights[r][COLS - 1])
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    res.append([r, c])
        return res



