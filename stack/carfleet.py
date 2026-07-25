class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedpos=[]
        for i in range(len(position)):
            speedpos.append([position[i],speed[i]])
        speedpos.sort(reverse=True)
        times=[]
        for i in range(len(speedpos)):
            time=(target-speedpos[i][0])/speedpos[i][1]
            if not times or time>times[-1]:
                times.append(time)
        return len(times)