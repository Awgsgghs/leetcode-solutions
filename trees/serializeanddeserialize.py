class Codec:
    def serialize(self, root):
        if not root:
            return "null"
        que = deque([root])
        res = []
        while que:
            node = que.popleft()
            if node:
                res.append(str(node.val))
                que.append(node.left)
                que.append(node.right)
            else:
                res.append('null')
        return ",".join(res)

    def deserialize(self, data):
        if data == "null": return None
        res = data.split(",")
        root = TreeNode(int(res[0]))
        que = deque([root])
        i = 1
        while que:
            curr = que.popleft()
            if i < len(res) and res[i] != "null":
                curr.left = TreeNode(int(res[i]))
                que.append(curr.left)
            i += 1
            if i < len(res) and res[i] != "null":
                curr.right = TreeNode(int(res[i]))
                que.append(curr.right)
            i += 1
        return root