class Solution:
    def trap(self, height: List[int]) -> int:
        result=0
        i=0
        j=len(height)-1
        maxleft=0
        maxright=0
        while i<j:
            if height[i]<=height[j]:
                maxleft=max(maxleft,height[i])
                result+=maxleft-height[i]
                i+=1
            else:
                maxright=max(maxright,height[j])
                result+=maxright-height[j]
                j-=1
        return result