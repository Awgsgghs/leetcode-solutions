class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp=root.left if root.left else None
        root.left=root.right if root.right else None
        root.right=temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root