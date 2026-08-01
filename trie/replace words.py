class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        mp={}
        for word in dictionary:
            root=mp
            for i in word:
                if i not in root:
                    root[i]={}
                root=root[i]
            root['*']=''
        sent=list(sentence.split())
        res=[]
        for word in sent:
            root=mp
            replace=""
            needreplace=True
            for i in word:
                if i in root and '*' not in root:
                    replace+=i
                    root=root[i]
                else:
                    if '*' not in root:
                        needreplace=False
                    break
            res.append(replace if needreplace else word)
        return " ".join(res)