class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxdiam=0
        self.maxlength(root,self.maxdiam)
        return self.maxdiam
    def maxlength(self,root,maxdiam):
        if not root:
            return 0
        leftlength=self.maxlength(root.left,maxdiam)
        rightlength=self.maxlength(root.right,maxdiam)
        self.maxdiam=max(self.maxdiam,leftlength+rightlength)
        return max(leftlength,rightlength)+1
