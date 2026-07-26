class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bs(isleft, find=-1):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    if isleft:
                        find = mid
                        right = mid - 1
                    else:
                        find = mid
                        left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return find

        findleft = bs(True)
        findright = bs(False)
        return [findleft, findright]
