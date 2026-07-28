class Solution:
    def dfs(self,root):
        if not root:
            return 0
        left=max(0,self.dfs(root.left))
        right=max(0,self.dfs(root.right))
        self.ans=max(self.ans, left+right+root.val)
        return root.val+max(left,right)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans=float('-inf')
        self.dfs(root)
        return self.ans