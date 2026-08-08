class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_loc=max(trip[2] for trip in trips)
        diff=[0]*(max_loc+1)
        for passen,fr,end in trips:
            diff[fr]+=passen
            diff[end]-=passen
        curr_passengers=0
        for i in diff:
            curr_passengers+=i
            if curr_passengers>capacity:
                return False
        return True