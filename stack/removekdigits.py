class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        for c in num:
            while res and k and res[-1] > c:
                res.pop()
                k -= 1
            res.append(c)
        if k > 0:
            res = res[:-k]
        ans = "".join(res).lstrip("0")
        return ans if ans else "0"


