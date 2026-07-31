class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start,curr):
            self.res.append(curr)
            for i in range(start,len(nums)):
                backtrack(i+1,curr+[nums[i]])
        curr=[]
        self.res=[]
        backtrack(0,curr)
        return self.res
