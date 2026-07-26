class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m
        halflen = (n + m + 1) // 2
        while left <= right:
            i = (left + right) // 2
            j = halflen - i
            left_A = nums1[i - 1] if i > 0 else float('-inf')
            right_A = nums1[i] if i < m else float('inf')

            left_B = nums2[j - 1] if j > 0 else float('-inf')
            right_B = nums2[j] if j < n else float('inf')
            if left_A <= right_B and left_B <= right_A:
                if (n + m) % 2 == 0:
                    return (max(left_A, left_B) + min(right_B, right_A)) / 2
                else:
                    return max(left_A, left_B)
            elif left_A > right_B:
                right = i - 1
            else:
                left = i + 1
        return 0.0
