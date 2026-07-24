class Solution:
    def maxArea(self, height: List[int])->int:
        area=0
        i=0
        j=len(height)-1
        while i<j:
            if height[i]>height[j]:
                if height[j]*(j-i)>area:
                    area=height[j]*(j-i)
                j-=1
            else:
                if height[i]*(j-i)>area:
                    area=height[i]*(j-i)
                i+=1
        return area
