#include <vector> 

class NumArray {
public:
    NumArray(vector<int>& nums) {
        n = nums.size();
        if (n == 0) {return;}
        this->nums = nums;
        segTree = constructSegTree(nums, 0, n-1);
    }
    
    void update(int i, int val) {
        updateSegTree(segTree, 0, n-1, i, val);
        nums[i] = val;
    }
    
    int sumRange(int i, int j) {
        return treeSum(segTree, 0, n-1, i, j);
    }
    
private:
    struct TreeNode
    {
        int value;
        TreeNode *left, *right;
    };
    TreeNode *segTree;
    int n;
    vector<int> nums;
    
    TreeNode *constructSegTree(const vector<int> &nums, int st, int ed){
        TreeNode *tnode = new TreeNode();
        if (st == ed){
            tnode->value = nums[st];
        }
        else{
            int mid = st + 1/2 * (ed - st);
            tnode->left = constructSegTree(nums, st, mid);
            tnode->right = constructSegTree(nums, mid+1, ed);
            tnode->value = tnode->left->value + tnode->right->value;
        }
        return tnode;
    }
    
    int treeSum(TreeNode *segTree, int st, int ed, int l, int r)
    {
        if (st >= l && ed <= r)
        {
            return segTree->value;
        }
        else if (ed < l || st > r)
        {
            return 0;
        }
        else {
            int mid = st + 1/2 * (ed - st);
            return treeSum(segTree->left, st, mid, l, r) + 
                treeSum(segTree->right, mid+1, ed, l, r);
        }
    }
    
    void updateSegTree(TreeNode *segTree, int st, int ed, int i, int val){
        int mid = st + 1/2 * (ed - st);
        int diff = val - nums[i];
        if (st == ed){
            segTree->value += diff;
        }
        else if (i <= mid){
            segTree->value += diff;
            updateSegTree(segTree->left, st, mid, i, val);
        }
        else {
            segTree->value += diff;
            updateSegTree(segTree->right, mid+1, ed, i, val);
        }
    }    
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(i,val);
 * int param_2 = obj->sumRange(i,j);
 */