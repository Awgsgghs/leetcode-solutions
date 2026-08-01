class TrieNode:
    def __init__(self):
        self.children={}
        self.index=-1
        self.palindromes=[]
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        root=TrieNode()
        def is_palindrome(s,l,r):
            while l<r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        for i, word in enumerate(words):
            node = root
            for j in range(len(word) - 1, -1, -1):
                ch = word[j]
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
                if is_palindrome(word, 0, j - 1):
                    node.palindromes.append(i)
            node.index = i
        res=set()
        for i,word in enumerate(words):
            node=root
            if word == "":
                for j, other_word in enumerate(words):
                    if i != j and is_palindrome(other_word, 0, len(other_word) - 1):
                        res.add((i, j))
                        res.add((j, i))
                continue
            for j,ch in enumerate(word):
                if node.index!=-1 and node.index!=i:
                    if is_palindrome(word,j,len(word)-1):
                        res.add((i,node.index))
                if ch not in node.children:
                    break
                node=node.children[ch]
            else:
                for j in node.palindromes:
                    if i!=j:
                        res.add((i,j))
                if node.index!=-1 and node.index!=i:
                    res.add((i,node.index))
        return [list(pair) for pair in res]