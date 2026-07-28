class Solution {
public:
    int maxDepth(TreeNode* root) {
        if (root==nullptr){
            return 0;
        }
        int leftlength=maxDepth(root->left);
        int rightlength=maxDepth(root->right);
        return max(leftlength,rightlength)+1;
    }
};