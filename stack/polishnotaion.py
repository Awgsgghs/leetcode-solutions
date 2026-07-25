class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=[]
        for s in tokens:
            if s=='+' or s=='-' or s=='*' or s=='/':
                number1=res.pop()
                number2=res.pop()
                if s=='+':
                    res.append(number1+number2)
                elif s=='-':
                    res.append(number2-number1)
                elif s=='/':
                    res.append(int(number2/number1))
                else:
                    res.append(number1*number2)
            else:
                res.append(int(s))
        return res.pop()