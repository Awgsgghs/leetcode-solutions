class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            row = mid // len(matrix[0])
            coloumn = mid % len(matrix[0])
            if matrix[row][coloumn] < target:
                left = mid + 1
            elif matrix[row][coloumn] > target:
                right = mid - 1
            else:
                return True
        return False
