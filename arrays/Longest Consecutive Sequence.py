class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            s.add(i)
        maxlength=0
        for i in s:
            if i-1 not in s:
                currentnum=i
                currentlength=1
                while currentnum+1 in s:
                    currentlength+=1
                    currentnum+=1
                maxlength=max(maxlength,currentlength)
        return maxlength
