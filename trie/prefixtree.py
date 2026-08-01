class Trie:

    def __init__(self):
        self.mp={}

    def insert(self, word: str) -> None:
        root=self.mp
        for i in word:
            if i not in root:
                root[i]={}
            root=root[i]
        root['*']=''

    def search(self, word: str) -> bool:
        root=self.mp
        for i in word:
            if i not in root:
                return False
            root=root[i]
        if '*' not in root:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        root=self.mp
        for i in prefix:
            if i not in root:
                return False
            root=root[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)