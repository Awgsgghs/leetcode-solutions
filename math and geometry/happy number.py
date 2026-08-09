class Solution:
    def __init__(self):
        self.visited=set()
    def isHappy(self, n: int) -> bool:
        if n==1:
            return True
        if n in self.visited:
            return False
        self.visited.add(n)
        newn=0
        while n:
            newn+=(n%10)**2
            n=n//10
        return self.isHappy(newn)