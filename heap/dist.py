class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap=[]
        for i in range(len(points)):
            dist=-(points[i][0]**2+points[i][1]**2)**0.5
            if len(heap)<k:
                heapq.heappush(heap,[dist,points[i]])
            else:
                heapq.heappushpop(heap,[dist,points[i]])
        return [points for _,points in heap]