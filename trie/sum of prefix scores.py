class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        mp={}
        for word in words:
            root=mp
            for i in word:
                if i not in root:
                    root[i]={}
                root=root[i]
                root['*']=root.get('*',0)+1
        res=[]
        for word in words:
            root=mp
            temp=0
            for i in word:
                root=root[i]
                temp+=root['*']
            res.append(temp)
        return res