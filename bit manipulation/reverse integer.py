class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        reverse=0
        x=abs(x)
        while x:
            reverse=reverse*10+x%10
            x=x//10
        reverse*=sign
        if reverse>2**31 or reverse<-2**31:
            return 0
        else:
            return reverse