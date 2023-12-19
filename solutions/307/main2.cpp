class SegTreeNode {
public: 
    SegTreeNode* left;
    SegTreeNode* right; 
    int start, end; 
    int info; 

    SegTreeNode(int a, int b): start(a), end(b), info(0), left(nullptr), right(nullptr) {} 
};

class NumArray {
    void init(SegTreeNode* node, int a, int b) {
        // 边界条件
        if (a == b) {
            node->info = nums[a]; 
            return; 
        }

        int mid = (a+b) / 2; 
        // 动态开点，两个必须一起开
        if (node->left == nullptr) {
            node->left = new SegTreeNode(a, mid); 
            node->right = new SegTreeNode(mid+1, b); 
        }

        // 递归
        init(node->left, a, mid); 
        init(node->right, mid+1, b); 

        // 更新node的info
        node->info = node->left->info + node->right->info; 
    }

    void UpdateSingle(SegTreeNode* node, int idx, int val) {
        // 这个区间与idx无关
        if (idx < node->start || idx > node->end) return; 

        if (node->start == node->end) {
            node->info = val; 
            return; 
        }

        // 递归
        UpdateSingle(node->left, idx, val); 
        UpdateSingle(node->right, idx, val); 
        // 别忘了更新node的info
        // 相当于后序遍历
        node->info = node->left->info + node->right->info;
    }

    int QueryRange(SegTreeNode* node, int a, int b) {
        // 查询区间不归我管
        // 互斥关系
        if (b < node->start || a > node->end) return 0; 
        
        // 当前区间完全在查询中
        // 包含关系
        if (a <= node->start && b >= node->end) {
            return node->info; 
        }

        // 注意这里不需要mid，直接用a, b递归
        // eg 
        //          [5, 9]
        // [5, 7]           [8, 9]

        // 查询[5, 8]
        // [5, 7]完全在[5, 8]中，直接返回
        // [8, 9]继续递归，8完全在[5, 8]中，直接返回
        // 9与[5, 8]互斥，返回0
        int l = QueryRange(node->left, a, b); 
        int r = QueryRange(node->right, a, b);
        return l+r; 
    }

    SegTreeNode* root; 
    vector<int> nums; 

public:
    NumArray(vector<int>& nums) {
        this->nums = nums; 
        int n = nums.size(); 
        root = new SegTreeNode(0, n-1); 
        init(root, 0, n-1); 
    }
    
    void update(int index, int val) {
        UpdateSingle(root, index, val); 
    }
    
    int sumRange(int left, int right) {
        return QueryRange(root, left, right); 
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */