class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        count=0
        for bit in range(32):
            for num in nums:
                if num&1<<bit:
                    count+=1
            if count%3==1:
                if bit==31:
                    res|=-1<<bit
                else:
                    res|=1<<bit
            count=0
        return res