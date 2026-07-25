class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res=[]
        for i in range(len(asteroids)):
            alive=True
            while res and res[-1]>0 and asteroids[i]<0:
                if abs(asteroids[i])==res[-1]:
                    alive=False
                    res.pop()
                    break
                elif abs(asteroids[i])<res[-1]:
                    alive=False
                    break
                else:
                    res.pop()
                    continue
            if alive:
                res.append(asteroids[i])
        return res
