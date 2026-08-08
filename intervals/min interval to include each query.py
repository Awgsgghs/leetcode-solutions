class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals=sorted(intervals,key=lambda x:x[0])
        sorted_que=sorted((q,i) for i,q in enumerate(queries))
        i=0
        n=len(intervals)
        que=[]
        res=[0]*len(queries)
        for q,idx in sorted_que:
            while i<n and intervals[i][0]<=q:
                start,end=intervals[i]
                length = end-start+1
                heapq.heappush(que,(length,end))
                i+=1
            while que and que[0][1]<q:
                heapq.heappop(que)
            if que:
                res[idx]=que[0][0]
            else:
                res[idx]=-1
        return res