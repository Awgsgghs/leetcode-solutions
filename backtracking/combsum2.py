class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        curr=[]
        candidates.sort()
        def backtrack(i):
            if sum(curr)==target:
                res.append(curr[:])
                return
            if sum(curr)>target:
                return
            if i>=len(candidates):
                return
            curr.append(candidates[i])
            backtrack(i+1)
            curr.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            backtrack(i+1)
        backtrack(0)
        return res