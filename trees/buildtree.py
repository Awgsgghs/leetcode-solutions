class Solution:
    def helper(self,preorder, start, end):
        if start>end:return None
        val=preorder[self.preidx]
        self.preidx+=1
        node=TreeNode(val)
        idx=self.mp[val]
        node.left=self.helper(preorder,start,idx-1)
        node.right=self.helper(preorder,idx+1,end)
        return node
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.preidx=0
        self.mp={}
        for i in range(len(inorder)):
            self.mp[inorder[i]]=i
        return self.helper(preorder,0,len(inorder)-1)