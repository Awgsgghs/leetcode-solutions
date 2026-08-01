class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        mp = {}
        for word in words:
            root = mp
            for i in word:
                if i not in root:
                    root[i] = {}
                root = root[i]
            root['*'] = word

        def backtrack(i, j, root):
            if not root:
                return
            if not (0 <= i < len(board) and 0 <= j < len(board[0])):
                return
            ch = board[i][j]
            if ch not in root:
                return
            root = root[ch]
            if '*' in root:
                res.append(root['*'])
                del root['*']
            board[i][j] = '#'
            backtrack(i - 1, j, root)
            backtrack(i + 1, j, root)
            backtrack(i, j + 1, root)
            backtrack(i, j - 1, root)
            board[i][j] = ch

        for i in range(len(board)):
            for j in range(len(board[0])):
                backtrack(i, j, mp)
        return res


