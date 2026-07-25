class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr,l,r):
            if l==n and r==n:
                res.append(curr[:])
                return
            if l<n:
                backtrack(curr+'(',l+1,r)
            if r<l:
                backtrack(curr+')',l,r+1)
        res=[]
        curr=""
        backtrack(curr,0,0)
        return res