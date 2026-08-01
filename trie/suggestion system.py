class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        class Trie:
            def __init__(self):
                self.children = collections.defaultdict(Trie)
                self.suggestions = []

            def add_suggest(self, suggest):
                if len(self.suggestions) < 3:
                    self.suggestions.append(suggest)

        node = Trie()
        for p in products:
            root = node
            for i in p:
                root = root.children[i]
                root.add_suggest(p)

        res = []
        root = node
        for i in searchWord:
            root = root.children[i]
            res.append(root.suggestions)
        return res


