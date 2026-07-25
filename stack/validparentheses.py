class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                res.append(s[i])
                continue
            else:
                if len(res) == 0:
                    return False
                top = res.pop()
                if (top == "[" and s[i] == "]"):
                    continue
                elif (top == "{" and s[i] == "}"):
                    continue
                elif (top == "(" and s[i] == ")"):
                    continue
                else:
                    return False
        return len(res) == 0

