class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals=sorted(intervals,key=lambda x:(x[0],x[1]))
        res=[]
        start=intervals[0][0]
        end=intervals[0][1]
        for interval in intervals[1:]:
            if interval[0]>end:
                res.append([start,end])
                start=interval[0]
                end=interval[1]
            elif interval[0]<=end and interval[1]>end:
                end=interval[1]
            elif interval[1]<=end:
                continue
        res.append([start,end])
        return res
