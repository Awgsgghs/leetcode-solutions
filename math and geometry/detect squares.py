class DetectSquares:

    def __init__(self):
        self.d=Counter()
        self.x_coord=defaultdict(set)

    def add(self, point: List[int]) -> None:
        x,y=point
        self.d[x,y]+=1
        self.x_coord[x].add(y)

    def count(self, point: List[int]) -> int:
        x,y=point
        ans=0
        for y2 in self.x_coord[x]:
            if y==y2:continue
            ans+=self.d[x,y2]*self.d[x-y+y2,y2]*self.d[x-y+y2,y]
            ans+=self.d[x,y2]*self.d[x+y-y2,y2]*self.d[x+y-y2,y]
        return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)