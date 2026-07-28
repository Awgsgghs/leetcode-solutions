class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res=[]
        self.maxlength=0
        self.length(root,1,self.maxlength)
        return self.res
    def length(self,root, currlength,maxlength):
        if not root:
            return
        if currlength>self.maxlength:
            self.maxlength=currlength
            self.res.append(root.val)
        self.length(root.right,currlength+1,self.maxlength)
        self.length(root.left,currlength+1,self.maxlength)