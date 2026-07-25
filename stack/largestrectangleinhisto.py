class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        res = []
        heights.append(0)
        for i in range(len(heights)):
            while res and heights[i] < heights[res[-1]]:
                h = heights[res.pop()]
                w = (i - res[-1] - 1) if res else i
                maxarea = max(maxarea, h * w)
            res.append(i)
        return maxarea
