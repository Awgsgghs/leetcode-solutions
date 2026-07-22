class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp = {}
        for i in range(0, len(nums)):
            if nums[i] in mp.keys():
                return [mp[nums[i]], i]
            else:
                mp[target - nums[i]] = i
        return 0

