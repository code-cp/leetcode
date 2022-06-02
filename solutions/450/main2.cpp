/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    TreeNode* deleteNode(TreeNode* root, int key) {
        // key is not found 
        if (root == nullptr) return root; 
        if (root->val == key) {
            // left is empty, right is not, return right 
            if (root->left == nullptr) return root->right; 
            // right is null, left is not, return left 
            else if (root->right == nullptr) return root->left; 
            else {
                // both children non empty, more complicated 
                // put left to be under the leftmost child of right tree 
                TreeNode* cur = root->right; 
                // find leftmost child of right tree  
                while (cur->left != nullptr) cur = cur->left; 
                cur->left = root->left; 
                root = root->right; 
                return root; 
            }
        }
        if (root->val > key) root->left = deleteNode(root->left, key); 
        if (root->val < key) root->right = deleteNode(root->right, key); 
        return root; 
    }
};