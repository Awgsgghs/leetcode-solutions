class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mp=set()
        for i in nums:
            if i in mp:
                return True
            else:
                mp.add(i)
        return False