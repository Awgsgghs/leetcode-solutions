class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        while left<=right:
            mid=(left+right)//2
            day=0
            i=0
            while i<len(weights):
                summa=0
                while i<len(weights) and summa+weights[i]<=mid:
                    summa+=weights[i]
                    i+=1
                day+=1
            if day>days:
                left=mid+1
            else:
                right=mid-1
        return left