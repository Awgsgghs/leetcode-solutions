class Solution:
    def validate(self,root,minval,maxval):
        if not root:
            return True
        if root.val<=minval or root.val>=maxval:
            return False
        else:
            return self.validate(root.left,minval,root.val) and self.validate(root.right, root.val, maxval)
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))