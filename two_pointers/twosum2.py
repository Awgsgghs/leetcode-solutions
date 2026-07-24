class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res=[0]*2
        i=0
        j=len(numbers)-1
        while i<j:
            total=numbers[i]+numbers[j]
            if total>target:
                j-=1
            elif total<target:
                i+=1
            else:
                res[0]=i+1
                res[1]=j+1
                break
        return res