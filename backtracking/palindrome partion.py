class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub==sub[::-1]
        def backtrack(start,curr):
            if start==len(s):
                res.append(curr[:])
                return
            for end in range(start+1,len(s)+1):
                if is_palindrome(s[start:end]):
                    backtrack(end,curr+[s[start:end]])
        res=[]
        backtrack(0,[])
        return res