class TimeMap:

    def __init__(self):
        self.mp=dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.mp.keys():
            self.mp[key]=[]
        self.mp[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp.keys():
             return ""
        left=0
        right=len(self.mp[key])-1
        res=""
        while left<=right:
            mid=(left+right)//2
            if self.mp[key][mid][1]<=timestamp:
                res=self.mp[key][mid][0]
                left=mid+1
            else:
                right=mid-1
        return res
