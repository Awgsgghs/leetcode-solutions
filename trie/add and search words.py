class WordDictionary:

    def __init__(self):
        self.mp = {}

    def addWord(self, word: str) -> None:
        root = self.mp
        for i in word:
            if i not in root:
                root[i] = {}
            root = root[i]
        root['*'] = ''

    def search(self, word: str) -> bool:
        def dfs(root, i):
            if i == len(word):
                if '*' in root:
                    return True
                return False
            char = word[i]
            if char == '.':
                return any(dfs(node, i + 1) for key, node in root.items() if key != '*')
            if char not in root:
                return False
            return dfs(root[char], i + 1)

        return dfs(self.mp, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)